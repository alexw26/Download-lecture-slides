from bs4 import BeautifulSoup
import requests

r = requests.get('https://faculty.math.illinois.edu/~icontrer/MATH415_Ivan_S18.html')

with open('math/math415.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

match = soup.href
print(match)

# print(soup.prettify())

# print (r.text) for hmtl files
# print(r.content) for images