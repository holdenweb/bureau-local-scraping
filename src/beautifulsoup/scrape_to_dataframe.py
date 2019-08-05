#Import the necessary libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://beta.charitycommission.gov.uk/charity-details/"

#Create some empty lists first
idlist = []
amountlist = []
#Create a list of charity IDs:
charityids = ["213890", "213891", "213892", "213894"]
#Loop through them:
for eachid in charityids:
  response = requests.get(url, params={'regId': eachid})
  #Now drill down into the page ('response'), and turn it into a more easily scrapable object
  soup = BeautifulSoup(response.content, 'lxml')
  #Print the results of drilling down into that, specifying a particular attribute we want to grab
  print(soup.find("p", attrs={"class": "pcg-charity-details__amount"}))
  #Then showing the text only (no tags) using .text
  print(soup.find("p", attrs={"class": "pcg-charity-details__amount"}).text)
  #Store as charityamount
  charityamount = soup.find("p", attrs={"class": "pcg-charity-details__amount"}).text
  #Append to list
  amountlist.append(charityamount)
  #Append the id, too - although we don't really need to do this
  idlist.append(eachid)

#Once that loop has finished we have two lists
print(amountlist)
print(idlist)

#Create a dictionary with those lists
d = {'charityid': idlist, 'amount': amountlist}
#Convert to a pandas data frame
df = pd.DataFrame(data=d)
#Show it
print(df)

#Export as a CSV file using the .to_csv function https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html
df.to_csv('allscrapeddata.csv')
