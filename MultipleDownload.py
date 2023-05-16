import requests
from bs4 import BeautifulSoup

def geturl():
    url = 'https://www.inkitt.com/genres/erotica'
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
    req = requests.get(url = url, headers = header)
    req.encoding = "utf-8"
    html = req.text
    bes = BeautifulSoup(html,"lxml")
    texts = bes.find("div", class_= "page")
    chapters = texts.find_all("a")
    words = []

    for chapter in chapters:
        name = chapter.string
        url1 = url + chapter.get("href")
        word = [url1, name]
        words.append(word)
    return words

if __name__ == '__main__':
    target = geturl()
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
    for tar in target:
        req = requests.get(url=tar[0],headers = header)
        req.encoding = "utf-8"
        html = req.text
        bes = BeautifulSoup(html,"lxml")
        texts = bes.find("div", class_= "story-page-text")
        texts_list = texts.text.split("\xa0"*4)
        with open("F:/Git/yellowtext/"+ tar[1] + ".txt","w") as file:
            for line in texts_list:
                file.write(line+"\n")

