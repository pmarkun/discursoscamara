# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

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
    publicaca_colecao = Field()
    publicacao_pagina = Field()