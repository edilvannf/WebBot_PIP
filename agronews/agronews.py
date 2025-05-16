import requests
from bs4 import BeautifulSoup

#GloboRural
pagina_globorural = requests.get('https://globorural.globo.com/ultimas-noticias/')
dados_globo = BeautifulSoup(pagina_globorural.text, 'html.parser')
noticias_globorural = dados_globo.find_all('div', class_='feed-post-body')

#CanalRural
pagina_canalrural = requests.get('https://www.canalrural.com.br/ultimas-noticias/')
dados_canal = BeautifulSoup(pagina_canalrural.text, 'html.parser')
noticias_canalrural = dados_canal.find_all('a', class_='feed-link hover gap-0')


mensagem1 = '📰 *Últimas notícias do Globo Rural:*\n\n'
mensagem2 = '📰 *Últimas notícias do Canal Rural:*\n\n'
mensagem3 = '📰 *Últimas notícias do Globo Rural:*\n\n'

print(f'{mensagem1.upper()}')

#Percorre todas as notícias do site GloboRural e exibe o título e o link
for div in noticias_globorural:
    h2 = div.find('h2', class_='feed-post-link gui-color-primary gui-color-hover')
    if h2:
        link_noticia = h2.find('a')
        if link_noticia:
            texto = link_noticia.text.strip()
            link = link_noticia['href']
            print(f'👉 *{texto}*\n🔗 {link}\n\n')
#oi edilvan

print(f'{mensagem2.upper()}')

#Percorre todas as notícias do site CanalRural e exibe o título e o link
for a in noticias_canalrural[:10]:  # Limitado a 10 notícias, pois no site do CanalRural são muitas notícias.
    h2 = a.find('h2')
    if h2:
        texto = h2.text.strip()
        link = a['href']
        print(f'👉 *{texto}*\n🔗 {link}\n')


