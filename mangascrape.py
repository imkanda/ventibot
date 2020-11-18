from bs4 import BeautifulSoup
import requests


class Scrape:
    def jjk_chapter_check(self):
        # source url
        source = requests.get('https://www.readjujutsukaisen.com/').text
        soup = BeautifulSoup(source, 'lxml')
        # loops through all fields with specified class
        contents = soup.find_all(class_="col-span-3")
        # newest_chp is the 2nd chapter in the list, aka latest uploaded/updated
        # newest_chp = contents[5]
        # chp_number is only the text portion showing chp number
        chp_number = contents[5].a.text
        return chp_number

    def jjk_link(self):
        # source url
        source = requests.get('https://www.readjujutsukaisen.com/').text
        soup = BeautifulSoup(source, 'lxml')
        # loops through all fields with specified class
        contents = soup.find_all(class_="col-span-3")
        # newest_chp is the 2nd chapter in the list, aka latest uploaded/updated
        # newest_chp = contents[5]
        # chp_link is hyperlink for new chapter
        chp_link = contents[5].a['href']
        return chp_link

    def jjk_update(self):
        # open txt file in read
        # reads txt file contents
        with open("jjkchapter.txt", "r+") as txt:
            jjk_chapter = txt.read()
        # checks to see if chapter from scrape is different to saved
        jjk_string = self.jjk_chapter_check()
        if jjk_chapter != jjk_string:
            # chapter is different so rewrites file and constructs update message with link to new chapter
            with open("jjkchapter.txt", "w+") as txt:
                txt.write(jjk_string)
            jjk_link = self.jjk_link()
            ch_message = "New JJK chapter uploaded! {}".format(jjk_link)
            return ch_message
        else:
            # chapter is the same so will return nothing
            return ""

    def csm_chapter_check(self):
        # source url
        source = requests.get('https://www.readchainsawman.com/').text
        soup = BeautifulSoup(source, 'lxml')
        # loops through all fields with specified class
        contents = soup.find_all(class_="col-span-3")
        # newest_chp is the 2nd chapter in the list, aka latest uploaded/updated
        # newest_chp = contents[5]
        # chp_number is only the text portion showing chp number
        chp_number = contents[5].a.text
        return chp_number

    def csm_link(self):
        # source url
        source = requests.get('https://www.readchainsawman.com/').text
        soup = BeautifulSoup(source, 'lxml')
        # loops through all fields with specified class
        contents = soup.find_all(class_="col-span-3")
        # newest_chp is the 2nd chapter in the list, aka latest uploaded/updated
        # newest_chp = contents[5]
        # chp_link is hyperlink for new chapter
        chp_link = contents[5].a['href']
        return chp_link

    def csm_update(self):
        # open txt file in read
        # reads txt file contents
        with open("csmchapter.txt", "r+") as txt:
            csm_chapter = txt.read()
        # checks to see if chapter from scrape is different to saved
        csm_string = self.csm_chapter_check()
        if csm_chapter != csm_string:
            # chapter is different so rewrites file and constructs update message with link to new chapter
            with open("csmchapter.txt", "w+") as txt:
                txt.write(csm_string)
            csm_link = self.csm_link()
            ch_message = "New CSM chapter uploaded! {}".format(csm_link)
            return ch_message
        else:
            # chapter is the same so will return nothing
            return ""

    def snk_chapter_check(self):
        # source url
        source = requests.get('https://www.readsnk.com').text
        soup = BeautifulSoup(source, 'lxml')
        # loops through all fields with specified class
        contents = soup.find_all(class_="flex flex-col")
        # newest_chp is the 1st chapter in the list, aka latest uploaded/updated
        newest_chp = contents[0]
        # chp_number is only the text portion showing chp number
        chp_number = newest_chp
        return chp_number

    def snk_link(self):
        # source url
        source = requests.get('https://www.readsnk.com/').text
        soup = BeautifulSoup(source, 'lxml')
        # loops through all fields with specified class
        contents = soup.find_all(class_="flex flex-col")
        # newest_chp is the 1st chapter in the list, aka latest uploaded/updated
        # newest_chp = contents[0]
        # chp_link is hyperlink for new chapter
        chp_link = contents[0].a['href']
        return chp_link

    def snk_update(self):
        # open txt file in read
        # reads txt file contents
        with open("snkchapter.txt", "r+") as txt:
            snk_chapter = txt.read()
        # checks to see if chapter from scrape is different to saved
        snk_string = self.snk_chapter_check()
        if snk_chapter != snk_string:
            # chapter is different so rewrites file and constructs update message with link to new chapter
            with open("snkchapter.txt", "w+") as txt:
                txt.write(snk_string)
            snk_link = self.snk_link()
            ch_message = "New SnK chapter uploaded! {}".format(snk_link)
            return ch_message
        else:
            # chapter is the same so will return nothing
            return ""

    def sl_chapter_check(self):
        # source url
        source = requests.get('https://readsololeveling.org/').text
        soup = BeautifulSoup(source, 'lxml')
        # loops through all fields with specified class
        contents = soup.find_all(class_="flex flex-col")
        # newest_chp is the 2nd chapter in the list, aka latest uploaded/updated
        # newest_chp = contents[1]
        # chp_number is only the text portion showing chp number
        chp_number = contents[1].a.text
        return chp_number

    def sl_link(self):
        # source url
        source = requests.get('https://readsololeveling.org/').text
        soup = BeautifulSoup(source, 'lxml')
        # loops through all fields with specified class
        contents = soup.find_all(class_="flex flex-col")
        # newest_chp is the 2nd chapter in the list, aka latest uploaded/updated
        # newest_chp = contents[1]
        # chp_link is hyperlink for new chapter
        chp_link = contents[1].a['href']
        return chp_link

    def sl_update(self):
        # open txt file in read
        # reads txt file contents
        with open("slchapter.txt", "r+") as txt:
            sl_chapter = txt.read()
        # checks to see if chapter from scrape is different to saved
        sl_string = self.sl_chapter_check()
        if sl_chapter != sl_string:
            # chapter is different so rewrites file and constructs update message with link to new chapter
            with open("slchapter.txt", "w+") as txt:
                txt.write(sl_string)
            sl_link = self.sl_link()
            ch_message = "New Solo Leveling chapter uploaded! {}".format(sl_link)
            return ch_message
        else:
            # chapter is the same so will return nothing
            return ""
