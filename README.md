# ventibot
multi function discord bot for The Hole

## Requirements
Required python libraries can be installed with `pip install -r requirements.txt`. This project uses selenium for web scraping to avoid bot detection, 
so you will need a compatible web driver. I used Chrome's most recent stable release (92 as of writing this) and its respective driver, 
found here: https://sites.google.com/a/chromium.org/chromedriver/downloads. You can unzip chromedriver.exe into the main directory for the project to work 
or you can edit `executable_path` in `__init__` of `mangascrape.py` to the path of your webdriver.
