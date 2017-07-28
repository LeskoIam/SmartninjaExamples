from urllib2 import urlopen

url = 'https://scrapebook22.appspot.com/'
response = urlopen(url).read()

print response
