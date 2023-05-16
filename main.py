#This python code is used to download some precific page
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'https://www.inkitt.com/stories/erotica/627591'
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
    fileSaveName = 'An Unwilling Mate'
    req = requests.get(url=url,headers = header)
    req.encoding = 'utf-8'
    html = req.text
    bes = BeautifulSoup(html,"lxml")
    texts = bes.find("div", class_= "story-page-text")
    texts_list = texts.text.split("\xa0"*4)
    with open("F:/Git/yellowtext/{}.txt".format(fileSaveName),"w",encoding='utf-8') as file:
        for line in texts_list:
            file.write(line+"\n")



