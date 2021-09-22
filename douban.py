import urllib.request
import re
import requests
from bs4 import BeautifulSoup
import codecs
# 爬虫函数
def crawl(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }

    html = requests.get(url, headers=headers).text
    # lxml：html解析库（把HTML代码转化成Python对象）
    soup = BeautifulSoup(html, 'lxml')
    infofile.write("")
    print('爬取豆瓣电影：\n')
    for tag in soup.find_all(attrs={"class": "item"}):
        # 爬取序号
        num = tag.find('em').get_text()
        print(num)
        infofile.write(num + "\r\n")
        # 电影名称
        name = tag.find_all(attrs={"class": "title"})
        zwname = name[0].get_text()
        print('[中文名称]', zwname)
        infofile.write("[中文名称]" + zwname + "\r\n")
        # 网页链接
        url_movie = tag.find(attrs={"class": "hd"}).a
        urls = url_movie.attrs['href']
        print('[网页链接]', urls)
        infofile.write("[网页链接]" + urls + "\r\n")
    # 爬取评分和评论数
        info = tag.find(attrs={"class": "star"}).get_text()
        info = info.replace('\n', '')
        info = info.lstrip()
        print('[评分评论]', info)
    # 获取评语
        info = tag.find(attrs={"class": "inq"})
        if (info):  # 避免没有影评时调用 get_text() 报错
            content = info.get_text()
            print('[影评]', content)
            infofile.write("[影评]" + content + "\r\n")
            print('')
    # 主函数
if __name__ == '__main__':
    infofile = codecs.open("Result_Douban.txt", 'a', 'utf-8')
    i = 0
    while i < 10:
        print('页码：', i + 1)
        num = i * 25  # 每次显示 25 部，URL 序号按 25 增加
        urls = 'https://movie.douban.com/top250?start=' + str(num) + '&filter='
        crawl(urls)
        infofile.write("\r\n\r\n")
        i = i + 1
    infofile.close()