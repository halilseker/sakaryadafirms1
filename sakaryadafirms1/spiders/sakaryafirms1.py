# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Sakaryafirms1Spider(CrawlSpider):
    name = 'sakaryafirms1'
    allowed_domains = ['sakaryada.com']
    start_urls = ['http://sakaryada.com/']

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        # First Rule collect firmlink from first page and both of Rules run itteratively until and of the Rule
        # Second Rule visits links and follow them, after following It calls parse_item method
        Rule(LinkExtractor(restrict_xpaths="//div[@class='block']/ul/li/a"), follow=True),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='firma-liste-baslik']/a"), callback='parse_item')
    )
    # This method collect infos from web pages
    def parse_item(self, response):
        # item = {}
        # #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # #item['name'] = response.xpath('//div[@id="name"]').get()
        # #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item

        yield {
            'firm_title': response.xpath("//div[@class='firma-detay-baslik']/text()").get(),
            'firm_address': response.xpath("//div[@class='firma-detayi']/ul/li[2]/text()").get(),
            'firm_phone_number': response.xpath("//div[@class='firma-detayi']/ul/li[5]/text()").get(),
            'firm_mobile_number': response.xpath("//div[@class='firma-detayi']/ul/li[11]/text()").get()
            # Other infos doesn't regular so I didn't add on it here
        }

        # 'firm_title': ftitles[i],
        # 'firm_representative': frepresentatives[i],
        # 'firm_phone_number': fphonenumber[i],
        # 'firm_email': femail[i],
        # 'firm_address': faddress[i],
        # 'firm_services': fservices[i]