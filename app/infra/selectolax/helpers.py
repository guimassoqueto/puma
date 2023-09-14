"""
Helper functions to parse data
"""
import re


def get_image_url(item_url: str) -> str:
  """
  Return the product image url. Only work with sneakers.
  """
  product_id = re.search(r"\d{6}-\d{2}", item_url).group()
  code1, code2 = product_id.split("-")
  return f"https://images.puma.com/image/upload/f_auto,q_auto,b_rgb:fff/global/{code1}/{code2}/sv01/fnd/BRA/w/1080/h/1080/fmt/jpg"
