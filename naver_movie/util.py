from bs4 import BeautifulSoup
import urllib.request


def text_normalize(text):
    return text.strip()


def get_soup(target_url):
    html = urllib.request.urlopen(target_url).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup
