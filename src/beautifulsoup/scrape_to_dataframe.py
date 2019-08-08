#
# Import the necessary libraries
#
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://beta.charitycommission.gov.uk/charity-details/"

#
# Create empty lists to hold ids and amounts
#
idlist = []
amountlist = []
#
# Set up the list of charity IDs of interest
#
charityids = ["213890", "213891", "213892", "213894"]

#
# Loop through list, processing each id to retrieve the amount
#
for id in charityids:
    response = requests.get(url, params={"regId": id})
    #
    # Extract the content from the response
    # and build a searchable "HTML soup".
    #
    soup = BeautifulSoup(response.content, "lxml")
    #
    # The relevant paragraph has a class of "pcg-charity-details__amount"
    # so select it using the soup's find method.
    #
    print(soup.find("p", attrs={"class": "pcg-charity-details__amount"}))
    #
    # The paragraph's text attribute is the content, no markup
    #
    print(soup.find("p", attrs={"class": "pcg-charity-details__amount"}).text)
    #
    # Save the value in a variable
    #
    charityamount = soup.find("p", attrs={"class": "pcg-charity-details__amount"}).text
    #
    # Append the id and amount to their resp[ective lists
    #
    idlist.append(id)
    amountlist.append(charityamount)

#
# Print the accumulated lists
#
print(amountlist)
print(idlist)

#
# Create a dictionary representing each column of
# a dataframe as a named list of values.
#
d = {"charityid": idlist, "amount": amountlist}

#
# Build a pandas DataFrame from that dictionary and show it
# - see http://queirozf.com/entries/pandas-dataframe-by-example
#
df = pd.DataFrame(data=d)
print(df)

#
# Export as a CSV file using the dataframe's to_csv method
# - see http://bit.ly/holdenweb_datraframe_to_csv
# Yes, I'm dyslexic. Sue me :P
#
df.to_csv("allscrapeddata.csv")
