#! python3
# this software downloads images from a given url

# Import relevant modules
import requests, os, bs4

# Set important variables.
url = ''
os.chdir('C:\\Users\\User\\Desktop')

# Download the page.
response = requests.get(url)
response.raise_for_status()
content = bs4.BeautifulSoup(response.text)

# Find the URL of all images.
elem = content.select('img')
if elem == []:
    print('Could not find images.')
    
imgUrl = []
for i in range(len(elem)):
    imgUrl.append('http:' + elem[i].get('src'))
    if not imgUrl[i].startswith('http://'):
        continue        
    else:
        # Download the images.
        print('Downloading image #'+ str(i) +'. ' +imgUrl[i])
        res = requests.get(imgUrl[i])
        res.raise_for_status()
        # Save the images.
        image = open(os.path.join('dl', os.path.basename(imgUrl[i])), 'wb')
        for chunk in res.iter_content(100000):
            image.write(chunk)
        image.close()
print('Done.')
