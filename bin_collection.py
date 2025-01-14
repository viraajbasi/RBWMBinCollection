from bs4 import BeautifulSoup
import requests
import dateutil.parser

urpn = "ENTER YOUR URPN HERE"
url = "https://forms.rbwm.gov.uk/bincollections?uprn=" + urpn
content = requests.get(url).text

soup = BeautifulSoup(content, features="html.parser")
soup.prettify()

next_collection_div = soup.find("div", { "class": "widget-bin-collections" })

for tbody in next_collection_div.find_all("tbody"):
    for tr in tbody.find_all("tr"):
        td = tr.find_all("td")
        next_collection_type = td[0].get_text()
        next_collection_date = dateutil.parser.parse(td[1].get_text()).strftime("%d/%m/%Y")
        print("Bin Type: " + next_collection_type)
        print("Date: " + next_collection_date)
        print("\n")