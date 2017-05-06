from BeautifulSoup import BeautifulSoup
import requests
# import urllib2
import csv



__author__ = 'mpolensek'
# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.

url = "https://scrapebook22.appspot.com/"
# response = urllib2.urlopen(url).read()
response = requests.get(url)
# print response.text

# Parse
soup = BeautifulSoup(response.text)
# print soup.html.head.title.string

# print soup.findAll("a")
with open('eggs.csv', 'wb') as csvfile:
    for link in soup.findAll("a"):
        if link.string == "See full profile":
            detail_link = url[:-1] + link["href"]
            # print detail_link
            email_response = requests.get(detail_link)
            # print email_response.text
            email_soup = BeautifulSoup(email_response.text)
            email = email_soup.find("span", attrs={"class": "email"}).string


            writer = a.writer(csvfile, delimiter=";")
            writer.writerow(['Spam', email])
