import re
import urllib.request as request
from datetime import datetime
from bs4 import BeautifulSoup

MTA_TURNSTILE_URL = "http://web.mta.info/developers/turnstile.html"
MTA_FILE_ROOT_URL = "http://web.mta.info/developers/"

def get_site():
    f = request.urlopen(MTA_TURNSTILE_URL)
    content = f.read()
    return content
    
def get_turnstile_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')
    turnstile_links = [(MTA_FILE_ROOT_URL + link['href']) for link in links if re.match('.*day.*20..', link.text)]
    return turnstile_links 

def get_links():
    return get_turnstile_links(get_site())
