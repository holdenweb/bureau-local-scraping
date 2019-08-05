#
# Import the libraries you need ... you may need to install them
# into your Python environment as they don't come with Python.
#
import requests                      # For fetching webpages
from bs4 import BeautifulSoup        # For drilling down into the webpage

#
# Store the basic URL we need
#
url = "https://beta.charitycommission.gov.uk/charity-details/"

#
# Fetch the URL, adding parameters to the request. This lets you
# use data already available (like a charity number) to make further
# requests. In this case the effective URL is:
#
#     https://beta.charitycommission.gov.uk/charity-details/?regId=213890
#
response = requests.get(url, params={'regId': "213890"})

#
# Now drill down into the page ('response'), and turn it into a more easily scrapable object
#
soup = BeautifulSoup(response.content, 'lxml')

#
# Print the results of drilling down into that, specifying a particular attribute we want to grab
#
print(soup.find("p", attrs={"class": "pcg-charity-details__amount"}))

#
# Then showing the text only (no tags) using .text
#
print(soup.find("p", attrs={"class": "pcg-charity-details__amount"}).text)
