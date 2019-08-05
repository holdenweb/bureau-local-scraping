import requests

from bs4 import BeautifulSoup

url = "https://beta.charitycommission.gov.uk/charity-details/"
response = requests.get(url, params={'regId': "213890"})

soup = BeautifulSoup(response.content, 'lxml')
print(soup.find("p", attrs={"class": "pcg-charity-details__amount"}))
print(soup.find("p", attrs={"class": "pcg-charity-details__amount"}).text)
