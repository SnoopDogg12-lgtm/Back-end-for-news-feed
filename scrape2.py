import json, requests
from bs4 import BeautifulSoup

data = {
    "titles": [],
    "links": []
}

url = "https://thenextweb.com/latest"
request_to_url = requests.get(url)
soup = BeautifulSoup(request_to_url.text,'html.parser' )

main = soup.find("div", {"id": "articleList"})
links = main.find_all("a",href=True)

for link in links:
    if link.text != "\n\n\n\n\n":
        data["titles"].append(link.text)
        data["links"].append(f"https://thenextweb.com/{link['href']}")


with open('data2.json', 'w') as data_file:
    json.dump(data, data_file, indent=4)