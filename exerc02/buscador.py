import requests
import requests_cache
from bs4 import BeautifulSoup

requests_cache.install_cache('cache')

def find_word_in_text(word, text):
    text = text.lower()
    word = word.lower()

    index = text.find(word)

    if index != -1:
        start = max(0, index - 20)
        end = min(len(text), index + 20 + len(word))
        return text[start:end]
    else:
        return None
    
def count_word_in_text(word, text):
    text = text.lower()
    word = word.lower()

    word_count = text.count(word)

    return word_count

def excl_backscapes_from_text(text):
    new_text = ''

    for i in range(0, len(text)-1):
        if text[i] != '\n' or text[i+1] != '\n':
            new_text += text[i]
            

    return new_text


def search(keyword, url, depth):
    response = requests.get(url, verify=False)
    html_content = response.text

    soup = BeautifulSoup(html_content, "html.parser")
    plain_text = soup.get_text()

    clean_text = excl_backscapes_from_text(plain_text)
    
    return count_word_in_text(keyword, clean_text)


def main():
    keyword = 'reitor'
    url = 'http://ifpi.edu.br'
    depth = 1

    word_count = search(keyword, url, depth)

    

    if word_count > 0:
        print("O termo '{}' foi encontrado na página {} vezes".format(keyword, word_count))
        
    else:
        print("O termo '{}' não foi encontrada na página".format(keyword))


if __name__ == '__main__':
    main()