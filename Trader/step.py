import requests


def getter(name):
    text = ''
    while True:
        if text.startswith('We'):
            break
        else:
            res = requests.get(url='https://stepic.org/media/attachments/course67/3.6.3/' + name)
            print(name)
            print(res.url)
            text = res.text
            name = res.text

    print(text)
