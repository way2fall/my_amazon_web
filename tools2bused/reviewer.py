import requests
import json
from bs4 import BeautifulSoup
from multiprocessing import Pool
import threading
import time
from random import randint

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
           'X-Requested-With': 'XMLHttpRequest'}

cookies = {'cookie': 'x-wl-uid=1f9WKtJ8BLt9qIGl1uWajRkNdY8wII8sCL1p5lC9YeIHBPHoE5/7DApYGW8ds55+E6DZunnDoJCBE9UtrFrBQ7cCF0AdZGkEN3wqJLe0/'
                     'Z822892Uh2bGzVbD8UyJnmFMHSfv0i315+4=; x-main=3zhvHOaCF4DmGxmanJgAsxoLfSUa3uMxAiutLO1AgVNkCYbXw7uHeXZrdkvnLEY2; '
                     'at-main=Atza|IwEBIBBENb7160GcREcPbh-y_5i-Ay09waaJbaGMHBlZbnjVJfODCKvXdQ5ODwsZchFPlCyfLMVjdeY5Rxj0QiNOVbTLCoo3-V5Xkze'
                     '96QzHNFZy4xBXE_fVQMnYMwBPNVoy3RWUSyg1lGM-uXpBE73BOz0HE7DtQUKtAP0SVy-qgLGldJST0enYNQrbzpBz34ru17rymF92fiSIVq7d9Wj95nW7'
                     'RqbLSkGu21yNly8ljY68QtKzSMNt-PJARTqvzy5fUPTinttqOiRF7N1k_pypH3EeUyeyJmD0QZuLz4uFiiXfXfmVZezr9OlItJrHb-uvVvxpB6FTEtYXK0'
                     'IentqvxLLo; s_vnum=1892338774771%26vn%3D4; s_nr=1470214840186-Repeat; s_dslv=1470214840189; skin=noskin; session-token'
                     '="eFYr7yyEBJfPg52y3YQwS1aOHlxLjb0Q5wOAZZ7MZ45qa4XckK+p6q2J+/n2qqshcSOV05aI3XclS7aWI21W2s29mTXwuEg9X25BvAQvVmTskvkc21S2W'
                     'YON98LVZSm8655vg+b+rI/V11GUs45+IVas0C/Yxkwqse94fUNOSv2EdXzOnhA4KydjLFZcEvw5sD6jcqtnk1frSKpwGlxCiXUOnewoDATSXgBqzMBlf6lI'
                     'PNyUbB9C/Tox8ibxD4jBHYz/oOYVNB+koPFfCMVMNQ=="; csm-hit=NCQNB9E0FA29F51891FJ+s-NCQNB9E0FA29F51891FJ|1470375283872; sessi'
                     'on-id-time=2082787201l; session-id=188-5906807-8745549; ubid-main=178-8395338-6824722'}


def get_reviewer_email(reviewer_code):
    reviewer_url = 'https://www.amazon.com/gp/profile/{}/customer_email'.format(reviewer_code)
    time.sleep(randint(1, 10))
    r = requests.get(reviewer_url, headers=headers, cookies=cookies)
    try:
        info = json.loads(r.text)
        print(info['data']['email'])
    except ValueError:
        pass


def get_reviewer_code(page):
    reviewer_page = 'https://www.amazon.com/review/top-reviewers/ref=cm_cr_tr_link_2?ie=UTF8&page={}'.format(str(page))
    time.sleep(randint(1, 10))
    r = requests.get(reviewer_page, headers=headers, cookies=cookies)
    soup = BeautifulSoup(r.text, 'lxml')
    ids = ('reviewer'+str(i) for i in range(page*10-9, page*10+1))
    for i in ids:
        selector = '#{} > td > a'.format(i)
        info = soup.select(selector)[1].get('name')
        print(info)


