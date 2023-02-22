import os
import requests


def cls():
    os.system('clear')


def request(url):
    response = requests.get(url, verify=False)
    
    return response


def main():

    url = 'https://www.google.com/search?q='
    search = input('Digite a pesquisa a ser feita: ')
    
    search = search.replace(' ', '+').casefold()

    full_url = url + search

    response = request(full_url)
    
    cls()
    
    print(response.text)


if __name__ == "__main__":
    main()