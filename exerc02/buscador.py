import requests
import requests_cache
from bs4 import BeautifulSoup

def find_word_in_text(word, text):
    return word.lower() in text.lower()
    

def search(keyword, site_url, depth):
    requests_cache.install_cache('banco')
    response = requests.get(site_url, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    clean_text = BeautifulSoup(soup.text, 'lxml').text
    
    return find_word_in_text(keyword, clean_text)


def main():
    keyword = input("Digite a palavra-chave a ser buscada: ")
    site_url = input("Digite a url do site: ")
    #depth = int(input("Digite a profundidade da busca: "))

    word_is_found = search(keyword, site_url, 1)

    if word_is_found:
        print("A palavra '{}' foi encontrada na página".format(keyword))
    else:
        print("A palavra '{}' não foi encontrada na página".format(keyword))


if __name__ == '__main__':
    main()