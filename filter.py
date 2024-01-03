import os
import numpy as np
import PIL.Image as Image

imgs_path = './image'

img_list = os.listdir(imgs_path)
for img_name in img_list:
    img = Image.open(os.path.join(imgs_path, img_name))
    img = np.array(img)
    if min(img.shape[:2]) < 480:
        os.remove(os.path.join(imgs_path, img_name))
