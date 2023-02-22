import os
import requests


def cls():
    os.system('clear')


def request(url):
    response = requests.get(url, verify=False)
    
    return response


def main():
    cep = int(input('Digite o cep (sem traço): '))
    url = 'https://viacep.com.br/ws/{}/json/'.format(cep)

    print(url)

    response = request(url)
    
    cls()

    print("Resultado da busca:\n")
    print(response.text)


if __name__ == "__main__":
    main()