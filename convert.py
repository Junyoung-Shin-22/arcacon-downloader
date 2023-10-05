import cv2 as cv
import imageio
import os
import sys

path = sys.argv[1]

img_path = os.path.join(path, 'img')
vid_path = os.path.join(path, 'vid')
png_path = os.path.join(path, 'png')
gif_path = os.path.join(path, 'gif')

os.makedirs(png_path, exist_ok=True)
os.makedirs(gif_path, exist_ok=True)

for i in os.listdir(img_path):
    name = i.split('.')[0]
    img = cv.imread(os.path.join(img_path, i), cv.IMREAD_UNCHANGED)
    cv.imwrite(os.path.join(png_path, f'{name}.png'), img)

for i in os.listdir(vid_path):
    name = i.split('.')[0]
    
    cap = cv.VideoCapture(os.path.join(vid_path, i))
    fps = cap.get(cv.CAP_PROP_FPS)

    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame[:,:,::-1]) # BGR -> RGB
    
    imageio.mimsave(os.path.join(gif_path, f'{name}.gif'), frames, fps=fps, loop=0)