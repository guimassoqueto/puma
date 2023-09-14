from playwright.async_api import async_playwright


class Playwright:
  @staticmethod
  async def get_content(url: str) -> str:
    """
    Get the web page full content, dynamic or not.
    """
    async with async_playwright() as pw:
      browser = await pw.chromium.launch(headless=True)
      page = await browser.new_page()
      await page.goto(url, wait_until="networkidle")
      html_content =  await page.content()
      return html_content