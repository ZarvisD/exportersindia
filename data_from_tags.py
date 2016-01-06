import requests
import re
from bs4 import BeautifulSoup
url="http://www.exportersindia.com/snow-falcon-international/products.htm?slno=569039"
content_data="taj pt10px"
r=requests.get(url)
soup=BeautifulSoup(r.content,'lxml')
mydata=soup.findAll("p",{"class":"taj pt10px"})
print mydata[0].get_text()
myadd=soup.findAll("p",{"itemprop":"streetAddress"})
print myadd[0].get_text()
myphone=soup.findAll("span",{"itemprop":"telephone"})
for ph in myphone:
	print ph.get_text()
