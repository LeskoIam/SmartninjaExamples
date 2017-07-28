from BeautifulSoup import BeautifulSoup
from pprint import pprint
import requests
import csv

__author__ = 'mpolensek'
# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.


base_url = "https://scrapebook22.appspot.com/"
response = requests.get(base_url)
soup = BeautifulSoup(response.text)

all_td = soup.findAll("td")

count = 0
person_dict = {}
all_data = []
for tdata in soup.findAll("td"):
    count += 1
    if count == 1:
        person_dict["name"] = tdata.string
    elif count == 2:
        person_dict["last_name"] = tdata.string
    elif count == 3:
        person_dict["age"] = tdata.string
    elif count == 4:
        person_dict["city"] = tdata.string
    elif count == 5:
        person_dict["detail_link"] = base_url[:-1] + tdata.a["href"]
        email_response = requests.get(person_dict["detail_link"])
        email_soup = BeautifulSoup(email_response.text)
        person_dict["email"] = email_soup.find("span", attrs={"class": "email"}).string
        pprint(person_dict)
        all_data.append(person_dict)

        count = 0
        person_dict = {}

header = ["name", "last_name", "age", "city", "detail_link", "email"]
with open("all_details.csv", "wb") as csvfile:
    writer = csv.DictWriter(csvfile, delimiter=";", fieldnames=header)
    writer.writeheader()
    writer.writerows(all_data)





