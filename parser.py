import urllib.request

from bs4 import BeautifulSoup


class UrlParser:
    # 解析帖子链接
    def get_new_urls(self, page_url):
        response = urllib.request.urlopen(page_url)
        soup = BeautifulSoup(response.read(), 'html.parser', from_encoding='utf-8')
        links = soup.find_all('td', class_='title')
        new_urls = set()
        for link in links:
            new_url = link.find('a').get('href')
            print("解析到的帖子链接 ", new_url)
            new_urls.add(new_url)

        return new_urls
