
from app.infra.aiohttp.aiohttp import AioHttpRetry
from app.settings import PUMA_SNEAKERS_URL
from app.infra.selectolax.parser import Selectolax
from app.logging.logger import getLogger
from app.infra.psycopg.postgres import insert_products
from asyncio import Semaphore
import math


logger = getLogger("app.py")


async def get_urls_to_scrap() -> list[str]:
  try:
    html_content = await AioHttpRetry.get_content(PUMA_SNEAKERS_URL)
    total_items = Selectolax(html_content).get_offers_count()
    total_pages_number = math.ceil(total_items / 36) + 1

    urls_to_scrap = [ PUMA_SNEAKERS_URL ]
    for page_number in range(2, total_pages_number): 
      urls_to_scrap.append(PUMA_SNEAKERS_URL + f"&p={page_number}")

    return urls_to_scrap
  except Exception as e:
    logger.error("Failed to get the list of pages to scrap", exc_info=True)
    raise e
    

async def scrap_data(url: str, concurrency_limit: Semaphore):
  async with concurrency_limit:
    try:
      content = await AioHttpRetry.get_content(url)
      selectolax = Selectolax(content)
      products = selectolax.get_products()
      await insert_products(products)

    except Exception as e:
      logger.error(e)