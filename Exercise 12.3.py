import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ") # Please don't forget to enter URL
count = input("Enter Count: ") # Please don't forget to enter count
position = input('Enter Position: ') # Please don't forget to enter position
count = int(count)
position = int(position)
a = position
while count != 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        if position != 0:
            url = tag.get('href', None)
            print(url)
            c = tag.contents[0]
            position = position - 1
        else:
            break
    count = count - 1
    position = a

print('Last Name in Sequence is', c)