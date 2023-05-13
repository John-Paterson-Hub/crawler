from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextracors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = "mycrawler"
    allowed_domains = ["toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    rules = {
        Rule(LinkExtrator(allow="catalogue/catagory")),
        Rule(LinkExtractor(allow="catalogue", deny="catagory"), callback="parse_item"),
    }

    def parse_item(self, response):
        yield {
            "title": response.css(".product_main h1::text").get(),
            "price": response.css(".price_color::text").get(),
            "avalibility": response.css(".availability::text")[1].get().replace("/n", "").replace(" ",""),
        }

    

# response
# response.css("h1")
# response.css("h3").get()
# response.css("h1::text").get()
# response.css("a::text").getall()
# response.css(".page-header").get()
# response.xpath("//a/text()").extract()

# scrapy crawl mycrawler -o output.json

