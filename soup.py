import requests
from bs4 import BeautifulSoup

class Soup(object):
    def __init__(self, url:str, append_mark:str, func):
        self.url = url
        self.links = []
        self.append_mark =append_mark
        self.func = func
    
    def get_links(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        for link in soup.find_all('a'):
            if self.is_appended(link.get('href')):
                self.links.append(link.get('href'))
        return self.links

    def is_appended(self, url:str):
        if self.append_mark == '' or self.append_mark in url:
            return True
        else:
            return False


if __name__ == '__main__':
    release = Soup('https://www.3gpp.org/ftp/Specs/2023-03/Rel-16', 'series', None)
    links = release.get_links()
    for link in links:
        ts_series = Soup(link, 'zip', None)
        print(ts_series.get_links())
        break

