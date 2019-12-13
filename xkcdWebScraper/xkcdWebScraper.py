# Downloads all of the XKCD web comics with multi threading
# original thoughts based on
# automate the boring stuff with python. Program created by Mark Foos

import requests, os, bs4, threading

url = 'https://xkcd.com'
os.makedirs('XKCD', exist_ok=True)
def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):

    # Downloads the page
        print('Downloading page https://xkcd.com/%s/...' % (urlNumber))
        res = requests.get('https://xkcd.com/%s/' % (urlNumber))
        res.raise_for_status()
        print("passed raised for status")
        soup = bs4.BeautifulSoup(res.text, features = "html.parser")
        print(soup)
    # Find the url of the comic image
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image')
        else:
            comicUrl = comicElem[0].get('src')

    # Download the image
            print("Downloading image %s... " % (comicUrl))
            res = requests.get("https:" + comicUrl)
            res.raise_for_status()

    # save the image to /XKCD
            imageFile = open(os.path.join('XKCD', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

    #get the prev buttons url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
    print('done')

downloadThreads = []
for i in range(0, 2200, 100):
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

for downloadThread in downloadThreads:
    downloadThread.join()
print("DONE!")
