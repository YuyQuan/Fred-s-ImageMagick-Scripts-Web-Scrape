import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from urllib.request import urlopen
import cgi

base = 'http://www.fmwconcepts.com/imagemagick/'

def sub(url):
    '''Call on subpages that you found and return a list of links that host the scripts'''
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    links = soup.find_all('a')
    ret = list()
    for link in links:
        res = str(link['href'])
        if "downloadcounter.php" in res:
            if res not in ret:
                ret.append(res)
            else:
                # I don't think this is ever the case, but just in case, don't return duplicates
                print('INFO: ' + str(url))
                print('Has multiple links to the same script')
    if len(ret) == 0:
        return None
    # `ret` elements look like: ../downloadcounter.php?scriptname=3Drotate_animate&dirname=3Drotate
    # so, split on '/' and get the "downloadcounter" part.
    # .split('/')[1] -> downloadcounter.php?scriptname=3Drotate_animate&dirname=3Drotate
    # Then, prefix the `base` url, so that we return a list that has elements that look like this
    # http://www.fmwconcepts.com/imagemagick/downloadcounter.php?scriptname=3Drotate_animate&dirname=3Drotate
    return [ base + str(x).split('/')[1] for x in ret]

def getLinks(url):
    '''Get all links on homepage that might contain scripts. Then, call sub() to get their links. Finally, download the scripts'''
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    links = soup.find_all('a')
    seen = set()
    for link in links:
        try:
            if (link['href'] != '#' and link['href'] != ''):
                res = str(link['href'])
                if res.startswith(base):
                    script = res.split('/')[4]
                    # ignore the index, 'Home Page'
                    if(script == 'index.php'):
                        continue
                    seen.add(script)
        except:
            pass
    # Uncomment these to verify the links you found
    # print(seen)
    # print(len(seen))
    for x in seen:
        get = sub(base + x + '/index.php')
        # we didn't find anything on this page...print url and continue
        if get is None:
            print('WARNING: ' + str(x))
            print('Did not find any links that contained a download script ("downloadcounter.php")')
            continue
        # some odd pages have multiple download scripts? So get them all
        # i.e. http://www.fmwconcepts.com/imagemagick/3Drotate/index.php
        for y in get:
            print('DOWNLOADING: ' + str(y))
            remotefile = urlopen(y)
            blah = remotefile.info()['Content-Disposition']
            value, params = cgi.parse_header(blah)
            filename = params["filename"]
            urlretrieve(y, filename)

getLinks('http://www.fmwconcepts.com/imagemagick/index.php')