import scrapy


class GoogleSpider(scrapy.Spider):
    name = "google"
    allowed_domains = ["google.com"]
    start_urls = ["https://google.com"]

    def parse(self, response):
        print('12312312')

        print(response.request.headers)
        with open("goo.html","w",encoding="utf-8") as f:
            f.write(response.text)
