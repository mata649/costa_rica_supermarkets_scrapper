from scrapy import Spider


class PequenoMundoSpider(Spider):
    name = 'pequeno_mundo'
    start_urls = ['https://tienda.pequenomundo.com/']

    def parse_product(self, response, **kwargs):
        product_name = response.xpath(
            '//h1[contains(@class, "page-title")]/span/text()').get()
        product_price = response.xpath(
            '//span[contains(@class, "price-wrapper")]/@data-price-amount').get()

        yield {
            'name': product_name,
            'price': product_price,
            'category': kwargs['category'],
            'url': response.url
        }

    def parse_category(self, response):
        links_to_products = response.xpath(
            '//div[contains(@class, "product-item-photo")]/a/@href').getall()
        category = response.url.split('/')[3]
        for link in links_to_products:
            yield response.follow(link, callback=self.parse_product, cb_kwargs={'category': category})

    def parse(self, response):
        links_to_categories = response.xpath(
            '//li[contains(@class, "ui-menu-item level1")]/a/@href').getall()

        for link in links_to_categories:
            yield response.follow(link, callback=self.parse_category)
