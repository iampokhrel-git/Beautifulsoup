import requests 
from bs4 import BeautifulSoup
url = "https://www.nrb.org.np"
r= requests.get(url)
htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,'html.parser')
navbarNav=soup.find(id='navbarNav')#navbarNav is taken from www.nrb.org.np 
print(navbarNav)
print(navbarNav.children)
print(navbarNav.contents)

for item in navbarNav.strings:
    print(item)
    
    for items in navbarNav.stripped_strings:
        print(items)
        
print(navbarNav.parents)

for item in navbarNav.parents:
    print(item.name)