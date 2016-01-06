import re
import urllib2 as lib2
import requests
#url that are the pages interesting
mainurl="exportersindia.com/indian-suppliers/"
# source of urls
baseurl= "http://www.exportersindia.com/indian-manufacturers/plant-seed.htm"
#open the page with urlib2
page = lib2.urlopen(baseurl)
#read the content of the base url
content = page.read()
#use regex to find all urls on page content
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
#array empty
urls_interesteds = []
#find the urls interesting for us who has a seeds 
baseurlll="exportersindia"
under_urls=[]
# url="http://www.exportersindia.com/indian-suppliers/fennel-seeds"+number+".htm?action=ajax_load_classified"
error="Fatal error: Call to a member function getAttribute() on a non-object in /home/sgupta/exportersindia.com/htdocs/catg_product_search_temp.php on line 40"
seeds_name=[]
final_seed_name=[]
each_seed_url=[]
for i in urls:
    if mainurl in i:
        urls_interesteds.append(i)
        # print i
# print len(urls_interesteds)
urls_interesteds.pop()
# print len(urls_interesteds)
for each_item in urls_interesteds:
	r=re.findall(r'/[\w\d -]+.htm',each_item)
	print r
	r3=r[0]
	seeds_name.append(r3[1:])
for each_seed in seeds_name:
	new_each_seed=each_seed[:-4]
	final_seed_name.append(new_each_seed)
	print new_each_seed
	seeds_url= "http://www.exportersindia.com/indian-suppliers/"+new_each_seed+".htm?action=ajax_load_classified"
	each_seed_url.append(seeds_url)
urltemplate="http://www.exportersindia.com/indian-suppliers/{}{}.htm?action=ajax_load_classified".format
searchurls=[urltemplate(s,pno) for s in final_seed_name for pno in range(1,25,1)]
for each_url_item in searchurls:
	# rany=requests.get(each_item)
	# print rany
	# print each_url_item
	r=requests.get(each_url_item)
	if r.content==error:
		print r.content
		break
	else:
		data=r.content
		webs=re.findall(r"'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",data)
		# print type(webs)
		for each_webs in webs:
			if baseurlll in each_webs:
				st=each_webs[1:]
				st2=st[:-2]
				if st2=="http://advertisers.exportersindia.com/":
					continue
				else:
					under_urls.append(st2)
for tr in under_urls:
	print tr
