import urllib3
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl(pagina):
	urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
	http = urllib3.PoolManager()

	try:
		dados_pagina = http.request('GET', pagina)
	except:
		print('Erro ao abrir página' + pagina)

	sopa = BeautifulSoup(dados_pagina.data, 'lxml')
	num_visualizacoes = sopa.find("div", class_="watch-view-count").string
	nome = sopa.find_all("ytd-channel-name", class_="style-scope")
	print(num_visualizacoes)
	print(nome)
	links = sopa.find_all('a')
	contador = 1
	print(sopa.title.string)
	for link in links:
		if ("href" in link.attrs):
			url = urljoin(pagina, str(link.get('href')))
			if "/watch?" in url:
				print(url)
				contador = contador + 1
	print(contador)

crawl('https://www.youtube.com/watch?v=VzkBv1-Y-TE')