import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Please Enter the link: ") #Please don't forget to enter your link

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('span')
count = 0
for tag in tags:
    count = count + int(tag.contents[0])

print(count)
#if you're using CMD please don't forget to first copy everything from line 1 - 10, type in your link, and then copy
#the code again from line 11 - 21