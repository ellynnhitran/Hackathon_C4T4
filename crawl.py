from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

list_empty = []
for i in range(1,6):
    url = "https://cookpad.com/vn/tim-kiem/th%E1%BB%B1c%20d%C6%B0%E1%BB%A1ng?event=search.suggestion&page={0}".format(i)
    connection = urlopen(url)  #open
    raw_data = connection.read()  #read
    text = raw_data.decode("utf-8") 
    soup = BeautifulSoup(text, "html.parser")
    section = soup.find("div", id="main_contents")
    li = section.find_all("li")
    dictionary_empty = {}
    for item in li:
        if item.img is not None:
            dictionary_empty = {
                "title": item.find('h2').span.string,
                "img" : item.img['src'],
                "nguyenlieu" : item.find('div','wide-card__body').string
            }
            list_empty.append(dictionary_empty)

pyexcel.save_as(records=list_empty, dest_file_name="test.xlsx")