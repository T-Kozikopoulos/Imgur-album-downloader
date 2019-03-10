import requests
from bs4 import BeautifulSoup
import urllib.request


# Files are saved in the script's directory.
def imgur_scraper(album_id):
    i = 1
    url = 'http://imgur.com/a/{}'.format(album_id)

    # Get the page's source code and create a soup object.
    code = requests.get(url)
    text = code.text
    soup = BeautifulSoup(text, "html.parser")
    
    # Grab all the images in the gallery
    for link in soup.findAll('div', {'class': 'post-image-container'}):
        href_temp = link.get('id')

        # Almost everything is .jpg, so you rarely need to change this. But if nothing happens when you run this,
        # then check the file type of one of the images(they'll all be the same) cause they might be PNGs.
        href = 'http://i.imgur.com/' + str(href_temp) + '.jpg'

        # Print the links as you download to make sure everything is running smoothly.
        print(href)

        # Save images as whatever you want, their original format doesn't really matter.
        fw = open('{}.png'.format('0{}'.format(str(i))), 'wb')
        fw.write(urllib.request.urlopen(href).read())
        fw.close()
        i += 1

# Call the function with just the album ID(last 5 characters of the URL).
imgur_scraper('4ov7Z')
