from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pdp
from urllib.request import urlopen as uReq
from urllib.request import Request
from bs4 import BeautifulSoup as soup
import re

import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
def get_genre_first_page(genre_url):
    response = requests.get(genre_url, headers= headers)
    
    if not response.ok:
        print('Status Code:', response.status_code)
        raise Exception('Failed to fetch web page' + genre_url)
    
    doc = BeautifulSoup(response.text)
    return doc

doc1 = get_genre_first_page('https://www.imdb.com/chart/top')
movie_tags = doc1.find_all('div', class_ = 'sc-b189961a-0 hBZnfJ cli-children')
rating = doc1.find_all('span', class_= 'ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating')

def mov_name_year_duration(cinema):
    # pattern1 = r'\d+\.\s*([A-Za-z\s]+)\d+'
    # pattern_new = r'\d+\.\s([0-9A-Za-z\s]+)\d+'
    # match1 = re.search(pattern1,cinema.text)
    # match2 = re.search(pattern_new, cinema.text)
    # 
    soup = BeautifulSoup(str(cinema), 'html.parser')
    tags = soup.find_all('h3')
    tags2 =soup.find_all('span', class_= "sc-b189961a-8 kLaxqf cli-title-metadata-item")
    return tags[0].text , tags2[0].text, tags2[1].text
pattern2 = r'(\d\.\d)'
filename= "imdb_m.csv"

f = open(filename, "w")

headers= "Name, Year, Duration, Rating \n"
f.write(headers)

for movie in movie_tags:
    name,year,duration= mov_name_year_duration(movie)
    # year= mov_year(movie)
    rating= re.findall(pattern2, movie.text)[0]
    
    print(name + "," + year + "," + duration + "," + rating +  "\n")
    f.write(name + "," + year + "," + duration + "," + rating +  "\n")
    
f.close()

