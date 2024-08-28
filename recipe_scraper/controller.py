from scrapy.crawler import CrawlerProcess
from datetime import datetime
from recipe_scraper.spiders.goodfood_spider import GoodFoodSpider
from recipe_scraper.file_manager import FileManager

class Controller:

    @staticmethod
    def run_spider(verbose=False, sample=0):
        """
        Sets up a Scrapy CrawlerProcess and performs crawling for GoodFoodSpider.
        :param verbose: prints additional information when true
        :param sample: If greater than 0, will only crawl for n=sample urls
        """
        # Ensure directories are set up and CSV is downloaded
        FileManager.ensure_directories()
        FileManager.download_recipes_csv()

        # Scrapy spider setup
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            'FEED_FORMAT': "json",
            'FEED_URI': "../data/output/" + datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".json"
        })

        # Start crawling
        process.crawl(GoodFoodSpider, sample=sample)
        process.start()

        if verbose:
            print("Crawling completed")
