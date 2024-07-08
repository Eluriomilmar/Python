"""Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code, use the code from the solution), and instead of printing the results to a screen, write the results to a txt file.
In your code, just make up a name for the file you are saving to."""


from bs4 import BeautifulSoup
import requests
base_url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"

r = requests.get(base_url)

soup = BeautifulSoup(r.text, "html.parser")

for story in soup.get_text():
    with open("file_to_save.txt", "a") as open_file:
        open_file.write(story)