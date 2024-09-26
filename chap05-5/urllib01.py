import urllib.request

def get_wikidocs(page):
    resouce = 'https://wikidocs.net/{}'.format(page)
    with urllib.request.urlopen(resouce) as s:
        with open('wikidocs_%s.html' % page, 'wb') as f:
            f.write(s.read())

get_wikidocs(20)
