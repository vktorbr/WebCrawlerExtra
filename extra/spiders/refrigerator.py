from extra.items import ExtraItem
import json
import scrapy


class RefrigeratorSpider(scrapy.Spider):
    name = 'refrigerator'
    start_urls = ['https://www.extra.com.br/c/eletrodomesticos/refrigeradores/?filtro=c13_c14&faixapreco=600to26999']


    headers = {
        ":authority": "www.extra.com.br",
        ":method": "GET",
        ":path": "/api/catalogo-ssr/products/?Filtro=c13_c14&FiltroFaixaPreco=600to26999&PaginaAtual=2&RegistrosPorPagina=20&Platform=1",
        ":scheme": "https",
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
        "cache-control": "no-cache",
        "cookie": "IPI-Extra.com=UsuarioGUID=97536e32-1cb5-429d-a007-977155edd453; chaordic_browserId=0-FdVtapBxHHEGbG2vwAnGup2azivCznn8kW5d16150659060887276; chaordic_anonymousUserId=anon-0-FdVtapBxHHEGbG2vwAnGup2azivCznn8kW5d16150659060887276; ISS-SEARCH=ABtest=B&ABver=CHAORDIC_100; lx_sales_channel=%5B%22desktop%22%5D; chaordic_testGroup=%7B%22experiment%22%3A%22EXTRA_NEW_RANK_HOTSITE_2019-11-25%22%2C%22group%22%3A%22C%22%2C%22testCode%22%3A%22EXTRA_NEW_RANK_HOTSITE_2019-11-25_C%22%2C%22code%22%3A%22EXTRA_NEW_RANK_HOTSITE_2019-11-25_C%2Fw7UfC6VhczkiVhCBkuSvhVYAdHiBTU5w%22%2C%22session%22%3A%22w7UfC6VhczkiVhCBkuSvhVYAdHiBTU5w%22%7D; ISS-Extra.com=TesteAB=B; bm_sz=8D376BB2ABB2A45E30DC20067BBD9231~YAAQZaQSAnXa3ht6AQAAP/RwoAz+n0taYperFuD970zY7KBsspa18QUpVstAmxr6fDk/0kr1XW8HHR5F6w+AQWsBA7MKdlYh8l48s2JzsK7M5/hf9VRADBEP1ajtcFE2W+8TqlA9YDlY9zc1d0DyNvZCY2rmP7EVmpR2t2nJxv+WjEoVSFV1o/9HN7V4tf0nr80=; _abck=1B8FB352BC556096AB64DE2BD22FAEB5~0~YAAQZaQSAnba3ht6AQAAP/RwoAZ5uhWs7nbyoQijqYRPZQIu5dszLoPi+79y0gaiZWONS8ajlsPD4hGg6viaMMy++BObfq0LhCT/xv+1gSeSGI2MISeE0wKNDgl/u68VxWFzw5tQMqTYcM/J6re0Zfikm+t8CY9eH3F+HRBKwlGem5YL3+LrD+UZLL2xlEQmMKcFKQwFcnMpW5fbCz4M4I+IQgqSWUY/wmwC56nmwRDzszP7r50hnofA+z/P5rZkwmYLyiNJdTTd3VOo/s1+7MDzNOlVBshwm/yhC3UDDOuWWEcbHVvbC0xKUbtHOxZ6JDQ6CuQrAikm2PETQ+/annDDoZIf20k77E366NijkzoJsY/6PdLDMsPTuMK9g/VWbJqb5MBS6NlyQLP5PBoGNEkoIC6hIYU6hJg=~-1~-1~-1; initialReferrer=; bm_mi=C05AD8D871EB9526ADFC5352BC2AF20D~5XlAzBOgPYGdgsizhSN160acZJpskUkUk6BpgveMQI3OuOjd1Sdq9xpt8A8Pp/hzrJB3FgLLH7fX0cYCFbO5h7t1jXu9dWcU3F2XwbwVYIIkL3dfCptjS5zmRZzj0PCsEZPy4tZhMEXsB6kfbikL7Wdk5RK5SMmqy62QrkWJ82qPc6odic7eNZvXIoW7Nb0Sm6JB5FdD6c1ptNMcCm6EzL2ZHKsMei7a5t5AhJHO6h5RIlvG/a+W4pka0MfHgVBQt1S4gm5iqtJSe+8uae6LsnYDDCLGLNJT6ID59LcQoQc=; bm_sv=1DD18E335E58AC10C8B542EABBE674FB~j8g7YQjeff3CAP3lJ+qNy4vPT0dFD7aTLi9Dr5nL4gN6IPvSlVqXQ4lB6CilfYjs5u2WPzdOyuQ0HtgUWVYWqoi9EpJFOLneQ6Rj0MimabmZItgTLiwt32QJ/uYpbdVPY2Ues6CQbQ622BFIz3LKDbz6m2qrY1i4bORaYkn+kNc=; ak_bmsc=305AFFB45C0938E73AA8C04A3FE6F2A9~000000000000000000000000000000~YAAQvqQSAsE0qpx6AQAAqWMeoQwaFdp4HlOqnqQwDFn6fxahUgi3agVyRxF/IkFGs18goVtGx9JNeJUvHeBwvqBoLDIR9Sd7kP/5h6tzaiFYYHKEvZvPdEIhbUq13kOzmlET8xDwwGKkWYxAc5VugysxtMIVPlHQONzuRCP7e6N8gBDTzS5ZiBym27tkfbl27fmu8c/J+ZuD8cDBgnDgv8/4fFA/an9f3Ta2VpqDTRppbNMcNAUJG/gvKl/7A5bbTKLta6C5OARRftLcqHuSXhHSq0leG5K8kGJwsBSzAEQPGr00JCNeushaZippBCsySg3yQ1xtH1HZ+An0HvBoZ3Zqpu1NAEJPlT1R/mxnFP0KeW+3NI92+hTp2zRaYekUG06xqA5mTcu4TA4AKcU1jB1Jo0PP8TJ0oiM6n8mEwRvpUnUfIiOF9aWOR/lEI95PRnqkIFeAOTnPN4c1qFXRcMdIwY+NjJtQcBUGVbxOdTroRgZnVD7gKQ3M; AKA_A2=A; ISS-BUSCA=ABtest=B&ABver=50PORCENTO; chaordic_session=1626201426060-0.9621934378029955",
        "pragma": "no-cache",
        "referer": "https://www.extra.com.br/c/eletrodomesticos/refrigeradores/?filtro=c13_c14&faixapreco=600to26999",
        "sec-ch-ua": '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67",
    }

    def parse(self, response):
        #percorre 80 páginas primeiras páginas
        for i in range(1, 81):
            #os dados são enviados dinamicamente pela api do extra
            url = 'https://www.extra.com.br/api/catalogo-ssr/products/?Filtro=c13_c14&FiltroFaixaPreco=600to26999&PaginaAtual=%d&RegistrosPorPagina=20&Platform=1' % (i)
            
            #para toda página chamo a callback parse_api para extrair as urls dos produtos
            yield response.follow(url, callback=self.parse_api, headers=self.headers)

    #da lista de produtos obtem-se as urls da página do produto
    def parse_api(self, response):
        raw_data = response.body
        data = json.loads(raw_data)
        
        for refrigerator in data["products"]:
            refrigerator_url = refrigerator["urls"]

            yield response.follow(refrigerator_url, callback=self.parse_refrigerator, headers=self.headers)

    #pega as informações da página do produto
    def parse_refrigerator(self, response):
        sku = response.css('p.css-kbw5o0 span:first-child::text').getall()[1]
        title = response.css('h1.css-rfo7gs::text').get()
        refrigerator = ExtraItem(sku=sku, title=title, url=response.url)

        yield refrigerator