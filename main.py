import requests

re = requests.get('https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html')
res = re.content
