import urllib.request
import json
page2 = urllib.request.Request("http://127.0.0.1:8000/update_item",  headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'})
openpage2 = urllib.request.urlopen(page2)
print (json.load(page2))