import os
import bs4
import requests
from sys import *

def folder_create(images):
    try:
        folder_name = input("Enter Folder Name :- ")
        os.mkdir(folder_name)
    except:
        print("Folder Exist with that Name !!!")
        folder_create()
    
    download_images(images, folder_name)

def download_images(images, folder_name):
    count = 0
    print(f"Total {len(images)} Image Found!")

    if len(images) != 0:
        for i, image in enumerate(images):
            try:
                image_link = image["data-srcset"]
            except:
                try:
                    image_link = image["data-fallback-src"]
                except:
                    try:
                        image_link = image["src"]
                    except:
                        pass
            try:
                r = requests.get(image_link).content
                try:
                    r = str(r, 'utf-8')
                except UnicodeDecodeError:
                    with open(f"{folder_name}/images{i+1}.jpg", "wb+")as f:
                        f.write(r)
                        count = count + 1
            except:
                pass
        if count == len(images):
            print("All Images Downloaded !")
        else:
            print(f"Total{count} Images Downloaded Out of {len(images)}")

def main():
    print("Web Scrapping Application to Download Images")
    print("Application  Name :"+argv[0])
    
    url = input("Enter URL from where you want to download images :- ")
    r = requests.get(url)

    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    images = soup.findAll('img')

    folder_create(images)

if __name__ == "__main__":
    main()