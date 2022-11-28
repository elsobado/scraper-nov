import requests
from bs4 import BeautifulSoup

re = requests.get('https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html')
res = re.content

soup = BeautifulSoup(res,'html.parser')
price = soup.find()'p'mp,bredeclase acac ,