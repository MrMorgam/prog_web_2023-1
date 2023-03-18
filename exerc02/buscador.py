import requests
import requests_cache
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

disable_warnings(InsecureRequestWarning)

requests_cache.install_cache('cache')


def get_soup(url):
    response = requests.get(url, verify=False)
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")

    return soup 


def count_word(word, text):
    text = text.lower()
    word = word.lower()

    word_count = text.count(word)

    return word_count


def excl_backscp(text):
    new_text = ''

    for i in range(0, len(text)-1):
        if text[i] != '\n' or text[i+1] != '\n':
            new_text += text[i]
            

    return new_text


def keyword_occurances(keyword, url):
    soup = get_soup(url)

    plain_text = soup.get_text()
    clean_text = excl_backscp(plain_text)
    keyword_count = count_word(keyword, clean_text)

    return keyword_count


def get_links(url):
    soup = get_soup(url)

    links = soup.find_all('a')
    
    urls = list()
    
    for link in links:
        if str(link.get('href')).startswith('http'):
            urls.append(link.get('href'))

    return urls


def search(url, keyword, depth):
    data = list()

    links = list()
    links.append(url)

    if depth > 0:
        links1 = get_links(url)

        for link in links1:
            if link not in links:
                links.append(link)

        if depth > 1:
            for link in links1:
                links2 = get_links(link)

                for link in links2:
                    link = link.lower()
                    if link not in links and 'localhost' not in link and 'wide.net' not in link:
                        links.append(link)

    for link in links:
            links_data = list()

            number_keywords = keyword_occurances(keyword, link)
            links_data.append(link)
            links_data.append(number_keywords)

            data.append(links_data)


    number_links = 0
    number_occurrences = 0

    for i in range(0, len(data)):
        print("Link: {}\nOcorrências: {}".format(data[i][0], data[i][1]))
        number_links += 1
        number_occurrences += int(data[i][1])
    


    print("\nTotal de links: {}".format(number_links))
    print("Total de ocorrências do termo '{}': {}". format(keyword, number_occurrences))


def main():
    keyword = 'estudo'
    url = 'https://www.bbc.com/portuguese'
    depth = 2

    search(url, keyword, depth)


if __name__ == '__main__':
    main()