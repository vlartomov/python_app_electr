import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
url = "https://www.kinopoisk.ru/lists/movies/top250/"
r = requests.get(url)
r.text

soup = BeautifulSoup(r.text, 'html.parser')

link = "https://www.kinopoisk.ru"+soup.find('div',{'class':'styles_root__ti07r'}).find('a',{'class':'base-movie-main-info_link__YwtP1'}).get('href')
russian_name = soup.find('div', class_='styles_root__ti07r').find('a', class_='base-movie-main-info_link__YwtP1').find('span', class_='styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj').text
engl_name = soup.find('div', class_='styles_root__ti07r').find('a', class_='base-movie-main-info_link__YwtP1').find('span', class_='desktop-list-main-info_secondaryText__M_aus').text
country = soup.find('div', class_='styles_root__ti07r').find('a', class_='base-movie-main-info_link__YwtP1').find('span', class_='desktop-list-main-info_truncatedText__IMQRP').text
raiting = soup.find('span', class_='styles_kinopoiskValuePositive__vOb2E styles_kinopoiskValue__9qXjg').text

data = []

for p in range(1, 6):
    print(p)
    
    url = f"https://www.kinopoisk.ru/lists/movies/top250/?page={p}"
    r = requests.get(url)
    time.sleep(5)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    films = soup.findAll('div', class_='styles_root__ti07r')
    
    for film in films:
        try:
            link = "https://www.kinopoisk.ru"+film.find('a', class_='base-movie-main-info_link__YwtP1').get('href')
        except:
            link = '-'
        try:
            russian_name = film.find('a', class_='base-movie-main-info_link__YwtP1').find('span', class_='styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj').text
        except:
            russian_name = '-'
        try:
            engl_name = film.find('a', class_='base-movie-main-info_link__YwtP1').find('span', class_='desktop-list-main-info_secondaryText__M_aus').text
        except:
            engl_name = '-'
        try:
            country = film.find('a', class_='base-movie-main-info_link__YwtP1').find('span', class_='desktop-list-main-info_truncatedText__IMQRP').text
        except:
            country = '-'
        try:
            raiting = soup.find('span', class_='styles_kinopoiskValuePositive__vOb2E styles_kinopoiskValue__9qXjg').text
        except:
            raiting = '-'
        
        data.append([link, russian_name, engl_name, country, raiting])
        

header = ['link', 'russian_name', 'engl_name', 'country', 'raiting']
df = pd.DataFrame(data, columns=header)
df.to_csv('/Users/neo/Desktop/test/kinopoisk2.csv', sep=';', encoding='utf8')