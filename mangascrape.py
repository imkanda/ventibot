from bs4 import BeautifulSoup
import requests


class Scrape:
    def jjk_chapter_check(self):
        jjkxml = 'https://mangasee123.com/rss/Jujutsu-Kaisen.xml'
        source = requests.get(jjkxml).text
        soup = BeautifulSoup(source, 'lxml')
        contents = soup.find_all('title')
        new_chp = contents[2].text
        return new_chp

    def jjk_link(self):
        jjkxml = 'https://mangasee123.com/rss/Jujutsu-Kaisen.xml'
        source = requests.get(jjkxml).text
        soup = BeautifulSoup(source, features='xml')
        contents = soup.find_all('link')
        chp_link = contents[3].text
        return chp_link

    def csm_chapter_check(self):
        csmxml = 'https://mangasee123.com/rss/Chainsaw-Man.xml'
        source = requests.get(csmxml).text
        soup = BeautifulSoup(source, 'lxml')
        contents = soup.find_all('title')
        new_chp = contents[2].text
        return new_chp

    def csm_link(self):
        csmxml = 'https://mangasee123.com/rss/Chainsaw-Man.xml'
        source = requests.get(csmxml).text
        soup = BeautifulSoup(source, features='xml')
        contents = soup.find_all('link')
        chp_link = contents[3].text
        return chp_link

    def snk_chapter_check(self):
        snkxml = 'https://mangasee123.com/rss/Shingeki-No-Kyojin.xml'
        source = requests.get(snkxml).text
        soup = BeautifulSoup(source, 'lxml')
        contents = soup.find_all('title')
        new_chp = contents[2].text
        return new_chp

    def snk_link(self):
        snkxml = 'https://mangasee123.com/rss/Shingeki-No-Kyojin.xml'
        source = requests.get(snkxml).text
        soup = BeautifulSoup(source, features='xml')
        contents = soup.find_all('link')
        chp_link = contents[3].text
        return chp_link

    def sl_chapter_check(self):
        slxml = 'https://mangasee123.com/rss/Solo-Leveling.xml'
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        source = requests.get(slxml, headers=header).text
        soup = BeautifulSoup(source, 'lxml')
        contents = soup.find_all('title')
        new_chp = contents[2].text
        return new_chp

    def sl_link(self):
        slxml = 'https://mangasee123.com/rss/Solo-Leveling.xml'
        source = requests.get(slxml).text
        soup = BeautifulSoup(source, features='xml')
        contents = soup.find_all('link')
        chp_link = contents[3].text
        return chp_link

    def brsrk_chapter_check(self):
        brsrkxml = 'https://mangasee123.com/rss/Berserk.xml'
        source = requests.get(brsrkxml).text
        soup = BeautifulSoup(source, 'lxml')
        contents = soup.find_all('title')
        new_chp = contents[2].text
        return new_chp

    def brsrk_link(self):
        brsrkxml = 'https://mangasee123.com/rss/Berserk.xml'
        source = requests.get(brsrkxml).text
        soup = BeautifulSoup(source, features='xml')
        contents = soup.find_all('link')
        chp_link = contents[3].text
        return chp_link

    def bc_chapter_check(self):
        bcxml = 'https://mangasee123.com/rss/Black-Clover.xml'
        source = requests.get(bcxml).text
        soup = BeautifulSoup(source, 'lxml')
        contents = soup.find_all('title')
        new_chp = contents[2].text
        return new_chp

    def bc_link(self):
        bcxml = 'https://mangasee123.com/rss/Black-Clover.xml'
        source = requests.get(bcxml).text
        soup = BeautifulSoup(source, features='xml')
        contents = soup.find_all('link')
        chp_link = contents[3].text
        return chp_link

    def tog_chapter_check(self):
        togxml = 'https://mangasee123.com/rss/Tower-Of-God.xml'
        source = requests.get(togxml).text
        soup = BeautifulSoup(source, 'lxml')
        contents = soup.find_all('title')
        new_chp = contents[2].text
        return new_chp

    def tog_link(self):
        togxml = 'https://mangasee123.com/rss/Tower-Of-God.xml'
        source = requests.get(togxml).text
        soup = BeautifulSoup(source, features='xml')
        contents = soup.find_all('link')
        chp_link = contents[3].text
        return chp_link

    def op_chapter_check(self):
        opxml = 'https://mangasee123.com/rss/One-Piece.xml'
        source = requests.get(opxml).text
        soup = BeautifulSoup(source, 'lxml')
        contents = soup.find_all('title')
        new_chp = contents[2].text
        return new_chp

    def op_link(self):
        opxml = 'https://mangasee123.com/rss/One-Piece.xml'
        source = requests.get(opxml).text
        soup = BeautifulSoup(source, features='xml')
        contents = soup.find_all('link')
        chp_link = contents[3].text
        return chp_link

    def boxer_chapter_check(self):
        boxerxml = 'https://mangasee123.com/rss/The-Boxer.xml'
        source = requests.get(boxerxml).text
        soup = BeautifulSoup(source, 'lxml')
        contents = soup.find_all('title')
        new_chp = contents[2].text
        return new_chp

    def boxer_link(self):
        boxerxml = 'https://mangasee123.com/rss/The-Boxer.xml'
        source = requests.get(boxerxml).text
        soup = BeautifulSoup(source, features='xml')
        contents = soup.find_all('link')
        chp_link = contents[3].text
        return chp_link

    def bl_chapter_check(self):
        blxml = 'https://mangasee123.com/rss/Blue-Lock.xml'
        source = requests.get(blxml).text
        soup = BeautifulSoup(source, 'lxml')
        contents = soup.find_all('title')
        new_chp = contents[2].text
        return new_chp

    def bl_link(self):
        blxml = 'https://mangasee123.com/rss/Blue-Lock.xml'
        source = requests.get(blxml).text
        soup = BeautifulSoup(source, features='xml')
        contents = soup.find_all('link')
        chp_link = contents[3].text
        return chp_link

    def BATE_chapter_check(self):
        BATExml = 'https://mangasee123.com/rss/The-Beginning-After-The-End.xml'
        source = requests.get(BATExml).text
        soup = BeautifulSoup(source, 'lxml')
        contents = soup.find_all('title')
        new_chp = contents[2].text
        return new_chp

    def BATE_link(self):
        BATExml = 'https://mangasee123.com/rss/The-Beginning-After-The-End.xml'
        source = requests.get(BATExml).text
        soup = BeautifulSoup(source, features='xml')
        contents = soup.find_all('link')
        chp_link = contents[3].text
        return chp_link

    def OPM_chapter_check(self):
        OPMxml = 'https://mangasee123.com/rss/Onepunch-Man.xml'
        source = requests.get(OPMxml).text
        soup = BeautifulSoup(source, 'lxml')
        contents = soup.find_all('title')
        new_chp = contents[2].text
        return new_chp

    def OPM_link(self):
        OPMxml = 'https://mangasee123.com/rss/Onepunch-Man.xml'
        source = requests.get(OPMxml).text
        soup = BeautifulSoup(source, features='xml')
        contents = soup.find_all('link')
        chp_link = contents[3].text
        return chp_link

    def ddd_chapter_check(self):
        DDDxml = 'https://mangasee123.com/rss/Dandadan.xml'
        source = requests.get(DDDxml).text
        soup = BeautifulSoup(source, 'lxml')
        contents = soup.find_all('title')
        new_chp = contents[2].text
        return new_chp

    def ddd_link(self):
        DDDxml = 'https://mangasee123.com/rss/Dandadan.xml'
        source = requests.get(DDDxml).text
        soup = BeautifulSoup(source, features='xml')
        contents = soup.find_all('link')
        chp_link = contents[3].text
        return chp_link

    def kengan_chapter_check(self):
        Kenganxml = 'https://mangasee123.com/rss/Kengan-Omega.xml'
        source = requests.get(Kenganxml).text
        soup = BeautifulSoup(source, 'lxml')
        contents = soup.find_all('title')
        new_chp = contents[2].text
        return new_chp

    def kengan_link(self):
        Kenganxml = 'https://mangasee123.com/rss/Kengan-Omega.xml'
        source = requests.get(Kenganxml).text
        soup = BeautifulSoup(source, features='xml')
        contents = soup.find_all('link')
        chp_link = contents[3].text
        return chp_link
