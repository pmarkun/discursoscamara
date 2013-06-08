#-*- coding:utf-8 -*
import re
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from scrapy.item import Item, Field

def clean(item):
    return ' '.join(item).strip()

class Discurso(Item):
    data = Field()
    sessao = Field()
    fase = Field()
    discurso = Field()
    sumario = Field()
    orador = Field()
    partido = Field()
    estado = Field()
    hora = Field()
    publicacao_data = Field()
    publicacao_colecao = Field()
    publicacao_pagina = Field()

class CamaraSpider(CrawlSpider):
    name = 'camara.gov.br'
    allowed_domains = ['camara.gov.br']
    start_urls = ["http://www.camara.gov.br/internet/sitaqweb/resultadoPesquisaDiscursos.asp?dtInicio=01%2F01%2F1974&dtFim=30%2F12%2F1984&basePesq=plenario&CampoOrdenacao=dtSessao&PageSize=249&TipoOrdenacao=DESC&btnPesq=Pesquisar"]
    rules = (
        Rule(SgmlLinkExtractor(allow=r'CurrentPage'), callback='parse_discurso', follow=True),
        )
    def parse_start_url(self, response):
        return self.parse_discurso(response)

    def parse_discurso(self, response):
        discursos = []
        x = HtmlXPathSelector(response)
        ds =  x.select("//table[@class='tabela-1 variasColunas']/tbody/tr[not(@style='display: none')]")
        for d in ds:
            discurso = Discurso()
            discurso['data'] = clean(d.select("./td")[0].select("./text()").extract())
            discurso['sessao'] = clean(d.select("./td")[1].select("./text()").extract())
            discurso['fase'] = clean(d.select("./td")[2].select("./text()").extract())
            discurso['discurso'] = ''
            discurso['sumario'] = clean(d.select("./following-sibling::tr[1]/td/text()").extract())
            orador = d.select("./td")[5].select("./text()").extract()
            discurso['partido'] = ''
            discurso['estado'] = ''
            discurso['orador'] = clean(orador)
            
            orad = re.search('(.*), (.*)-([A-z]*)', orador[0])
            if (orad):
                discurso['orador'] = orad.group(1).strip()
                discurso['partido'] = orad.group(2)
                discurso['estado'] = orad.group(3)

            discurso['hora'] = clean(d.select("./td")[6].select("./text()").extract())
            discurso["publicacao_colecao"] = ''
            discurso["publicacao_pagina"] = ''
            discurso["publicacao_data"] = ''

            if d.select("./td")[7].select("./a/@onclick"):
                pub = d.select("./td")[7].select("./a/@onclick").extract()[0].split("'")
                discurso["publicacao_colecao"] = pub[1]
                discurso["publicacao_pagina"] = pub[3]
                discurso["publicacao_data"] = pub[5]
            
            discursos.append(discurso)
        return discursos