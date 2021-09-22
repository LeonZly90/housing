import requests
from bs4 import BeautifulSoup
# 爬取详细信息
def getInfo(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    html = requests.get(url, headers=headers).text
    # lxml：html解析库（把HTML代码转化成Python对象）
    soup = BeautifulSoup(html, 'lxml')
    # 电影简介
    print('电影简介：')
    info = soup.find(attrs={'id': 'info'})
    print(info.get_text())
    other = soup.find(attrs={"class": "related-info"}).get_text()
    print(other.replace('\n', '').replace('', '')) # 过滤空格和换行
    # 评论
    print('评论信息：')
    for tag in soup.find_all(attrs={"id": "hot-comments"}):
        for comment in tag.find_all(attrs={"class": "comment-item"}):
            com = comment.find("p").get_text() # 爬取段落 p
            print(com.replace('\n', '').replace('', ''))
# 爬虫函数
def crawl(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    html = requests.get(url, headers=headers).text
    # lxml：html解析库（把HTML代码转化成Python对象）
    soup = BeautifulSoup(html, 'lxml')
    for tag in soup.find_all(attrs={"class": "item"}):
        # 爬取序号
        num = tag.find('em').get_text()
        print(num)
        # 电影名称
        name = tag.find_all(attrs={"class": "title"})
        zwname = name[0].get_text()
        print('[中文名称]', zwname)
        # 网页链接
        url_movie = tag.find(attrs={"class": "hd"}).a
        urls = url_movie.attrs['href']
        print('[网页链接]', urls)
        getInfo(urls)
# 主函数
if __name__=='__main__':
    i = 0
    while i < 1:
        print('页码：', i+1)
        num = i * 25 # 每次显示 25 部，URL 序号按 25 增加
        urls = 'https://movie.douban.com/top250?start=' + str(num) + '&filter='
        crawl(urls)
        i = i + 1