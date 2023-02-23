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
    
    cleantext = BeautifulSoup(response.text, 'lxml').text

    cls()

    print(cleantext)


if __name__ == "__main__":
    main()