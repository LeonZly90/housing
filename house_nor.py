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
    get_address = [tag.get_text() for tag in soup.find_all('h4', 'card-title')]
    print(get_address)

    data, get_price, get_cap, get_rent, get_noi, get_rate = [], [], [], [], [], []
    for tag in soup.find_all('div', 'col-md-6'):
        data.append([tag.get_text().replace('\n', '')])
    # print(data)
    # print(len(data))
    for i in range(len(data)):
        if 'Purchase Price:' in data[i][0]:
            get_price.append(data[i][0].replace('Purchase Price:$', ''))
        if 'Cap Rates:' in data[i][0]:
            get_cap.append(data[i][0].replace('Cap Rates:', '').replace('%', ''))
        if 'Rental Income:' in data[i][0]:
            get_rent.append(data[i][0].replace('Rental Income:$', ''))
        if 'Cash Flow (NOI):' in data[i][0]:
            get_noi.append(data[i][0].replace('Cash Flow (NOI):$', ''))
        if 'Neighborhood:' in data[i][0]:
            get_rate.append(data[i][0].replace('Neighborhood:', ''))
    print(get_price)
    print(get_cap)
    print(get_rent)
    print(get_noi)
    print(get_rate)
    return data, get_address, get_price, get_cap, get_rent, get_noi, get_rate


if __name__ == '__main__':
    url = "https://www.noradarealestate.com/real-estate-investments/"
    data, get_address, get_price, get_cap, get_rent, get_noi, get_rate = crawl(url)
    dic = {'address': get_address, 'price': get_price, 'cap': get_cap, 'rent': get_rent, 'noi': get_noi, 'rate':get_rate}
    df = pd.DataFrame(dic)
    print(df)
