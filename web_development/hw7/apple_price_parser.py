import requests
from bs4 import BeautifulSoup

from constants import PHONES_BASE_URL, APPLE_PRODUCER_PARAM


def get_product_items_price():
    r = requests.get(f'{PHONES_BASE_URL}/{APPLE_PRODUCER_PARAM}')
    soup = BeautifulSoup(r.text, 'html.parser')
    pagination_tag = soup.find('rz-paginator')
    page_count = int(pagination_tag.findChildren('li')[-1].text) if pagination_tag else 0

    # tiles = soup.find_all("rz-catalog-tile")
    #
    # for tile in tiles:
    #     print(tile)
    #
    # for tile in tiles:
    #     old_price_tag = tile.find(name='div', attrs={'class': 'goods-tile__price--old'})
    #     new_price_tag = tile.find(name='div', attrs={'class': 'goods-tile__price'})
    #
    #     old_price_value = int(old_price_tag.contents[0].strip().replace('\xa0', '')) if old_price_tag else None
    #     old_price_curr = old_price_tag.findChild(name='span', attrs={'class': 'currency'}).text.strip() if old_price_tag else None
    #     new_price_value = int(new_price_tag.findChild(name='span', attrs={'class':'goods-tile__price-value'}).contents[0].strip().replace('\xa0', '')) if new_price_tag else None
    #     new_price_curr = new_price_tag.findChild(name='span', attrs={'class': 'currency'}).text.strip() if new_price_tag else None
    #
    #     apple = {
    #         'product_id': tile.find(attrs={'class': 'g-id'}).text.strip(),
    #         'product_name': tile.find(attrs={'class': 'goods-tile__title'}).text.strip(),
    #         'product_status': tile.find(attrs={'class': 'goods-tile__availability'}).text.strip(),
    #         'product_price_old': old_price_value,
    #         'product_price_old_curr': old_price_curr,
    #         'product_price_new': new_price_value,
    #         'product_price_new_curr': new_price_curr,
    #     }
    #
    #     print(apple)
    #

    # urls = (
    #     [APPLE_PHONES_BASE_URL]
    #     if not page_count
    #     else [APPLE_PHONES_BASE_URL] + [f'{PHONES_BASE_URL}page={p};{APPLE_PRODUCER_PARAM}' for p in range(2, page_count + 1)]
    # )
