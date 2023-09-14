from app.errors.unexpected_status_error import UnexpectedStatusError
from aiohttp_retry import RetryClient

class AioHttpRetry:
  @staticmethod
  async def get_content(url: str) -> str:
    async with RetryClient() as client:
        async with client.get(url) as response:
          if response.status > 400 and response.status < 500: raise UnexpectedStatusError(response.status)
          return await response.text()