from BeautifulSoup import BeautifulSoup
import requests
# import urllib2
import csv

__author__ = 'mpolensek'
# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.

# ###### Cilj: Na strani moramo priti do email naslova vsakega, ki je nastet na strani ######

# URL katerega bomo obiskali
url = "https://scrapebook22.appspot.com/"

# Obisci stran in dobi surov HTML. Vsebino dobimo kot enden dolg string HTMLja.
response = requests.get(url)  # requests nacin
# response = urllib2.urlopen(url).read()  # urllib2 nacin

# Prikazemo vsebino strani (HTML)
print response.text  # requests nacin
# print response  # urllib2 nacin


# Parse
# Vsebino strani (celoten HTML string) podatmo BeautifulSoup - ta ga "precese" in zgradi boljso strukturo
# za hitrejsi in lazji dostop do posameznih tagov.
soup = BeautifulSoup(response.text)
# soup = BeautifulSoup(response)  # urllib2 nacin

# Poglejmo naslov strani (title)
print soup.html.head.title.string
# Najdemo vse link tage (<a href=.....>)
# .findAll isce po tag-ih!
print soup.findAll("a")


# 1. Najdemo vse link tage
for link in soup.findAll("a"):
    # 2. Zanimajo nas samo tisti ki imajo ime linka "See full profile"
    if link.string == "See full profile":
        # 3. Iz osnovnega url-ja in url-ja povezave na podrobnosti zgradimo celoten naslov do podrobnosti vsakega posameznika
        detail_link = url[:-1] + link["href"]
        print detail_link
        # 4. Obiscemo podstran s podropnostmi
        email_response = requests.get(detail_link)
        print email_response.text
        # 5. Iz podstrani naredmo nov BeautifulSoup objekt. Enako kot za glavno stran.
        email_soup = BeautifulSoup(email_response.text)
        # 6. Po vsebini podstrani iscemo tag "span" s class-om z imenom "email". Te iskalne pogoje podamo kot dict
        email = email_soup.find("span", attrs={"class": "email"}).string

        print email


# Enako kot zgoraj le da shrani se v csv (comma separated values) file
# Ko uporabljamo csv modul moramo file obvezno odpreti v "_b" (binary) nacinu!
with open('eggs.csv', 'wb') as csvfile:
    # Naredimo writer objekt, ki ga podpira razne metode za pisanje v csv file
    # Dolocimo tudi locilo. Za slovenscino se priporoca ";" saj selo radi uporabljamo decimalno vejico
    writer = csv.writer(csvfile, delimiter=";")
    for link in soup.findAll("a"):
        if link.string == "See full profile":
            detail_link = url[:-1] + link["href"]
            email_response = requests.get(detail_link)
            email_soup = BeautifulSoup(email_response.text)
            email = email_soup.find("span", attrs={"class": "email"}).string

            # Zapisemo eno vrstico, podamo jo kot list
            writer.writerow(['Email', email])
