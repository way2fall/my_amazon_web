import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'}

cookies = {
    'cookie': 'x-wl-uid=1f9WKtJ8BLt9qIGl1uWajRkNdY8wII8sCL1p5lC9YeIHBPHoE5/7DApYGW8ds55+E6DZunnDoJCBE9UtrFrBQ7cCF0AdZGkEN3wqJLe0/'
              'Z822892Uh2bGzVbD8UyJnmFMHSfv0i315+4=; x-main=3zhvHOaCF4DmGxmanJgAsxoLfSUa3uMxAiutLO1AgVNkCYbXw7uHeXZrdkvnLEY2; '
              'at-main=Atza|IwEBIBBENb7160GcREcPbh-y_5i-Ay09waaJbaGMHBlZbnjVJfODCKvXdQ5ODwsZchFPlCyfLMVjdeY5Rxj0QiNOVbTLCoo3-V5Xkze'
              '96QzHNFZy4xBXE_fVQMnYMwBPNVoy3RWUSyg1lGM-uXpBE73BOz0HE7DtQUKtAP0SVy-qgLGldJST0enYNQrbzpBz34ru17rymF92fiSIVq7d9Wj95nW7'
              'RqbLSkGu21yNly8ljY68QtKzSMNt-PJARTqvzy5fUPTinttqOiRF7N1k_pypH3EeUyeyJmD0QZuLz4uFiiXfXfmVZezr9OlItJrHb-uvVvxpB6FTEtYXK0'
              'IentqvxLLo; s_vnum=1892338774771%26vn%3D4; s_nr=1470214840186-Repeat; s_dslv=1470214840189; skin=noskin; session-token'
              '="eFYr7yyEBJfPg52y3YQwS1aOHlxLjb0Q5wOAZZ7MZ45qa4XckK+p6q2J+/n2qqshcSOV05aI3XclS7aWI21W2s29mTXwuEg9X25BvAQvVmTskvkc21S2W'
              'YON98LVZSm8655vg+b+rI/V11GUs45+IVas0C/Yxkwqse94fUNOSv2EdXzOnhA4KydjLFZcEvw5sD6jcqtnk1frSKpwGlxCiXUOnewoDATSXgBqzMBlf6lI'
              'PNyUbB9C/Tox8ibxD4jBHYz/oOYVNB+koPFfCMVMNQ=="; csm-hit=NCQNB9E0FA29F51891FJ+s-NCQNB9E0FA29F51891FJ|1470375283872; sessi'
              'on-id-time=2082787201l; session-id=188-5906807-8745549; ubid-main=178-8395338-6824722'}
pages = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def get_brands():
    url = 'https://www.amazon.com/gp/search/other/ref=sr_in_r_-2?rh=i%3Afashion-womens-jewelry%2Cn%3A7141123011%2Cn%3A7147440011%2Cn%3A7192394011&bbn=7192394011&pickerToList=lbr_brands_browse-bin&indexField={}&ie=UTF8&qid=1470827347'
    for i in pages:
        r = requests.get(url.format(i), headers=headers, cookies=cookies)
        soup = BeautifulSoup(r.text, 'lxml')
        inside = soup.select('#ref_2528832011 > ul > li > span > a > span.refinementLink')
        with open('brands.txt', 'a', encoding='utf-8') as br:
            for j in inside:
                br.write(j.get_text()+'\n')

get_brands()