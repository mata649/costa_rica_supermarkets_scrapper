
from scrapy import Spider


class PriceSmartSpider(Spider):
    name = 'pricesmart'
    start_urls = ['https://www.pricesmart.com/site/cr/es/categorias']



    def parse_product(self, response, **kwargs):
        product_name = response.xpath('//h1[contains(@class, "main-title")]/text()').get().replace('\n', ' ').strip()
        product_price = response.xpath(
            '//strong[contains(@class, "currency")]/text()').get().replace('\n', ' ').strip()

        yield {
            'name': product_name,
            'price': product_price,
            'category': kwargs['category'],
            'url': response.url
        }

    def parse_category(self, response):
        links_to_products = response.xpath(
            '//div[contains(@class, "search-product-box")]/a/@href').getall()
        category = response.url.split('/')[7].split('?')[0]
        for link in links_to_products:
            yield response.follow(link, callback=self.parse_product, cb_kwargs={'category': category})

        next_page_link = link = response.xpath(
            '//li[contains(@class, "page-item") and contains(@id, "next")]/a/@href').get()
        if next_page_link:
            yield response.follow(next_page_link, callback=self.parse_category)

    def parse(self, response):
        links_to_categories = response.xpath(
            '//a[contains(@class, "categories-section-link")]//@href').getall()

        for link in links_to_categories:
            yield response.follow(link, callback=self.parse_category)
