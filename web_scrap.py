# import the necessary libraries
import bs4
import requests

# make request to the website
res = requests.get('https://en.wikipedia.org/wiki/Deep_learning')
type(res.text)
# convert into class Beautiful Soup
soup = bs4.BeautifulSoup(res.text, 'lxml')
type(soup)
# .mw-headline is the class which was observed on the website using inspect element
# to find all the headings in the Wikipedia page
for i in soup.select('.mw-headline'):
    print(i.text)
