import socket
import urllib.request

website = "http://data.pr4e.org/romeo.txt"
website = website.split("/")
print(website)
for i in website:
    print(i, end="/")