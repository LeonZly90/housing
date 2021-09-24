# https://www.browserstack.com/guide/run-selenium-tests-using-selenium-chromedriver
# https://pythonhowtoprogram.com/how-to-scrape-javascript-websites-with-selenium-using-python-3/
# https://blog.csdn.net/weixin_39763293/article/details/110535093
# https://stackoverflow.com/questions/51743859/navigating-through-pagination-with-selenium-in-python #how many pages
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml

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

    WEBDRIVER_PATH = r'C:\Users\LZhang\Downloads\chromedriver_win32\chromedriver.exe'
    driver = webdriver.Chrome(WEBDRIVER_PATH)

    url = 'https://www.noradarealestate.com/real-estate-investments/'

    driver.get(url)
    print(driver.title)



    print(1)
    data1, get_address1, get_price1, get_cap1, get_rent1, get_noi1, get_rate1 = crawl(url)
    dic1 = {'address': get_address1, 'price': get_price1, 'cap': get_cap1, 'rent': get_rent1, 'noi': get_noi1, 'rate':get_rate1}
    df1 = pd.DataFrame(dic1)
    print(df1)
    # driver.implicitly_wait(10)
    actions = ActionChains(driver)

    page2 = driver.find_element_by_partial_link_text('next')
    actions.move_to_element(page2)
    actions.click(page2)
    print(2)

    ads = driver.find_elements_by_xpath('//*[@class="col-md-6"]')

    for ad in ads:
        # collect each video title
        # please note that the find_element_by_xpath under the video variable
        # title = ad.find_element_by_xpath('.//*[@id="video-title"]')
        # print the title collected
        print(ad.text)
    # data, get_address, get_price, get_cap, get_rent, get_noi, get_rate = crawl(url)
    # dic = {'address': get_address, 'price': get_price, 'cap': get_cap, 'rent': get_rent, 'noi': get_noi, 'rate':get_rate}
    # df = pd.DataFrame(dic)
    print('df')
    # # time.sleep(5)
    # page3 = driver.find_element_by_partial_link_text('next')
    # actions.move_to_element(page3)
    # actions.click(page3)
    # # time.sleep(5)
    # print(3)
    # data, get_address, get_price, get_cap, get_rent, get_noi, get_rate = crawl(url)
    # dic = {'address': get_address, 'price': get_price, 'cap': get_cap, 'rent': get_rent, 'noi': get_noi, 'rate':get_rate}
    # df = pd.DataFrame(dic)
    # print(df)
    # # driver.implicitly_wait(10)
    # # time.sleep(10)
    # page4 = driver.find_element_by_partial_link_text('next')
    # actions.move_to_element(page4)
    # actions.click(page4)
    # # time.sleep(5)
    # print(4)
    # data, get_address, get_price, get_cap, get_rent, get_noi, get_rate = crawl(url)
    # dic = {'address': get_address, 'price': get_price, 'cap': get_cap, 'rent': get_rent, 'noi': get_noi, 'rate':get_rate}
    # df = pd.DataFrame(dic)
    # print(df)

    actions.perform()

