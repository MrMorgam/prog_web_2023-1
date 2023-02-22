import os
import requests
import requests_cache
from bs4 import BeautifulSoup

def cls():
    os.system('clear')

def request(url):
    r = requests.get(url, verify=False)

    return r

def main():
    url = 'https://ifpi.edu.br'
    r = request(url)

    html_text = BeautifulSoup(r.text, 'html.parser')
    cabecalho = html_text.find_all('a', href=True)

    n = 0
    
    cls()

    for cabecalho in html_text.find_all('a', href=True):
        n += 1
        print("Link", n, ": ", cabecalho['href'],)

    print("\nForam encontrados {} links na página {}{}{}". format(n, "'", url,"'"))

if __name__ == "__main__":
    main()