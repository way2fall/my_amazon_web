import requests
from bs4 import BeautifulSoup

px_url = 'http://proxy.ipcn.org/country/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'}
# r = requests.get(px_url, headers=headers)
# soup = BeautifulSoup(r.text, 'lxml')
# proxy_cand = soup.select('[border=1] > tr > td')
# ip_list = (str(i.get_text().strip()) for i in proxy_cand if str(i.get_text().strip()) != '')


ips = '''
36.250.69.4:80
58.18.50.10:3128
58.19.222.139:3128
58.59.68.91:9797
59.39.88.190:8080
59.127.154.78:80
60.191.153.12:3128
60.191.158.211:3128
60.191.160.20:3128
60.191.163.147:3128
60.191.164.226:3128
60.191.165.28:3128
60.191.165.100:3128
60.191.167.93:3128
60.191.174.227:3128
60.191.180.38:3128
60.194.100.51:80
61.53.65.54:3128
61.134.34.148:3128
61.150.89.67:3128
61.158.173.14:8080
61.160.212.74:3128
61.162.223.41:9797
61.163.32.6:3128
61.163.59.65:3128
61.174.10.22:8080
61.175.220.4:3128
61.175.222.179:3128
101.251.199.66:3128
106.38.251.62:8088
111.206.81.248:80
112.90.72.83:80
112.91.208.78:9999
112.101.80.171:9797
112.112.70.115:80
112.112.70.116:80
113.107.57.76:80
113.107.57.76:8101
113.108.141.98:9797
115.25.138.245:3128
116.236.196.136:80
117.36.197.152:3128
118.26.226.157:3128
118.126.142.209:3128
118.144.104.254:3128
118.144.151.145:3128
118.144.156.2:3128
118.144.176.6:3128
118.144.213.85:3128
118.244.239.2:3128
119.6.136.122:80
119.147.86.212:9090
119.188.94.145:80
119.255.9.93:80
120.25.226.76:8080
120.52.72.20:80
120.52.72.21:80
120.52.72.23:80
120.52.72.24:80
120.52.72.47:80
120.52.72.48:80
120.52.72.52:80
120.52.72.53:80
120.52.72.54:80
120.52.72.55:80
120.52.72.56:80
120.52.72.58:80
120.52.72.59:80
120.52.73.24:80
120.52.73.25:80
120.52.73.25:8080
120.52.73.26:80
120.52.73.26:8081
120.52.73.27:80
120.52.73.28:80
120.52.73.29:8080
120.52.73.30:80
120.52.73.31:80
120.52.73.31:8080
120.52.73.31:8081
120.52.73.32:8080
120.52.73.33:80
120.52.73.34:8080
120.192.92.99:80
120.194.18.90:81
121.8.170.53:9797
121.41.110.73:8080
122.72.18.160:80
122.96.59.102:80
122.96.59.102:82
122.96.59.102:83
122.96.59.105:80
122.96.59.105:81
122.96.59.105:82
122.96.59.105:83
122.96.59.105:843
122.96.59.106:80
122.96.59.106:81
122.96.59.106:82
122.96.59.106:83
122.146.176.41:8080
122.224.209.98:3128
122.226.62.90:3128
122.226.128.251:3128
122.226.132.139:3128
122.226.141.67:3128
122.226.203.70:3128
123.56.28.196:8888
123.65.217.151:9797
123.139.59.242:9999
123.146.128.15:3128
123.157.99.139:3128
124.42.7.103:80
124.88.67.30:80
124.202.180.6:8118
124.206.56.125:3128
124.206.133.227:80
124.206.164.180:3128
124.206.167.250:3128
124.206.186.161:3128
124.207.132.242:3128
124.244.77.129:80
125.217.199.148:8197
134.196.214.127:3128
183.61.236.53:3128
183.61.236.55:3128
183.62.9.84:8080
183.62.58.250:9797
183.131.151.208:80
183.239.167.122:8080
202.100.167.142:80
202.100.167.144:80
202.100.167.145:80
202.100.167.149:80
202.100.167.159:80
202.100.167.160:80
202.100.167.180:80
202.100.167.182:80
202.105.179.164:3128
202.106.16.36:3128
202.107.238.51:3128
203.88.170.183:8080
218.7.170.190:3128
218.10.97.115:3128
218.26.237.18:3128
218.28.218.193:3128
218.29.237.206:3128
218.77.83.89:3128
218.90.174.167:3128
218.95.84.54:3128
'''
ip_list = ips.split()


def validate_ip_address(ip):
    validate_url = 'http://lwons.com/wx'
    proxies = {'http': 'http://' + ip}
    try:
        r = requests.get(validate_url, proxies=proxies, headers=headers)
        if r.text == 'default':
            return ip
    except Exception:
        print('bad ip:', ip)
        return None

for i in ip_list:
    validate_ip_address(i)