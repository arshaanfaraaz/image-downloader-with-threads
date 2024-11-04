import threading
import requests
import uuid

class ImageDownloadByUrl(threading.Thread):
    def __init__(self, url):
        self.url = url
        threading.Thread.__init__(self)
        
    def run(self):
        image = requests.get(self.url).content
        image_name = f'images/{str(uuid.uuid4())}.jpg'
        with open(image_name, "wb") as image_file:
            image_file.write(image)
            print('Image Downloaded')
            



