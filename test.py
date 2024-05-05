import requests
from bs4 import BeautifulSoup
import os
from tqdm import tqdm  # tqdmをインポート

def download_images(base_url, query, num_pages=1):
    if not os.path.exists('images'):
        os.makedirs('images')

    for page in tqdm(range(num_pages), desc="Downloading Images"):  # tqdmをforループに適用
        start = page * 20 + 1
        url = base_url % query
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        images = soup.find_all('img')

        for i, img in enumerate(images):
            img_url = img.get('src')
            if img_url:
                print(f'Trying to download image from {img_url}')  # どのURLからダウンロードを試みるか出力
                try:
                    img_data = requests.get(img_url).content
                    file_path = f'images/image_{start + i}.jpg'
                    with open(file_path, 'wb') as handler:
                        handler.write(img_data)
                    print(f'Successfully downloaded to {file_path}')  # ダウンロード成功時のメッセージ
                except Exception as e:
                    print(f'Error downloading {img_url}: {e}')  # エラー発生時のメッセージ

download_images("https://www.google.com/search?q=%s&tbm=isch", "99letters")

