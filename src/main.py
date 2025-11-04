import asyncio
from apify import Actor
from .models import InputModel
from .auth import load_or_refresh_cookies
from .scraper import WeiboScraper


async def main():
    async with Actor:
        input_data = await Actor.get_input() or {}
        input_cfg = InputModel(**input_data)

        Actor.log.info(f"Starting Weibo lifestyle UGC scraper")
        Actor.log.info(f"Keywords: {input_cfg.keywords}")
        Actor.log.info(f"Pages per keyword: {input_cfg.max_pages}")

        cookies = await load_or_refresh_cookies()
        scraper = WeiboScraper(cookies, input_cfg.max_pages, input_cfg.concurrency)

        for kw in input_cfg.keywords:
            Actor.log.info(f"Scraping keyword: {kw}")
            posts = await scraper.scrape_keyword(kw)
            Actor.log.info(f"{len(posts)} posts for '{kw}'")

            for post in posts:
                await Actor.push_data(post.dict())

        Actor.log.info("Scraping completed successfully.")


if __name__ == "__main__":
    asyncio.run(main())
