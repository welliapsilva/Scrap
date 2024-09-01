from typing import Any, Iterable
import scrapy
from scrapy.http import Response #primeira mente importar o scrapy

#criar uma classe e nomear ela usando sempre a primeira maiuicula de cada palavra. este jeito de nomear se chama CamelCase
class QuotesToScrapeSpider(scrapy.Spider):  #colocar o nome da classe e entre parenteses colocou a a sipider para pode erdar os dados desta classe
    #indentidade da Spider
    name = 'frasebot'
    #request
    def start_requests(self):  ##iniciar a requisição
        urls = ['https://quotes.toscrape.com/']  #informar os URLs a serem varridos
        # #laço de repetiçã para entar em cada site e retornar os dados conforme é executado retornaldo a os dados cada vez que passar e for encontrando os dados
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    #Response
    def parse(self,response):
        #aqui é  onde voce deve processar o qeu é retornado da response
        with open('pagina.html', 'wb') as arquivo: #retornando o arquivo com os dados do html
            arquivo.write(response.body)