linksfile = open('webpages.txt', 'r+') #open the file with pages in it
links = linksfile.read().splitlines() 
import requests
import csv
from xml.etree import ElementTree
import re
import requests
API = "http://access.alchemyapi.com/calls/url/URLGetLanguage?apikey=ENTERAPIKEY&url="
for link in links: 
	from xml.etree import ElementTree
	page = API+link # create a variable called page which is the API page to fetch
	r =  requests.get(page) # ping the API for each page assign the variable r
	doc = ElementTree.fromstring(r.text) #get the text content from r and assign it the name doc
	for tag in doc.findall('.//language'): #find all of the language tags...
		language = tag.text # assign the language tag the variable language
		with open("outputfile.csv", "a") as backlinkfile:
			backlinkfilewriter = csv.writer(backlinkfile)
			backlinkfilewriter.writerow([link,language])
			backlinkfile.close()