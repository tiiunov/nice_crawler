import re
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse, urljoin


class Networking:
    @staticmethod
    def get_html_text(url, params=None):
        html = requests.get(url, params=params)
        if html.status_code == 200:
            return html.content
        else:
            raise ConnectionError(f"something bad :( code {html.status_code}")

    def get_beautiful_html_text(self, url):
        soup = BeautifulSoup(self.get_html_text(url), "html.parser")
        return soup.prettify()

    def get_links(self, url):
        urls = set()
        soup = BeautifulSoup(self.get_html_text(url), "html.parser")
        for a_tag in soup.findAll("a"):
            href = a_tag.attrs.get("href")
            if href == "" or href is None:
                continue
            href = urljoin(url, href)
            parsed = urlparse(href)
            href = parsed.scheme + "://" + parsed.netloc + parsed.path
            if not self.right_url(href):
                continue
            urls.add(href)
        return urls

    @staticmethod
    def right_url(url):
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)

    @staticmethod
    def get_title(html_text):
        reg = re.compile('[^a-zA-Zа-яА-Я0-9._ ]')
        soup = BeautifulSoup(html_text, 'html.parser')
        title_all = soup.title
        if title_all is None:
            return None
        title = title_all.text
        title = reg.sub('', title)
        return title.strip()

    @staticmethod
    def get_bad_title(url):
        reg = re.compile('[^a-zA-Zа-яА-Я0-9._ ]')
        title = reg.sub('', url)
        return title.strip()

    def get_media_links(self, url):
        soup = BeautifulSoup(self.get_html_text(url), "html.parser")
        tags = soup.findAll('img')
        for t in tags:
            print(t)
