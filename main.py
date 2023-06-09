
import requests
import threading
import concurrent.futures
import time
from PIL import Image, ImageFilter
import glob
import cv2
import os

image_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

start = time.perf_counter()
size = (1200, 1200)

def open_image(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images


def download_image(image_url):
    image_byte = requests.get(image_url).content
    image_name = image_url.split("/")[3]
    image_name = f"{image_name}.jpg"
    with open(image_name, "wb") as image_file:
        image_file.write(image_byte)
        print(f"{image_name} was downloaded...")
     


def process_image(image):
    img = Image.open(image)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size) 
    img.save(f"processed/{image}")
    print(f'{image} was processed...')

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as executor:
     executor.map(download_image, image_urls)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_image , open_image("\PhotoDownloadThreading"))
    finish = time.perf_counter()

    print(f'\nfinished in {round(finish - start, 2)} seconds')
          



