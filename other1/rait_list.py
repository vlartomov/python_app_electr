from cgitb import text
import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://www.kinopoisk.ru/lists/movies/top250/"
r = requests.get(url)
r.text

soup = BeautifulSoup(r.text, 'html.parser')

ementa = getattr(soup.find('span', class_='styles_kinopoiskValuePositive__vOb2E styles_kinopoiskValue__9qXjg'), 'text', None)
print(ementa)

#raiting
#data = []
#data.append([raiting])
#header = ['raiting']
#df = pd.DataFrame(data, columns=header)
#df.to_csv('/Users/neo/Desktop/test/kinopoisk3.csv', sep=';', encoding='utf8')