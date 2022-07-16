from bs4 import BeautifulSoup
import requests
from urllib.parse import unquote

source = requests.get('https://faculty.math.illinois.edu/~icontrer/MATH415_Ivan_S18.html').text
soup = BeautifulSoup(source, 'lxml')

# with open('math/math415.html') as html_file:
#    soup = BeautifulSoup(html_file, 'lxml')

substring_1 = "https://faculty.math.illinois.edu"
substring_2 = ".pdf"

# for loop adapted from https://www.youtube.com/watch?v=HDEvWfSk2So together with https://www.youtube.com/watch?v=ng2o98k983k 
for link in soup.find_all('a') : # finds all links using <a> tag

    url = link.get('href')
    pdf = unquote(url) # transforms url (as a link) in a string called pdf

    if (substring_1 in pdf and substring_2 in pdf): # checks to make sure we have correct pdf links
        r = requests.get(url) # use "url" instead of "pdf" since "pdf" is a string representation of "url"
        lecture_name = r.url[url.rfind('/')+1:] # gets the name of the pdf by finding the last '/' and including everything after that last '/'
        
        print(lecture_name)

        with open('c:/users/samwa/eduweb_download_slides/math/math415/' + lecture_name, 'wb') as file:
            for chunk in r.iter_content(chunk_size=10000):
                if chunk: # checks to make sure chunk is not empty
                    file.write(chunk)

        # questions to ask Bhavya
        # 1. If same pdf link, uninclude it?

    else:
        print("non-pdf file")
    
    print()



# print(link)

# print(soup.prettify())

# print (r.text) for hmtl files
# print(r.content) for images