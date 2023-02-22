import os
import requests
from bs4 import BeautifulSoup


def cls():
    os.system('clear')


def request(url):
    response = requests.get(url, verify=False)

    return response

   
def main():
    url = input("Digite um endereço de página web: ")
    response = request(url)

    tag = input('Digite a tag: ')
    html_text = BeautifulSoup(response.text, 'html.parser')
    header = html_text.find_all(tag)

    n = 0

    cls()

    for header in html_text.find_all(tag):
        n += 1
        print("Tag", tag, n, ": ", header)

    print("\nForam encontrados {} tags '{}' na página '{}'". format(n, tag, url))


if __name__ == "__main__":
    main()