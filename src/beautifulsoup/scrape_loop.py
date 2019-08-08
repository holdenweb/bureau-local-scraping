import requests
from bs4 import BeautifulSoup

#
# Store the basic URL we need
#
url = "https://beta.charitycommission.gov.uk/charity-details/"

#
# Fetch the URL, also adding some parameters at the end. The resulting URL is
# https://beta.charitycommission.gov.uk/charity-details/?regId=213890
# Create a list of charity IDs:
#
charityids = ["213890", "213891", "213892"]

#
# Loop through them:
#
for eachid in charityids:
    #
    # Get the page's response, whose `content` attribute holds the HTML
    #
    response = requests.get(url, params={"regId": eachid})

    #
    # Now turn the HTML into a more easily scrapable object
    #
    soup = BeautifulSoup(response.content, "lxml")

    #
    # Print the results of drilling down into that, specifying a particular attribute we want to grab
    #
    print(soup.find("p", attrs={"class": "pcg-charity-details__amount"}))

    #
    # Then showing the text only (no tags) using .text
    #
    print(soup.find("p", attrs={"class": "pcg-charity-details__amount"}).text)
