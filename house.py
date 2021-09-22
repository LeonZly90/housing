import requests
from bs4 import BeautifulSoup
# 爬虫函数
def crawl(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    html = requests.get(url, headers=headers).text
    # lxml：html解析库（把HTML代码转化成Python对象）
    soup = BeautifulSoup(html, 'lxml')
    # print("豆瓣电影250：序号 \t 影片名 \t 评分 \t 评价人数")
    for tag in soup.find_all('div', 'property-wrap'):
        content = tag.get_text()
        content = content.replace('\n', '') # 删除多余换行
        print(content, '\n')
    # 主函数
if __name__=='__main__':
    # url = 'https://movie.douban.com/top250?format=text'
    url = 'https://www.maverickinvestorgroup.com/investment-properties'
    crawl(url)

# from urllib.request import Request, urlopen
# from bs4 import BeautifulSoup
# import urllib
# import requests
#
# # url = "https://www.noradarealestate.com/real-estate-investments/"
# url = 'https://www.maverickinvestorgroup.com/investment-properties'
# req = requests.get(url)
# soup = BeautifulSoup(req.text, 'html.parser')
# print(soup.title)
#
# span = soup.find_all('span', class_='cap')
# print(len(span))
# print(span) ##
# print(span[0])
# print(span[0].string)
# cap=[]
# for i in range(len(span)):
#     # print(i)
#     cap.append(span[i].string)
# print(cap)
#
#
# a= soup.find_all('span', class_='field-content')
# print(len(a))
# print(a)
#
# # for i in soup.find_all('span', {'class':'cap', 'class':'field-content'}):
# #     print('dadadada',i)
# items = soup.select('span.cap')+soup.select('span.field-content')
# print(items)


# price = div.span.text
# div.span.extract()
# title = div.get_text(strip=True)
# print(title)
# print(price)
# for link in soup.find_all('a'):
#     print(link.get('href'))
# # https://table.investments/what-we-do/buy/properties-for-sale/
#
# list1 = {'address': '2905 Mockingbird Lane Midwest City OK 73110',
#          'price': 193500,
#          'cap rate': 6.8,
#          'rent': 1725}
#
# list2 = {'address': '1433 Northeast 26th StreetOklahoma City, OK 73111',
#          'price': 92000,
#          'cap rate': 7.7,
#          'rent': 950}
#
# list3 = {'address': '1417 Shalimar Drive Del City, OK 73115',
#          'price': 102000,
#          'cap rate': 8,
#          'rent': 1065}
#
# list4 = {'address': '1104/1108 Tall Oaks Drive Midwest City, OK 73110',
#          'price': 152000,
#          'cap rate': 7,
#          'rent': 1450}
#
# import pandas as pd
#
#
# def calculation_rent():
#     house = pd.DataFrame([list1, list2, list3, list4])
#     # house = house.sort_values(['cap rate'], ascending=[False])
#     print(house, '\n')
#
#     price = house['price'].tolist()
#     # print('price', price)  # price [193500, 92000, 102000, 152000]
#     rent = house['rent'].tolist()
#     # print('rent', rent)  # rent [1725, 950, 1065, 1450]
#     caprate = house['cap rate'].tolist()
#     # print('cap rate', caprate)
#     budget = 300000
#     print('budget $%d' % budget)
#     dp = [[0 for i in range(budget + 1)] for x in range(len(price))]  # 4行budget列
#     # print(dp)
#     for i in range(len(price)):
#         for j in range(budget + 1):
#             if j < price[i]:
#                 dp[i][j] = dp[i - 1][j]  # 不放
#             else:
#                 dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - price[i]] + rent[i])
#     # print(dp)
#     print('*' * 60, '\n')
#     res = dp[-1][-1]
#     print('Profit:', res)
#     for i in range(len(rent), -1, -1):
#         # print('i', i)
#         if res == dp[i - 1][budget]:
#             continue
#         else:
#             price_include = price[i]
#             rent_include = rent[i]
#             # print('price_include', price_include, 'rent_include', rent_include)
#             res = res - rent_include
#             budget -= price[i]
#             # print('res', res, 'budget', budget)
#
#             list = house.iloc[i].tolist()
#             print(list)
#     print('Rest budget:', budget)
#
#
# print(calculation_rent())
# print('*' * 60, '\n')
#
# house = pd.DataFrame([list1, list2, list3, list4])
# house = house.sort_values(['cap rate'], ascending=[False]).reset_index(drop=True)
# print(house, '\n')
