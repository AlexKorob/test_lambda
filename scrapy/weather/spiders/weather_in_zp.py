import scrapy


class WeatherInZpSpider(scrapy.Spider):
    name = 'weather_in_zp'
    allowed_domains = ('https://www.gismeteo.ua', )
    start_urls = ['https://www.gismeteo.ua/weather-zaporizhia-5093/']

    HEADERS = {
        ":authority": "www.gismeteo.ua",
        ":method": "GET",
        ":path": "/weather-zaporizhia-5093/",
        ":scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;"
                  "q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/83.0.4103.61 Safari/537.36",
    }

    def parse(self, response):
        block_with_weather = response.xpath(
            "//div[@class='tabs _center']/a//span[@class='js_value tab-weather__value_l']"
        )
        integer = block_with_weather.xpath("text()").extract_first().strip()
        remainder = block_with_weather.xpath("span/text()").extract_first().strip().replace(",", ".")
        yield {"weather": integer + remainder}
