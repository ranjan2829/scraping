# IMPORT ALL THE REQUIRED LIBRARIES
from bs4 import BeautifulSoup as BS
import requests as req

url = "https://www.businesstoday.in/latest/economy"

webpage = req.get(url)
trav = BS(webpage.content, "html.parser")
M = 1
for link in trav.find_all('a'):
	
	# PASTE THE CLASS TYPE THAT WE GET
	# FROM THE ABOVE CODE IN THIS AND
	# SET THE LIMIT GRATER THAN 35
	if(str(type(link.string)) == "<class 'bs4.element.NavigableString'>"
	and len(link.string) > 35):

		print(str(M)+".", link.string)
		M += 1
