
import requests
from bs4 import BeautifulSoup

#! Send a HTTP Request

url = 'https://editorial.rottentomatoes.com/article/the-10-scariest-horror-movies-ever/'
response = requests.get(url)

#! Parse the Content with Beutiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

#! Find Elements using  tags and attributes
title = soup.title.text
print("Title : ", title)

all_links = soup.find_all('h2')
for link in all_links:
    print("Link : ", all_links)
