import requests


def Main():
	param = {
		"country" : "in",
		"sortBy" : "top",
		"apiKey" : "67079904a0ab4ac8b188b7f432a99569"
	}
	url = "https://newsapi.org/v2/top-headlines"
	res = requests.get(url,params = param)
	#print(res)
	page = res.json()
	articles = page["articles"]
	results = []

	for ar in articles:
		results.append(ar["title"])

	for i in range(len(results)):
		print(i+1,results[i])

if __name__ == '__main__':
	Main()