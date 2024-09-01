from typing import Any, Iterable
import scrapy
from scrapy.http import Response #primeira mente importar o scrapy

#criar uma classe e nomear ela usando sempre a primeira maiuicula de cada palavra. este jeito de nomear se chama CamelCase
class GoodReadsSpider(scrapy.Spider):  #colocar o nome da classe e entre parenteses colocou a a sipider para pode erdar os dados desta classe
    #indentidade da Spider
    name = 'desafioFrase'
    #request
    def start_requests(self):  ##iniciar a requisição
        urls = ['https://www.goodreads.com/quotes']  #informar os URLs a serem varridos
        # #laço de repetiçã para entar em cada site e retornar os dados conforme é executado retornaldo a os dados cada vez que passar e for encontrando os dados
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    #Response
    def parse(self,response):
        #aqui é  onde voce deve processar o qeu é retornado da response

    ##este trecho copia o html de uma pgina
        # with open('pagina.html', 'wb') as arquivo: #retornando o arquivo com os dados do html
        #     arquivo.write(response.body)  
        for elemento in response.xpath('//div[@class="quote"]'): ##encontra as 10 citaçoes que este site tem
            yield{
                'frase': elemento.xpath('.//div[@class="quoteText"]/text()').get(), # retorna a frase do primeio elemento enocntrado dentro da div da frase
                'autor': elemento.xpath('.//span[@class="authorOrTitle"]/text()').get(), #retorno o autor da frase acima selecionada
                'tags':elemento.xpath('.//div[@class="greyText smallText left"]/a/text()').getall()
                
            }

##colocando o ponto antes do xpath que são referentes ao primeiro, isso indita que ao voltar o laço de repetiação ele deve coltar somente na div espeficada no elemento pai.