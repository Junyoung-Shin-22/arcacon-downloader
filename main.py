import requests
import os
import bs4

import sys

url = sys.argv[1]

response = requests.get(url)
if response.status_code != 200:
    print('error loading page. exit.')
    exit()

html = response.text
soup = bs4.BeautifulSoup(html, features='html.parser')

wrapper = soup.select_one('div.emoticons-wrapper')
# print(wrapper)

imgs = wrapper.select('img.emoticon')
vids = wrapper.select('video.emoticon')
# print(len(imgs), len(vids))

p = url.split('/')[-1]
img_path = os.path.join(p, 'img')
vid_path = os.path.join(p, 'vid')
os.makedirs(img_path, exist_ok=True)
os.makedirs(vid_path, exist_ok=True)

for i, img in enumerate(imgs, 1):
    src = img['src']
    # print(src)
    res = requests.get('https:'+src)
    if res.status_code != 200:
        print('error downloading image. skipping...')
        continue
    con = res.content

    with open(os.path.join(img_path, f'{i}.webp'), 'wb') as f:
        f.write(con)

for i, vid in enumerate(vids, 1):
    src = vid['data-src']
    # print(src)
    res = requests.get('https:'+src)
    if res.status_code != 200:
        print('error downloading video. skipping...')
        continue
    con = res.content

    with open(os.path.join(vid_path, f'{i}.mp4'), 'wb') as f:
        f.write(con)
