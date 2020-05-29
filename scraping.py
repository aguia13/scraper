from bs4 import BeautifulSoup
import requests


def main():

	r = requests.get('https://api.scrapingdog.com/scrape?api_key=<y5ed06433f82ad608d30d40d8>&url=https://apiworld.co/awards/api-300-top-industry-innovations/').text
	soup = BeautifulSoup(r,'html.parser')
	allapis = soup.find_all("tr")
	l={}
	u=list()

	for i in range(0,len(allapis)):
		try:
			api = allapis[i].find_all("td")
		except:
			api=None
		try:
			l["company"]=api[0].text.replace("\n","")
		except:
			l["company"]=None

		try:
			l["api"]=api[1].text.replace("\n","")
		except:
			l["api"]=None

		try:
			l["category"]=api[2].text.replace("\n","")
		except:
			l["category"]=None
		print(l)
		u.append(l)
		l={}
	print(u)



	return


if __name__ == '__main__':
	main()