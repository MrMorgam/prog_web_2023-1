import os
import requests
import shutil


def cls():
    os.system('clear')


def request_image(url):
    response = requests.get(url, stream=True)
    
    return response

 
def main():

    url = 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_light_color_272x92dp.png'
    file_name = 'image.jpg'

    response = request_image(url)

    cls()

    if response.status_code == 200:
    
        response.raw.decode_content = True
    
        with open(file_name,'wb') as f:
            shutil.copyfileobj(response.raw, f)
        
        print('Image sucessfully downloaded: ', file_name)
    else:
        print('Image couldn\'t be retreived')


if __name__ == "__main__":
    main()