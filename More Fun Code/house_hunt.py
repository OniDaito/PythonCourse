''' Hunts for houses in specific areas on moveflat '''

import urllib
from lxml import etree
import StringIO, string, webbrowser

url = "http://www.moveflat.com/london-flat/flatshare-flatmate/london-areas/property/Box/"
sock = urllib.urlopen(url)
htmlSource = sock.read()    
sock.close()
max_cost = 500

nice_areas = ["Angel","Islington", "Camden","Bow","Brick Lane",
"Euston", "Hampstead", "Homerton", "Kilburn", "Seven Sisters", "Shoreditch",
"Hackney", "Victoria", "Whitechapel"]

import lxml.html

previous_results = []

f = open('house_hunt.txt','r+')

for line in f:
	previous_results.append( line.strip() )


result = lxml.html.fromstring(htmlSource)

areas = result.get_element_by_id("Areas")

for element, attribute, link, pos in areas.iterlinks():

	for a in nice_areas:
		if a in element.text_content():
	
			newurl = "http://www.moveflat.com/" + link
			sock = urllib.urlopen(newurl)
			areaSource = sock.read()  
			sock.close()
			
			areaHtml =  lxml.html.fromstring(areaSource)
			areaAds =  areaHtml.get_element_by_id("ads")
			
			
			
			for area_element, area_attribute, area_link, area_pos in areaAds.iterlinks():
			
				if area_link in previous_results:
					break
			
				s = area_element.text_content()	
				s = s.encode("utf8")
				cost = s[string.rfind(s,"£") : ]
				cost = cost.replace(" ","")
				cost = cost.replace("\n","")
				cost = cost.replace("£","")
				
				real_cost = int(cost)
				
				if real_cost < max_cost:
					print area_link,real_cost
					webbrowser.open("http://www.moveflat.com/" + area_link)
					f.write(area_link +"\n")

f.close()	