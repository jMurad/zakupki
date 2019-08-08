import requests
from bs4 import BeautifulSoup
import re


# результат поискового запроса
def get_html(url, ref=0):
    url = f'http://zakupki.gov.ru/epz/order/quicksearch/search.html?' \
          f'searchString={_searchString}&' \
          f'{_conformity}&' \   
    f'pageNumber={_pageNumber}&' \
        f'sortDirection={_sortDirection}&' \
        f'recordsPerPage=_{_recordsPerPage}&' \
        f'showLotsInfoHidden={_showLotsInfoHidden}&' \
        f'{_fz}' \
        f'{_etapzak}' \
        f'currencyId={_currencyId}&' \
        f'regionDeleted={_regionDeleted}&' \
        f'publishDateFrom={_publishDateFrom}&' \
        f'publishDateTo={_publishDateTo}&' \
        f'updateDateFrom={_updateDateFrom}&' \
        f'updateDateTo={_updateDateTo}&' \
        f'applSubmissionCloseDateFrom={_applSubmissionCloseDateFrom}&' \
        f'applSubmissionCloseDateTo={_applSubmissionCloseDateTo}&' \
        f'sortBy={_sortBy}'
    if ref:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/73.0.3683.86 Safari/537.36',
            'referer': 'http://zakupki.gov.ru/epz/main/public/home.html',
            'Upgrade-Insecure-Requests': '1',
            'DNT': '1'
        }
    else:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/73.0.3683.86 Safari/537.36',
            'Upgrade-Insecure-Requests': '1',
            'DNT': '1'
        }

    s = requests.Session()
    r = s.get(url, headers=headers)
    # r = requests.get(url)
    return r.text


# урлы всех страниц с сайта
def get_all_pages():
    total_pages = 100
    base_url = 'http://zakupki.gov.ru/epz/order/quicksearch/search.html?searchString=&morphology=on&'
    page_part = 'pageNumber='
    url_gen = []
    for i in range(1, total_pages):
        url_gen.append(base_url + page_part + str(i))
    return url_gen


def get_all_advert(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find_all('div', class_='registerBox')
    ad = []
    for i in range(0, len(ads)):
        # time.sleep(1)
        every_ad = ads[i]
        soup2 = BeautifulSoup(str(every_ad), 'lxml')
        test = soup2.select('div.reportBox li a')[1].attrs["href"]
        if 'http://' not in test:
            test = 'http://zakupki.gov.ru' + test
        docs_html = get_html(test)
        soup3 = BeautifulSoup(docs_html, 'lxml')
        idzakupki = soup3.find(text=re.compile(r' №\S{19}'))
        if idzakupki:
            idzakupki = idzakupki.strip().split(' ')[1]
        elem = soup3.find(text=re.compile(r'Протокол признания участника уклонившимся'))
        if elem:
            text = elem.parent.parent.parent.select('td')[1].select('div span')[1].text.strip()
            ad.append({'datetime': text, '#zakupka': idzakupki})
    return ad


def main():
    all_pages = get_all_pages()
    ads = []
    i = 0
    for page in all_pages:
        i += 1
        if i > 150:
            break
        ads.append(get_all_advert(page))
        print('next page')
    print(ads)


if __name__ == '__main__':
    main()
