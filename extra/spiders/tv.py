import scrapy
import json
from extra.items import ExtraItem

class TvSpider(scrapy.Spider):
    name = 'tv'
    start_urls = ['https://www.extra.com.br/c/tv-e-video/televisores/?filtro=c1_c2&faixapreco=1000to90999']

    headers = {
        ":authority": "www.extra.com.br",
        ":method": "GET",
        ":path": "/api/catalogo-ssr/products/?Filtro=c1_c2&FiltroFaixaPreco=1000to90999&PaginaAtual=2&RegistrosPorPagina=20&Platform=1",
        ":scheme": "https",
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
        "cache-control": "no-cache",
        "cookie": "IPI-Extra.com=UsuarioGUID=97536e32-1cb5-429d-a007-977155edd453; chaordic_browserId=0-FdVtapBxHHEGbG2vwAnGup2azivCznn8kW5d16150659060887276; chaordic_anonymousUserId=anon-0-FdVtapBxHHEGbG2vwAnGup2azivCznn8kW5d16150659060887276; ISS-SEARCH=ABtest=B&ABver=CHAORDIC_100; lx_sales_channel=%5B%22desktop%22%5D; chaordic_testGroup=%7B%22experiment%22%3A%22EXTRA_NEW_RANK_HOTSITE_2019-11-25%22%2C%22group%22%3A%22C%22%2C%22testCode%22%3A%22EXTRA_NEW_RANK_HOTSITE_2019-11-25_C%22%2C%22code%22%3A%22EXTRA_NEW_RANK_HOTSITE_2019-11-25_C%2Fw7UfC6VhczkiVhCBkuSvhVYAdHiBTU5w%22%2C%22session%22%3A%22w7UfC6VhczkiVhCBkuSvhVYAdHiBTU5w%22%7D; ISS-Extra.com=TesteAB=B; ISS-BUSCA=ABtest=B&ABver=50PORCENTO; _abck=1B8FB352BC556096AB64DE2BD22FAEB5~0~YAAQfqQSAsL+Kp16AQAAwdxcoQaur/H8zO2LjAmM5OsmGLV+8KjxaGUTj7rODzuhBJW92qtpSED4KT8Z+x7hQMbcRcPn9A8PHzkrYs8bhBLgelrNmiHI8HHEqsVA8rOOFaD2o2e42YpgJpaYxHPsX+K/rM9TMQF0rHExC1XGN9pfD7oguwiaN8Qjcjpiku7nUnSY6s4ctQEJXfGgRFEng9bl5lY5j6GtbFriq7tV+5SENBHHaOS+2ZE1xvTe4jjPjG/f+2la8151fOqTFg3GTK2hPghAqBKLoZ+qhQd2hRH8jQL2k2n30XKgIfsYCY4whLfQrwWCEpeiGT3vB1W+wnF9PFsfJnErA+qMDE+9b8EpgaEAZ+xTUZPHk1Iv6Aec4bVwcPZP6/iYzoZQ3E4oBycJxYsPvPGgsHA=~-1~-1~-1; bm_sz=14B7989DDDD424D0C42E88F86F301EBA~YAAQfqQSAsP+Kp16AQAAwdxcoQxItG+SDM8PWAKR8JUL6bHnxTmuldR1S5C/Id06a2KMMeJYE8J+0Zx/H2QgdwXxBATFZWVqE52DLde2X1ky7KASKuHv4eeXO0Isiqbzz7ycAdooypTRpp6EIReuJkerp1foVKXw84mPvApOCx4kjkQpl9yzP+f5zXyBny/fYGeNOwR5VimsI/KoJiyBnPhW0CrxPgE4L1nZuOc+Ct7RKGADv14LI/EM09LXtMNHhS7YYJw0xh1Wj4//F2xrMDrb1aCxkA77wlWqBAx3O0e98QlRQg==~3490359~4405555; AKA_A2=A; bm_mi=44F60F268167EDB4441044D920050435~EzzYjDZPkPNS+NvknzTZOIhLJ9TxiAvW2xD4v9i5gtgCp1l2rD9sUCTuxjtXnPr1izFRWhYyZgTb3GQoST+W0c9ZGWC385+RTmdQkYtQfMMOmkdMnV5wVJTtdkhVXl+QRmQGatisyzEhn2x6iQh1RPOgPMMjVVkBthSEHf+uwYUNOeYhJx3DmSGKIYmupnXta++DbHo5witQQsHwN8ZqVzwI7AhezXqlpWCqUBQ+5RTVpKn9+7EDGIYAzcnhU0Q6tEDoW9RD0YIK78wvfzj7Xg==; bm_sv=56C832A6A1941C775BA61A76E05870B6~cUsov49Y9ZWD0OUuQNIl3woIcqBzEI0gaXV4M/2bI4/+3XRkXh8ivk7Jc0IC/d5E/QiCv7qKfnOgmcYxVylSlE/7JnvaEpmI/yXffp14bSoq2wEbXl2di2J3El1TBoMVdG9MESKgwurtO2HagdsteQScxBrFvesFsuGdnCdGdTE=; ak_bmsc=1D062030D0248CB30A95C382B98F5782~000000000000000000000000000000~YAAQfqQSApMLK516AQAAikRgoQx5hKpvpAd2kfkUvan5oIWO1OhZT6hYpY50JMbxrJXKT8AQ4C962Kc8pzraoWOSqdHtNjotMHlY0fayZbFC+GUTuNuls4hhnpvJduNtXt3OOEYAWTQ99C9wkQ6oT8X+rpNUGjPjlFesguUfDc1ToBdb4TckebC2xSvbSWSDImfhzYZhHU3uCEpERk2+aZCHBZmQD44w5rSGrg/uT7NGLkHXr/Yz09RAKFmV4CCtFArJn5lpR37Ffaq1I5Z0lEF3tzlvlFBfWJi3NwewyHM1pJ4u0hGgqfJWUvC2gNqCDTOY59SpOd7xjExI2KHz4ZB4tG8CidbZtcPpbgspUDGQ5kL+B3iWPKarxpL5QlxzMe4ghvx/A3LYtxd/30uIS6OzfwQW/5gXD4EY3wBhGYGyZEBkF/6tFDvuiQFB4Dy0Yz9NnE6xvj5/Bw==",
        "pragma": "no-cache",
        "referer": "https://www.extra.com.br/c/tv-e-video/televisores/?filtro=c1_c2&faixapreco=1000to90999",
        "sec-ch-ua": '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67"
    }

    def parse(self, response):
        #percorre 99 páginas primeiras páginas
        for i in range(1, 90):
            #os dados são enviados dinamicamente pela api do extra
            url = 'https://www.extra.com.br/api/catalogo-ssr/products/?Filtro=c1_c2&FiltroFaixaPreco=1000to90999&PaginaAtual=%d&RegistrosPorPagina=20&Platform=1' % (i)

            #para toda página chamo a callback parse_api para extrair as urls dos produtos
            yield response.follow(url, callback=self.parse_api, headers=self.headers)
    
    #da lista de produtos obtem-se as urls da página do produto
    def parse_api(self, response):
        raw_data = response.body
        data = json.loads(raw_data)
        
        for tv in data["products"]:
            tv_url = tv["urls"]

            yield response.follow(tv_url, callback=self.parse_tv, headers=self.headers)
    
    #pega as informações da página do produto
    def parse_tv(self, response):
        sku = response.css('p.css-kbw5o0 span:first-child::text').getall()[1]
        title = response.css('h1.css-rfo7gs::text').get()
        tv = ExtraItem(sku=sku, title=title, url=response.url)

        yield tv