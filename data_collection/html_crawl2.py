from bs4 import BeautifulSoup
import requests

def extract_spirit_data_page(base_url, spirits_url):
    spirit_data = []
    parsed = requests.get(spirits_url)
    if parsed.status_code != 200:
        return None

    soup = BeautifulSoup(parsed.content, 'html.parser')
    spirits = soup.find_all('div', class_='productHeader headlineList')

    for spirit in spirits:
        anchor_tag = spirit.find('a')
        link = anchor_tag.get('href')

        try:
            table_data = extract_spirit_table(base_url + link)
            spirit_data.append(table_data)
        except (AttributeError, TypeError):
            continue

    return spirit_data

def extract_spirit_table(spirit_link):
    parsed = requests.get(spirit_link)
    soup = BeautifulSoup(parsed.content, 'html.parser')
    spec_table = soup.find(id='ctl00_ContentRegion_ctl00_tblSpec')
    price = soup.find('div', class_='priceStor')['content']

    keys = [row.string for row in spec_table.find_all('td', class_='dtifSpecName')]
    values = [row.string for row in spec_table.find_all('td', class_='dtifSpecInfo')]
    res = dict(zip(keys, values))
    res['price'] = price

    return res

def extract_data(base_url, spirits_url, index, data):
    new_data = extract_spirit_data_page(base_url, spirits_url + str(index))

    if new_data is None:
        return data
    else:
        data += new_data
        extract_data(base_url, spirits_url, index+1, data)

    return data
