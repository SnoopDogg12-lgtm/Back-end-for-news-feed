import json, requests
from bs4 import BeautifulSoup

class Scrapper:
    def __init__(self,url,element_to_look_for,id_or_class,name,file_name,base_url):
        self.url = url
        self.element_to_look_for = element_to_look_for
        self.id_or_class = id_or_class
        self.file_name = file_name
        self.name = name
        self.base_url = base_url
        self.request_to_page = None
        self.soup = None
        self.data = {
            "titles": [],
            "links": []
        }
    
    def access_page_content(self):
        # Trying to connect to the page and gets its html content
        try:
            self.request_to_page = requests.get(self.url)
            self.soup = BeautifulSoup(self.request_to_page.text,'html.parser')
        except:
            print("Something went wrong with the request to the website !")

    def scrape_content(self):
        if self.id_or_class != "":
            element = self.soup.find(f"{self.element_to_look_for}", {f"{self.id_or_class}": f"{self.name}"})
        else:
            element = self.soup.find(f"{self.element_to_look_for}")

        links = element.find_all("a",href=True)

        for link in links:
            if link.text != "":
                self.data["titles"].append(link.text)
                
                # Checking if the scraped link doesn't contain https
                # and in case it doesn't we append the base url to the secondary url
                if "https" not in str(link["href"]):
                    self.data["links"].append(f'{self.base_url}{link["href"]}')
                else:
                    self.data["links"].append(f'{link["href"]}')

        with open(f'{self.file_name}',"w") as data_file:
            json.dump(self.data, data_file, indent=4)


scrapper = Scrapper("https://news.sky.com/world","div","class","sdc-site-tiles__group","data3.json","https://news.sky.com")
scrapper.access_page_content()
scrapper.scrape_content()