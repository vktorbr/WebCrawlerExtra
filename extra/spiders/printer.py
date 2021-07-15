import scrapy
import json
from extra.items import ExtraItem

class ExSpider(scrapy.Spider):
    name = 'printer'
    start_urls = ['https://www.extra.com.br/c/informatica/impressoras/?filtro=c56_c61&faixapreco=200to53413']

    headers = {
        ":authority": "www.extra.com.br",
        ":method": "GET",
        ":path": "/api/catalogo-ssr/products/?Filtro=c56_c61&FiltroFaixaPreco=200to53413&PaginaAtual=2&RegistrosPorPagina=20&Platform=1",
        ":scheme": "https",
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
        "cache-control": "no-cache",
        "cookie": "IPI-Extra.com=UsuarioGUID=97536e32-1cb5-429d-a007-977155edd453; chaordic_browserId=0-FdVtapBxHHEGbG2vwAnGup2azivCznn8kW5d16150659060887276; chaordic_anonymousUserId=anon-0-FdVtapBxHHEGbG2vwAnGup2azivCznn8kW5d16150659060887276; ISS-SEARCH=ABtest=B&ABver=CHAORDIC_100; lx_sales_channel=%5B%22desktop%22%5D; chaordic_testGroup=%7B%22experiment%22%3A%22EXTRA_NEW_RANK_HOTSITE_2019-11-25%22%2C%22group%22%3A%22C%22%2C%22testCode%22%3A%22EXTRA_NEW_RANK_HOTSITE_2019-11-25_C%22%2C%22code%22%3A%22EXTRA_NEW_RANK_HOTSITE_2019-11-25_C%2Fw7UfC6VhczkiVhCBkuSvhVYAdHiBTU5w%22%2C%22session%22%3A%22w7UfC6VhczkiVhCBkuSvhVYAdHiBTU5w%22%7D; ISS-Extra.com=TesteAB=B; ISS-BUSCA=ABtest=A&ABver=50PORCENTO; AKA_A2=A; bm_sz=8D376BB2ABB2A45E30DC20067BBD9231~YAAQZaQSAnXa3ht6AQAAP/RwoAz+n0taYperFuD970zY7KBsspa18QUpVstAmxr6fDk/0kr1XW8HHR5F6w+AQWsBA7MKdlYh8l48s2JzsK7M5/hf9VRADBEP1ajtcFE2W+8TqlA9YDlY9zc1d0DyNvZCY2rmP7EVmpR2t2nJxv+WjEoVSFV1o/9HN7V4tf0nr80=; _abck=1B8FB352BC556096AB64DE2BD22FAEB5~0~YAAQZaQSAnba3ht6AQAAP/RwoAZ5uhWs7nbyoQijqYRPZQIu5dszLoPi+79y0gaiZWONS8ajlsPD4hGg6viaMMy++BObfq0LhCT/xv+1gSeSGI2MISeE0wKNDgl/u68VxWFzw5tQMqTYcM/J6re0Zfikm+t8CY9eH3F+HRBKwlGem5YL3+LrD+UZLL2xlEQmMKcFKQwFcnMpW5fbCz4M4I+IQgqSWUY/wmwC56nmwRDzszP7r50hnofA+z/P5rZkwmYLyiNJdTTd3VOo/s1+7MDzNOlVBshwm/yhC3UDDOuWWEcbHVvbC0xKUbtHOxZ6JDQ6CuQrAikm2PETQ+/annDDoZIf20k77E366NijkzoJsY/6PdLDMsPTuMK9g/VWbJqb5MBS6NlyQLP5PBoGNEkoIC6hIYU6hJg=~-1~-1~-1; ak_bmsc=CF1C0678CC606B639389554463D0DD44~000000000000000000000000000000~YAAQZaQSAnfa3ht6AQAAP/RwoAzyABfcIzKe5r1wNvdh3A0upqIKMyxLcLCnnF3zHDSD1ZirvFE6Gb3A20F4IBQ9wCdiozdrcJElJ7BYottO+CEIjL//Ey+zCCtpnQcR7FlmdzU4PkvxFeEEodIesDINrYA3BiFd6pnAbyMGTt7RtLbw1KYJoR3ZQHomS/SbUMlhzcKk2GSC8QzjFQ+OJuQwT+tfLpzBPmzdjrd8YbTQJ4S5KRsMlrGz9+Rv4bPdVot++VkqQqIR8ZxCx40qCGhUKzgev3Zg8O+nE/nfUdCDRcHe/tfXIc/p+FKZ03Eq2Vh5W4I1lvDbvvAe7W0a4b3FU9BjYwt0cADHpu55aykpD0ym0aYG/S1FEN1UcGCQ6U2kKSu+ZmYutPpw; bm_mi=EB6E25052A5686EE4DFFA370D22B6DDF~SvaTyqMpCTE1OZikpWYuSseTsNm5iZREha5N5dlsjrowlqEjVyXL0AEbOKIScpp+/GrKYI4TW3Ufvn4Y8FLng0jsxKILGIN6h+R9Zkcp/8fTSD+j4kFxhLndfggAwFBN4lXvb8cpQKcHuiOElUFDMWx57mk4582Eo5HC1UAstbhsU+So/FFrTGVeovj7l+RR9NqQu69mUy1B2raEAJQI/lJoHf2FTyCxrhADIyZc17YHfYYz1jGA8KA9RL6TQs/UNI3Roey++Iurq8zCtDGy7w==; bm_sv=69C343A08BC4E1414EAF58B90E6C4017~cTYSlckmCp+ikbR0uF3nQx+6zi9X2uQw98boP5djo5W2kSCioUZlIo5v8lve7elWXQxiJieRtFvb/k+xnqhlPiPoIy8QKXx9APh+pZ3Q4Fk0/n1t2zpii97a8UOYTDyyWnKKv1Z0cw7A7l9bpDGIZ2KsPdfrCiicAR5UMVklQBc=",
        "pragma": "no-cache",
        "referer": "https://www.extra.com.br/c/informatica/impressoras/?filtro=c56_c61&faixapreco=200to53413",
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
            url = 'https://www.extra.com.br/api/catalogo-ssr/products/?Filtro=c56_c61&FiltroFaixaPreco=200to53413&PaginaAtual=%d&RegistrosPorPagina=20&Platform=1' % (i)
            
            #para toda página chamo a callback parse_api para extrair as urls dos produtos
            yield response.follow(url, callback=self.parse_api, headers=self.headers)
   
    #da lista de produtos obtem-se as urls da página do produto
    def parse_api(self, response):
        raw_data = response.body
        data = json.loads(raw_data)
        for product in data["products"]:
            printer_url = product["urls"]

            yield response.follow(printer_url, callback=self.parse_printer, headers=self.headers)

    #pega as informações da página do produto
    def parse_printer(self, response):
        sku = response.css('p.css-kbw5o0 span:first-child::text').getall()[1]
        title = response.css('h1.css-rfo7gs::text').get()
        printer = ExtraItem(sku=sku, title=title, url=response.url)

        yield printer
