import requests
from bs4 import BeautifulSoup

pagina = requests.get('https://globorural.globo.com/ultimas-noticias/')
dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

noticias = dados_pagina.find_all('div', class_='feed-post-body')

mensagem = '📰 *Últimas notícias do Globo Rural:*\n\n'

print(f'{mensagem.upper()}')

for div in noticias:
    h2 = div.find('h2', class_='feed-post-link gui-color-primary gui-color-hover')
    if h2:
        link_noticia = h2.find('a')
        if link_noticia:
            texto = link_noticia.text.strip()
            link = link_noticia['href']
            print(f'👉 *{texto}*\n🔗 {link}\n\n')
#oi edilvan
