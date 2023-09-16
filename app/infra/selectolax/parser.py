from app.domain.model import Item
from app.logging.logger import getLogger
from selectolax.parser import HTMLParser
from app.infra.selectolax.helpers import (get_image_url, get_afiliate_link)
import re


logger = getLogger("parser.py")


class Selectolax:
  def __init__(self, content: str) -> int:
    self.parser = HTMLParser(content)


  def get_offers_count(self) -> int:
    """
    Retrieve the quantity of items in offer
    """
    node = self.parser.css_first(".page-products-count")
    raw_inner_text = node.text()

    re_match = re.search(r"\d+", raw_inner_text)
    if re_match is None: raise ValueError("Selectolax did not found the item's quantity.")
    count = int(re_match.group())

    return count
  

  def get_products(self) -> list[dict]:
    """
    Return a list contaning the products scraped.
    """
    all_items = self.parser.css(".grid__item")
    products = []
    for item in all_items:
      try:
        title = item.css_first(".product-item__name").text().strip()
        if not re.search('tênis', title, re.IGNORECASE): continue
        
        url = item.css_first(".product-item__img-w").attrs["href"] # anchor tag with product's url
        image_url = get_image_url(url)
        category = f"Puma Outlet {title}"
        affiliate_url = get_afiliate_link(url)

        price = float(item.css_first('[data-price-type="finalPrice"]').attrs["data-price-amount"])
        previous_price = float(item.css_first('[data-price-type="oldPrice"]').attrs["data-price-amount"])
        discount = round((1 - (price / previous_price)) * 100)
        if discount < 40: continue

        product = Item(
          url=url,
          image_url=image_url,
          afiliate_url=affiliate_url,
          title=title,
          category=category,
          price=price,
          previous_price=previous_price,
          discount=discount
        )
        products.append(product.model_dump())

      except Exception as e:
        logger.error(e)
        continue

    return products
