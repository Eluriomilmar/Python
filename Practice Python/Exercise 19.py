"""Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture."""


from bs4 import BeautifulSoup
import requests
base_url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"

r = requests.get(base_url)

soup = BeautifulSoup(r.text, "html.parser")

for story in soup.get_text():
    if story == ".":
        print(story)
    else:
        print(story, end = "")