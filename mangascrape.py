from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Scrape:
    def __init__(self):
        with open("manga.json") as local_manga_file:
            self.manga = json.load(local_manga_file)
        options = Options()
        options.headless = True
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")
        self.driver = webdriver.Chrome(options=options, executable_path='chromedriver.exe')

    def manga_info(self, id):  # get newest ch and ch link for a manga id in our json file
        xml_link = self.manga[id]["source"]
        self.driver.get(xml_link)
        xml = self.driver.page_source
        soup = BeautifulSoup(xml, 'lxml')
        l_soup = BeautifulSoup(xml, features='xml')
        titles = soup.find_all('title')
        new_ch = titles[2].text
        links = l_soup.find_all('link')
        ch_link = links[3].text
        return new_ch, ch_link

    def new_ch_check(self):  # iterates over manga.json and checks if any have new chapters
        _manga = []
        for manga_id in self.manga:
            print(f"checking manga {manga_id}")
            if manga_id != "info":
                _manga_info = self.manga[manga_id]
                new_ch, ch_link = self.manga_info(manga_id)
                desc = self.manga['info']['default_desc'].replace("%title%", _manga_info['title'])
                if "desc" in _manga_info:
                    desc = _manga_info['desc']
                if "local_ch" in _manga_info:
                    if new_ch != _manga_info["local_ch"]:
                        print(f"{_manga_info['title']} is not up to date! updating...")
                        if "ignore" in _manga_info:
                            if not _manga_info["ignore"]:
                                _manga.append({"ch": new_ch, "link": ch_link, "desc": desc, "thumbnail": _manga_info["thumbnail"]})
                        else:
                            _manga.append(
                                {"ch": new_ch, "link": ch_link, "desc": desc, "thumbnail": _manga_info["thumbnail"]})
                    else:
                        print(f"{_manga_info['title']} is up to date")
                else:
                    print(f"{_manga_info['title']} has never been scraped, syncing its chapter count to current")
                self.update_local_ch(manga_id, new_ch)
        return _manga

    def save_manga_info(self):  # updates local json file to whatever self.manga is now (should only ever be ch update)
        with open("manga.json", "w") as local_manga_file:
            json.dump(self.manga, local_manga_file, indent=2)

    def update_local_ch(self, id, ch):  # update a ch value in self.manga to reflect an updated manga, then save the file
        self.manga[id]["local_ch"] = ch
        self.save_manga_info()
