import requests
from bs4 import BeautifulSoup


URL = 'https://www.kivano.kg/mobilnye-telefony'
HEADERS = {
    "user-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15',
    "accept": '*/*',
}

LINK = "https://kivano.kg"


def get_html(headers, url, params=None):
    response = requests.get(url, params=params, headers=headers)
    return response


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='item product_listbox oh')
    phones = []
    for i in items:
        phones.append({
            "title": i.find('strong').get_text(),
            'image': LINK + i.find('img').get('src')
        })
    print(items)


def get_parse_result():
    html = get_html(url=URL, headers=HEADERS)
    # print(html.text)
    get_content(html.text)


get_parse_result()
