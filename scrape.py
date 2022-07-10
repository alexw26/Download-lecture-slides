from bs4 import BeautifulSoup
import requests
from urllib.parse import unquote

#source = requests.get('https://faculty.math.illinois.edu/~icontrer/MATH415_Ivan_S18.html').text
#soup = BeautifulSoup(source, 'lxml')

with open('math/math415.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

substring_1 = "https://faculty.math.illinois.edu"
substring_2 = ".pdf"

for link in soup.find_all('a') : # finds all links using <a> tag
    url = link.get('href')
    # print(url)
    pdf = unquote(url)
    if (substring_1 in pdf and substring_2 in pdf):
        print(pdf)
        # next step is instead of printing pdf out, 
        # we need to download it onto our machine 
        # (use url variable instead of pdf variable 
        # since url is the actual url and pdf is a string representation of it)

        # also, include naming as well?

        # questions to ask Bhavya
        # 1. Naming of pdf files (since some lectures include multiple slides,
        # and there are also review pdfs, not just lecture pdfs)?
        # 2. Include non-lecture pdfs?

        # watch the video on how to download pdfs to local machine
    else:
        print("non-pdf file")
    print()

# print(link)

# print(soup.prettify())

# print (r.text) for hmtl files
# print(r.content) for images

# how to differentiate between pdf file links and other links?