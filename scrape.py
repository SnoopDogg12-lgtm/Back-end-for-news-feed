import json, requests
from bs4 import BeautifulSoup

data = {
    "titles": [],
    "links": []
}

url = "https://www.wired.co.uk/"
request_to_url = requests.get(url)
soup = BeautifulSoup(request_to_url.text,'html.parser' )

main = soup.find("main")
links = main.find_all("a",href=True)

for link in links:
    if link.text != "":
        data["titles"].append(link.text)
        data["links"].append(f"https://www.wired.co.uk{str(link['href'])}")


with open('data.json', 'w') as data_file:
    json.dump(data, data_file, indent=4)