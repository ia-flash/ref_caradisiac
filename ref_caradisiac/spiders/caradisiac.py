import scrapy
import re

class RefModeleSpider(scrapy.Spider):
    name = 'modeles'


    def start_requests(self):

        marque = getattr(self, 'marque', None)
        marque_url = getattr(self, 'marque_url', None)

        if marque is not None:
            url = 'https://www.caradisiac.com/auto--%s/modeles' % marque

        if marque_url is not None:
            url = 'https://www.caradisiac.com%smodeles' % marque_url
            marque = setattr(self,'marque',re.search('(?<=\/auto--)(.*)(?=\/)', marque_url).group(1))

        yield scrapy.Request(url, self.parse)


    def parse(self, response):
        for ref in  response.css('div.visuModeleGalerie.col-xs-2.col-sm-4.col-md-5 a'):
            yield {
                'src':  ref.css('img').xpath('@src').get(),
                'alt': ref.css('img').xpath('@alt').get(),
                'href': 'https://www.caradisiac.com' + ref.xpath('@href').get(),
                'marque' : self.marque,
            }


class RefMarqueSpider(scrapy.Spider):
    name = 'marques'


    def start_requests(self):
        url = 'https://www.caradisiac.com/constructeurs--automobiles/'

        yield scrapy.Request(url, self.parse)


    def parse(self, response):
        for ref in  response.css('a.hidden-xs'):
            yield {
                'src':  ref.css('img').xpath('@src').get(),
                'href': ref.xpath('@href').get(),
                'marque' : ref.xpath('@title').get(),
            }
