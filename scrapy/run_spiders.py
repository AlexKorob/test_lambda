from multiprocessing.context import Process
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.utils.project import get_project_settings

from weather.spiders.weather_in_zp import WeatherInZpSpider


def crawl():
    process = CrawlerProcess(get_project_settings())
    process.crawl(WeatherInZpSpider)
    process.start()


def lambda_save_weather_to_db(event, config):
    process = Process(target=crawl)
    process.start()
    process.join()
    return {
        "statusCode": 200,
        "body": "The weather saved!"
    }
