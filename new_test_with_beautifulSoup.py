import requests
from bs4 import BeautifulSoup
import urllib3
import json

#--------------------- bug1 
#------------------ bug2



# disable HTTPS warnings
urllib3.disable_warnings()

#EUCTR URL link
URL = "https://www.clinicaltrialsregister.eu/ctr-search/search?query=cancer"

r  = requests.get(URL,verify=False)

data = r.content

soup = BeautifulSoup(data)

for link in soup.find_all("div", class_="results grid_8plus"):
    print(link.get('href'))