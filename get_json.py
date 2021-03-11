import urllib.request
import json

'''
Get the sample-data from the json
'''

# change this to your own ip.
url = "http://127.0.0.1:5000/api/v1/resources/programming/all"

# ------------------------------------- #

request = urllib.request.Request(url)
response = urllib.request.urlopen(request)

json = json.loads(response.read())

for i in json:
	text = "Programming language {} is best for {}".format(i["title"], i["text"])
	print(text)

