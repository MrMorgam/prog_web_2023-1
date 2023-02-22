import os
import requests
from bs4 import BeautifulSoup


def cls():
    os.system('clear')


def request(url):
    response = requests.get(url, verify=False)

    return response


def main():
    url = 'https://ifpi.edu.br'
    response = request(url)

    html_text = BeautifulSoup(response.text, 'html.parser')
    header = html_text.find_all('a', href=True)

    n = 0
    
    cls()

    for header in html_text.find_all('a', href=True):
        n += 1
        print("Link", n, ": ", header['href'],)

    print("\nForam encontrados {} links na página {}{}{}". format(n, "'", url,"'"))


if __name__ == "__main__":
    main()