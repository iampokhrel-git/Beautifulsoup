import requests 
from bs4 import BeautifulSoup
url = "https://www.nrb.org.np"
r= requests.get(url)
htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,'html.parser')
print(soup)