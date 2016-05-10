"""
Create a piece of code that downloads an entire album from imgur. It should support multiple arguments. e.g.
imgurDownloader http://imgur.com/a/0NZBe http://imgur.com/a/OKduw
The url might get a bit redundant for large batch's, so consider leaving out the link, so one just needs to enter 0NZBe
OKduw ect. You can use a third party librarys.

Tip: every single image link in an album is listed in the source code.

Bonus points: You can enter the directory you would like to save the files but it's optional. Extra bonus points: if
you can change all the file-names into something readable, that's also customizable. For example if I wanted all my
images called wallpapers001, wallpapers_002, ect. I would just add wallpapers# as an argument.

thanks to koldof for this challenge!
"""

import imgurpython as ip
import urllib
import shutil
import os.path


def auth():
    with open('20120316C.txt', 'r') as f:
        data = f.read().split()
        client_id = data[0]
        client_secret = data[1]

    return ip.ImgurClient(client_id, client_secret)


def download_images_from_list(list_name):
    img_list = client.get_album_images(list_name)
    l = len(str(img_list.__len__()))
    print(l)

    print('Name prefix? (leave blank if not needed)')
    name = input('> ')

    offset = 0
    for n, img in enumerate(img_list):
        print(n, img)
        url = img.link
        ext = url[url.rfind('.'):]

        title = ''
        if name:
            while True:
                title = name + str(n + offset).zfill(l) + ext
                if os.path.isfile(title):
                    offset += 1
                    print('number already exists')
                else:
                    break
        else:
            title = url[url.rfind('/') + 1:]

        with urllib.request.urlopen(url) as response, open(title, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)

if __name__ == '__main__':
    client = auth()

    while True:
        gallery = input('gallery snippet: ')
        download_images_from_list(gallery)
