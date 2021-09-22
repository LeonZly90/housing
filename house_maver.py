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


def calculation_noi(budget, house):
    house[['price', 'rent', 'noi']] = house[['price', 'rent', 'noi']].astype(int)
    house[['cap']] = house[['cap']].astype(float)
    # house = house[house['price'] <= budget]
    # house = house.sort_values(['cap'], ascending=[False]).reset_index(drop=True)
    print(house)
    price = house['price'].tolist()
    # print('price', price)
    capRate = house['cap'].tolist()
    # print('cap rate', capRate)
    rent = house['rent'].tolist()
    # print('rent', rent)
    noi = house['noi'].tolist()
    # print('noi', noi)

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
    res_noi = dp[-1][-1]
    print('res_noi:', res_noi)  # 2113

    for i in range(len(noi), -1, -1):
        if res_noi == dp[i - 1][budget]:
            continue
        else:
            price_include = price[i]
            noi_include = noi[i]
            # print('price_include', price_include, 'noi_include', noi_include)
            res_noi = res_noi - noi[i]
            budget -= price[i]
            # print('res_noi', res_noi, 'budget', budget)

            list = house.iloc[i].tolist()
            print(list, '\n')
    # print('Rest budget:', budget)
    return budget

def calculation_rent(budget, house):
    house[['price', 'rent', 'noi']] = house[['price', 'rent', 'noi']].astype(int)
    house[['cap']] = house[['cap']].astype(float)
    # house = house[house['price'] <= budget]
    # house = house.sort_values(['cap'], ascending=[False]).reset_index(drop=True)
    # print(house)
    price = house['price'].tolist()
    # print('price', price)
    capRate = house['cap'].tolist()
    # print('cap rate', capRate)
    rent = house['rent'].tolist()
    # print('rent', rent)
    noi = house['noi'].tolist()
    # print('noi', noi)

    # print('budget $%d' % budget)
    dp = [[0 for i in range(budget + 1)] for x in range(len(price))]
    # print(dp)
    for i in range(len(price)):
        for j in range(budget + 1):
            if j < price[i]:
                dp[i][j] = dp[i - 1][j]  # 不放
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - price[i]] + rent[i])
    # print(dp)
    print('*' * 60, '\n')
    res_rent = dp[-1][-1]
    print('res_rent:', res_rent)  # 2113

    for i in range(len(rent), -1, -1):
        if res_rent == dp[i - 1][budget]:
            continue
        else:
            price_include = price[i]
            rent_include = rent[i]
            # print('price_include', price_include, 'rent_include', rent_include)
            res_rent = res_rent - rent[i]
            budget -= price[i]
            # print('res_rent', res_rent, 'budget', budget)

            list = house.iloc[i].tolist()
            print(list, '\n')
    # print('Rest budget:', budget)
    return budget

if __name__ == '__main__':
    budget = 300000
    url = 'https://www.maverickinvestorgroup.com/investment-properties'
    info = crawl(url)
    house = pd.DataFrame(info)
    house[['price', 'rent', 'noi']] = house[['price', 'rent', 'noi']].astype(int)
    house[['cap']] = house[['cap']].astype(float)
    # print(house)
    print('Rest budget:', calculation_noi(budget, house))

    print('*' * 60, '\n')
    print('Rest budget:', calculation_rent(budget, house))

    print('*' * 60, '\n')
    print('Based on cap rate:')
    house = house[house['price'] <= budget]
    house_cap = house.sort_values(['cap'], ascending=[False]).reset_index(drop=True)
    print(house_cap.head())
