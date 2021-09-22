import requests
from bs4 import BeautifulSoup
import pandas as pd


def crawl(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/83.0.4103.116 Safari/537.36 '
    }
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    info = []
    for tag in soup.find_all('div', 'property-wrap'):
        get_address = tag.find_all('h2', 'property-title')[0].get_text().replace('\n', '')
        # print(get_address)

        get_price = tag.find_all('div', 'property-price')[0].get_text().replace('\n', '').replace('$', '').replace(',',
                                                                                                                   '')
        # print(get_price)

        get_cap = tag.find_all('div', 'property-cap')[0].get_text().replace('Cap Rate: ', '').replace('%', '')
        # print(get_cap)

        get_rent = tag.find_all('div', 'property-rent')[0].get_text().replace('Rent: ', '').replace(',', '')
        # print(get_rent)

        get_noi = tag.find_all('div', 'property-noi')[0].get_text().replace('Monthly NOI: $', '').replace(',', '')
        # print(get_noi)

        info.append({'address': get_address, 'price': get_price, 'cap': get_cap, 'rent': get_rent, 'noi': get_noi})
        # print(info)
    return info


def calculation_rent(house):
    house[['price', 'rent', 'noi']] = house[['price', 'rent', 'noi']].astype(int)
    house[['cap']] = house[['cap']].astype(float)
    house = house.sort_values(['cap'], ascending=[False]).reset_index(drop=True)
    print(house)
    price = house['price'].tolist()
    # print('price', price)
    capRate = house['cap'].tolist()
    # print('cap rate', capRate)
    rent = house['rent'].tolist()
    # print('rent', rent)
    noi = house['noi'].tolist()
    # print('noi', noi)

    budget = 300000
    print('budget $%d' % budget)
    dp = [[0 for i in range(budget + 1)] for x in range(len(price))]
    # print(dp)
    for i in range(len(price)):
        for j in range(budget + 1):
            if j < price[i]:
                dp[i][j] = dp[i - 1][j]  # 不放
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - price[i]] + noi[i])
    # print(dp)
    print('*' * 60, '\n')
    res = dp[-1][-1]
    print('Profit:', res)
    for i in range(len(noi), -1, -1):
        # print('i', i)
        if res <= 0:
            break
        if res == dp[i - 1][budget]:
            continue
        else:
            price_include = price[i]
            noi_include = noi[i]
            # print('price_include', price_include, 'noi_include', noi_include)
            res = res - noi[i]
            budget -= price[i]
            # print('res', res, 'budget', budget)

            list = house.iloc[i].tolist()
            print(list)
    print('Rest budget:', budget)
    return


if __name__ == '__main__':
    url = 'https://www.maverickinvestorgroup.com/investment-properties'
    info = crawl(url)
    house = pd.DataFrame(info)
    # print(house)
    print(calculation_rent(house))

    # print(calculation_rent())
    # print('*' * 60, '\n')
    #
    # house = pd.DataFrame([list1, list2, list3, list4])
    # house = house.sort_values(['cap rate'], ascending=[False]).reset_index(drop=True)
    # return (house, '\n')
