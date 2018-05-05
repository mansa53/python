import requests
url='https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+Bangalore&price_level=5&rating=4&key=AIzaSyA_cejruGmaxJJzGFPt9_ouDZRgksqGyCc'
json_data=requests.get(url).json()
#print(json_data)

json_status=json_data['next_page_token']
#print('API status'+json_status)
for each  in json_data['results']:
	print(each['name'])
json_place=json_data['results'][0]['name']
print(json_place)
