from bs4 import BeautifulSoup
import requests


class Scrape:
    def jjk_chapter_check(self):
        jjkxml = 'https://mangasee123.com/rss/Jujutsu-Kaisen.xml'
        source = requests.get(jjkxml).text
        soup = BeautifulSoup(source, 'lxml')
        contents = soup.find_all('title')
        print(contents)
        new_chp = contents[2].text
        return new_chp

    def jjk_link(self):
        jjkxml = 'https://mangasee123.com/rss/Jujutsu-Kaisen.xml'
        source = requests.get(jjkxml).text
        soup = BeautifulSoup(source, features='xml')
        contents = soup.find_all('link')
        print(contents)
        chp_link = contents[3].text
        return chp_link

    def csm_chapter_check(self):
        csmxml = 'https://mangasee123.com/rss/Chainsaw-Man.xml'
        source = requests.get(csmxml).text
        soup = BeautifulSoup(source, 'lxml')
        contents = soup.find_all('title')
        print(contents)
        new_chp = contents[2].text
        return new_chp

    def csm_link(self):
        csmxml = 'https://mangasee123.com/rss/Chainsaw-Man.xml'
        source = requests.get(csmxml).text
        soup = BeautifulSoup(source, features='xml')
        contents = soup.find_all('link')
        print(contents)
        chp_link = contents[3].text
        return chp_link

    def snk_chapter_check(self):
        snkxml = 'https://mangasee123.com/rss/Shingeki-No-Kyojin.xml'
        source = requests.get(snkxml).text
        soup = BeautifulSoup(source, 'lxml')
        contents = soup.find_all('title')
        print(contents)
        new_chp = contents[2].text
        return new_chp

    def snk_link(self):
        snkxml = 'https://mangasee123.com/rss/Shingeki-No-Kyojin.xml'
        source = requests.get(snkxml).text
        soup = BeautifulSoup(source, features='xml')
        contents = soup.find_all('link')
        print(contents)
        chp_link = contents[3].text
        return chp_link

    def sl_chapter_check(self):
        slxml = 'https://mangasee123.com/rss/Solo-Leveling.xml'
        source = requests.get(slxml).text
        soup = BeautifulSoup(source, 'lxml')
        contents = soup.find_all('title')
        print(contents)
        new_chp = contents[2].text
        return new_chp

    def sl_link(self):
        slxml = 'https://mangasee123.com/rss/Solo-Leveling.xml'
        source = requests.get(slxml).text
        soup = BeautifulSoup(source, features='xml')
        contents = soup.find_all('link')
        print(contents)
        chp_link = contents[3].text
        return chp_link

    def brsrk_chapter_check(self):
        brsrkxml = 'https://mangasee123.com/rss/Berserk.xml'
        source = requests.get(brsrkxml).text
        soup = BeautifulSoup(source, 'lxml')
        contents = soup.find_all('title')
        print(contents)
        new_chp = contents[2].text
        return new_chp

    def brsrk_link(self):
        brsrkxml = 'https://mangasee123.com/rss/Berserk.xml'
        source = requests.get(brsrkxml).text
        soup = BeautifulSoup(source, features='xml')
        contents = soup.find_all('link')
        print(contents)
        chp_link = contents[3].text
        return chp_link

    def bc_chapter_check(self):
        bcxml = 'https://mangasee123.com/rss/Black-Clover.xml'
        source = requests.get(bcxml).text
        soup = BeautifulSoup(source, 'lxml')
        contents = soup.find_all('title')
        print(contents)
        new_chp = contents[2].text
        return new_chp

    def bc_link(self):
        bcxml = 'https://mangasee123.com/rss/Black-Clover.xml'
        source = requests.get(bcxml).text
        soup = BeautifulSoup(source, features='xml')
        contents = soup.find_all('link')
        print(contents)
        chp_link = contents[3].text
        return chp_link

    def tog_chapter_check(self):
        togxml = 'https://mangasee123.com/rss/Tower-Of-God.xml'
        source = requests.get(togxml).text
        soup = BeautifulSoup(source, 'lxml')
        contents = soup.find_all('title')
        print(contents)
        new_chp = contents[2].text
        return new_chp

    def tog_link(self):
        togxml = 'https://mangasee123.com/rss/Tower-Of-God.xml'
        source = requests.get(togxml).text
        soup = BeautifulSoup(source, features='xml')
        contents = soup.find_all('link')
        print(contents)
        chp_link = contents[3].text
        return chp_link
