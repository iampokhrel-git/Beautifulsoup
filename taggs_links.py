import requests 
from bs4 import BeautifulSoup
url = "https://www.nrb.org.np"
r= requests.get(url)
htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,'html.parser')
anchors=soup.find_all('a')
all_links=set()

for link in anchors:
    if(link.get('href')!='a'):
        linkText="https://www.nrb.org.np" + link.get('href')
        all_links.add(link)
        print(linkText)
    