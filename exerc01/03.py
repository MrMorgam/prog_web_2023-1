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
    url = input("Digite um endereço de página web: ")
    r = request(url)

    tag = input('Digite a tag: ')
    html_text = BeautifulSoup(r.text, 'html.parser')
    cabecalho = html_text.find_all(tag)

    n = 0

    cls()

    for cabecalho in html_text.find_all(tag):
        n += 1
        print("Tag", tag, n, ": ", cabecalho)

    print("\nForam encontrados {} tags '{}' na página '{}'". format(n, tag, url))

if __name__ == "__main__":
    main()