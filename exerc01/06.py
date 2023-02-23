import os
import requests
from bs4 import BeautifulSoup


def cls():
    os.system('clear')


def request(url):
    request = requests.get(url, verify=False)

    return request

 
def main():
    url = 'https://ge.globo.com/futebol/brasileirao-serie-a'
    response = request(url)
    html_text = BeautifulSoup(response.text, 'html.parser')

    header = html_text.find_all(_class = 'tabela')

    n = 0
    
    cls()

    for header in html_text.find_all('a', href=True):
        n += 1
        print(header)


if __name__ == "__main__":
    main()