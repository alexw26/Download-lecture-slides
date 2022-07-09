import requests

r = requests.get('https://faculty.math.illinois.edu/~icontrer/MATH415_Ivan_S18.html')

print(r.text)

# print(r.content) for images