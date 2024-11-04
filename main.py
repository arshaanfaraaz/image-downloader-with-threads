import time
from ImageDownloaderStart import ImageDownloadByUrl
import os


start = time.perf_counter()

if not os.path.exists('images'):
    os.makedirs('images')
    



if __name__ == '__main__':
    
    urls = [
    'https://images.pexels.com/photos/247851/pexels-photo-247851.jpeg?auto=compress&cs=tinysrgb&w=1200',
    'https://images.pexels.com/photos/884788/pexels-photo-884788.jpeg?auto=compress&cs=tinysrgb&w=1200', 
    'https://images.pexels.com/photos/1906658/pexels-photo-1906658.jpeg?auto=compress&cs=tinysrgb&w=1200',
    'https://images.pexels.com/photos/709143/pexels-photo-709143.jpeg?auto=compress&cs=tinysrgb&w=1200',
    'https://images.pexels.com/photos/1323550/pexels-photo-1323550.jpeg?auto=compress&cs=tinysrgb&w=1200',
    'https://images.pexels.com/photos/1631677/pexels-photo-1631677.jpeg?auto=compress&cs=tinysrgb&w=800'
    ]
    

    
    threads = []
    for url in urls:
        thread = ImageDownloadByUrl(url)
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    
    finish = time.perf_counter()
    
    print(f'\nFinished in {round(finish - start, 2)}')







