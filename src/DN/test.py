__author__ = 'mpolensek'
# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.

import requests
from BeautifulSoup import BeautifulSoup

url = 'http://quotes.yourdictionary.com/theme/marriage/'

#response = urllib2.urlopen(url).read()

response = requests.get(url)

soup = BeautifulSoup(response.text)

all_quotes = soup.findAll('p', attrs={'class': 'quoteContent'})


count = 0
for single_quote in all_quotes:
    print single_quote.text
    print "******************"
    count += 1
    if count == 5:
        break
