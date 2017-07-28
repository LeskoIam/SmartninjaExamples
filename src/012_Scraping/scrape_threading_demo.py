import time
import requests
from threading import Thread
from BeautifulSoup import BeautifulSoup


def parse(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)

    for link in soup.findAll("a"):
        # print link, link.string
        if link.string == "See full profile":
            person_url = url[:-1] + link["href"]
            person_html = requests.get(person_url).text
            person_soup = BeautifulSoup(person_html)
            print person_soup.find("span", attrs={"class": "email"}).string


def faster_parse(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)

    threads = []
    for link in soup.findAll("a"):
        # print link, link.string
        if link.string == "See full profile":
            person_url = url[:-1] + link["href"]
            t = Thread(target=parse_url, args=(person_url, ))
            t.daemon = True

            threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()


def parse_url(person_url):
    person_html = requests.get(person_url).text
    person_soup = BeautifulSoup(person_html)
    print person_soup.find("span", attrs={"class": "email"}).string


if __name__ == '__main__':
    url = "https://scrapebook22.appspot.com/"

    start_time = time.time()
    parse(url)
    # faster_parse(url)
    print "TIME TAKEN: ", time.time() - start_time, "sec"
