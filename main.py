from asyncio import create_task, gather, run, Semaphore
from app.errors.unexpected_status_error import UnexpectedStatusError
from app.logging.logger import getLogger
from app.app import get_urls_to_scrap, scrap_data
from app.settings import MAX_CONCURRENCY


logger = getLogger("main.py")
CONCURRENCY_LIMIT = Semaphore(MAX_CONCURRENCY)


async def main():
  urls = await get_urls_to_scrap()
  tasks = []
  for url in urls:
      task = create_task(scrap_data(url, CONCURRENCY_LIMIT))
      tasks.append(task)
  result = await gather(*tasks)
  return result
  

if __name__ == "__main__":
  logger.info("Initializing application...")
  try:
    app = run(main())
    if app: logger.info("Application completed")
  except UnexpectedStatusError as e:
    logger.error(e)
  except Exception as e:
    logger.error(e)