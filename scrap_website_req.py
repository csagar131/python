import requests

from bs4 import BeautifulSoup

page  = requests.get('http://books.toscrape.com')

print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')

tag = soup.select_one('body.default ul li a').string    # prints HOME from the site inside the unordered list
print(tag)