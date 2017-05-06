import requests
from pprint import pprint
from BeautifulSoup import BeautifulSoup

__author__ = 'mpolensek'


# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.


class ArsoVremePostaja(object):
    def __init__(self, postaja, vreme, temp, vlaga, v_smer, v_hitrost, v_sunki, tlak):
        self.postaja = unicode(postaja)
        self.vreme = unicode(vreme)
        self.temp = unicode(temp)
        self.vlaga = unicode(vlaga)
        self.v_smer = unicode(v_smer)
        self.v_hitrost = unicode(v_hitrost)
        self.v_sunki = unicode(v_sunki)
        self.tlak = unicode(tlak)

    def temp_F(self):
        return float(self.temp)*1.45

def main(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html)
    all_places = soup.find("table", attrs={"class": "online"})

    all_places = all_places.findAll("tr")

    data = []
    for row in all_places:
        cols = row.findAll('td')
        cols = [ele.text.strip() for ele in cols]
        raw_data = [ele for ele in cols if ele]  # Get rid of empty values
        try:
            vreme = ArsoVremePostaja(postaja=raw_data[0],
                                     vreme=raw_data[1],
                                     temp=raw_data[2],
                                     vlaga=raw_data[3],
                                     v_smer=raw_data[4],
                                     v_hitrost=raw_data[5],
                                     v_sunki=raw_data[6],
                                     tlak=raw_data[9])
            data.append(vreme)
        except IndexError as err:
            print "ERROR: {err}".format(err=err.message)
    return data


if __name__ == '__main__':
    url = "http://www.arso.gov.si/vreme/napovedi%20in%20podatki/vreme_si.html"
    vreme = main(url)
    for postaja in vreme:
        print postaja.postaja
        print postaja.vreme
        print postaja.temp
        print postaja.vlaga
        print postaja.v_smer
        print postaja.v_hitrost
        print postaja.v_sunki
        print postaja.tlak
        print postaja.temp_F()
