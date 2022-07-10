from bs4 import BeautifulSoup
import requests
from urllib.parse import unquote

source = requests.get('https://faculty.math.illinois.edu/~icontrer/MATH415_Ivan_S18.html').text
soup = BeautifulSoup(source, 'lxml')

#with open('math/math415.html') as html_file:
#    soup = BeautifulSoup(html_file, 'lxml')

for link in soup.find_all('a') : # finds all links using <a> tag
    url = link.get('href')
    #print(url)
    print(unquote(url))
    print()

#print(link)

#print(soup.prettify())

# print (r.text) for hmtl files
# print(r.content) for images

# how to differentiate between pdf file links and other links?