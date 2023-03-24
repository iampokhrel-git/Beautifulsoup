import requests 
from bs4 import BeautifulSoup
url = "https://www.nrb.org.np"
r= requests.get(url)
htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,'html.parser')
navbarNav=soup.find(id='navbarNav')#navbarNav is taken from www.nrb.org.np 
print(navbarNav.next_sibling.next_sibling)
print(navbarNav.previous_sibling.previous_sibling)

element=soup.select('#searchform')     # we take searchform from source code
print(element)