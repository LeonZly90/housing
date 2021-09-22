import requests
from bs4 import BeautifulSoup


def crawl(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/83.0.4103.116 Safari/537.36 '
    }
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    # for tag in soup.find_all('div', 'col-md-4'):
    for tag in soup.find_all('div', 'col-md-4'):
        print(tag)
        name = tag.find_all('h4 class="card-title', 'title')
        # name = name[0].get_text()
        print('address', name)


if __name__ == '__main__':
    url = "https://www.noradarealestate.com/real-estate-investments/"
    crawl(url)
