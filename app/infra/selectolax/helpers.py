"""
Helper functions to parse data
"""
import re
from urllib.parse import quote
from app.settings import AWIN_ID, AWIN_AFFID


def get_image_url(item_url: str) -> str:
  """
  Return the product image url. Only work with sneakers.
  """
  product_id = re.search(r"\d{6}-\d{2}", item_url).group()
  code1, code2 = product_id.split("-")
  return f"https://images.puma.com/image/upload/f_auto,q_auto,b_rgb:fff/global/{code1}/{code2}/sv01/fnd/BRA/w/1080/h/1080/fmt/jpg"


def get_afiliate_link(item_url: str) -> str:
  """
  Return the afiliate url of the provided item.
  """
  if not AWIN_ID: raise Exception("You must provide the AWIN_ID")
  if not AWIN_AFFID: raise Exception("You must provide the AWIN_FFID")
  item_url_encoded=quote(item_url)
  awin_link = f"https://www.awin1.com/cread.php?awinmid={AWIN_ID}&awinaffid={AWIN_AFFID}&ued={item_url_encoded}"
  return awin_link

def encode_url(url: str) -> str:
  return quote(url)