if __name__ == '__main__':
    # threads = []
    # pages = [i for i in range(1, 11)]
    # for i in pages:
    #     t = threading.Thread(target=get_reviewer_code, args=(i,))
    #     threads.append(t)
    # for i in pages:
    #     threads[i-1].start()
    # for i in pages:
    #     threads[i-1].join()

    reviewer_codes = '''
    A12DQZKRKTNF5E
    A2KWFSBGBMTLOL
    A2NYK9KWFMJV4Y
    A1MC6BFHWY6WC3
    AO1Z0TQWCRGL4
    A26R7LLAFTPC3U
    A25C2M3QF9G7OQ
    A2SWGQVH78I33R
    A3HPCRD9RX351S
    A2DNZ0XS4QDO9N
    A1H4BDHFRBPRV9
    A3R1WFO4KIUQXZ
    A1WPFIZ8P3O86V
    A3S3R88HA0HZG3
    A1JZFGZEZVWQPY
    A16T2C41GZYAJZ
    A1TUL3FFHYEXBK
    A3SR3PZM0IQ6OR
    ABDR6IJ93HFIO
    A2BYV7S1QP2YIG
    A357B3PUHSVQA
    ASKZO80Z1RKTR
    A27H9DOUGY9FOS
    A1POFVVXUZR3IQ
    A1KYJA5YM1479G
    ASEBX8TBYWQWA
    A5VHX16RZ0KV5
    APRNS6DB68LLV
    A17HMM1M7T9PJ1
    A2AY4YUOX2N1BQ
    ALYZJ7W14YS26
    A14ZQ17DIPJ6UB
    A1E1LEVQ9VQNK
    A2D1LPEUCTNT8X
    A38RMU1Y5TDP9
    A1X1CEGHTHMBL1
    A2LXX47A0KMJVX
    A1IU7S4HCK1XK0
    AOEAD7DPLZE53
    AZKRFNQ8EFO4T
    A1MJFTAZUCGNYU
    A2MNB77YGJ3CN0
    AO9LDPUTA0919
    A27EE7X7L29UMU
    A4WEZJOIZIV4U
    A1PB2NV4HC72L4
    A2GJX2KCUSR0EI
    A1VGXHHR08G044
    A35Q0RBM3YNQNF
    A2UNWFVHL0JWBH
    A31N0XY2UTB25C
    A1HIVLFS0H3QG0
    AK7CAW3N1XZV6
    A17V9XL4CWTQ6G
    ACJT8MUC0LRF0
    A1LACH6MLQWZ
    A2VYLXYG3H6TYN
    A2MZZP3ZU9B5JS
    ARBKYIVNYWK3C
    A1BLC62SBF3PNQ
    A2W0GY64CJSV5D
    A3UIH7DCQRA21L
    A21OBYW0N5ENS7
    A25GROL6KJV3QG
    A2HC94KQKVGIA1
    A7EU2BWLLCJY2
    A202CZ4PJH83G4
    ADLVFFE4VBT8
    A10PEXB6XAQ5XF
    A2PNBB4GXRG14K
    A22CW0ZHY3NJH8
    A112RDNJQ0A72R
    A1UIMU8Q87ZPCH
    A2WW57XX2UVLM6
    A3V5F050GVZ56Q
    A32WT1ZEE4QGZB
    A3RR2P5IS3DGPR
    A1IGCUY11IG8I2
    A1F7YU6O5RU432
    A3L9FT8OJY4Q6I
    A5CDMTW6JKV5G
    A388KNV094E8C6
    A2OJW07GQRNJUT
    A3EXWV8FNSSFL6
    A3VVMIMMTYQV5F
    A23GFTVIETX7DS
    A1TPW86OHXTXFC
    A1VGHTDOZXOOYP
    A34VRVI4CSI5RQ
    A2XOOQ9N7OQVIA
    A8VI7KMUHI7ZH
    A328S9RN3U5M68
    A2IBCAV99XTMFK
    A28Q0JA9H8WZOD
    A1IJUCICSBF7LA
    A2PF64RBR1G1SZ
    A1GQAKL9CGQLP1
    AL38YB2PK4YPU
    A3SZGKK2BMNAQP
    A2E2Q4CNJ2NJAS
    '''
    codes = reviewer_codes.split()
    code_len = len(codes)
    threads = []
    for i in range(code_len):
        t = threading.Thread(target=get_reviewer_email, args=(codes[i],))
        threads.append(t)
    for i in range(code_len):
        threads[i].start()
    for i in range(code_len):
        threads[i].join()
