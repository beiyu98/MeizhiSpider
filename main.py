from downloader import Meizhi
from parser import UrlParser

print('豆瓣小组帖子爬虫')
print('可下载发帖用户的头像，主页地址，名字，发帖图片')
print('-----------------------------------------------')
print('请输入小组的名字：')
group = input()
print('-----------------------------------------------')
print('请输入要下载的帖子数(25的整数倍)：')
count = input()
print('-----------------------------------------------')
root_url = "https://www.douban.com/group/" + group + "/discussion?start="
print('爬取的小组地址为', root_url)
print('-----------------------------------------------')

urls = set()
parser = UrlParser()
n = 0
while n < int(count):
    url = root_url + str(n)
    links = parser.get_new_urls(url)
    for link in links:
        urls.add(link)

    n += 25

meizhi_downloader = Meizhi()
meizhi_downloader.download(urls)
