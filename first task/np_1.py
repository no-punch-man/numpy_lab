import numpy as np
from PIL import Image

def change_lunar(img):
    data = np.array(img)
    updated_data = (data - data.min())*(254/(np.unique(data).size))
    res_img = Image.fromarray(updated_data)
    if res_img.mode != 'RGB':
        res_img = res_img.convert('RGB')
    return res_img

img1 = Image.open(r'sources\lunar01_raw.jpg')
img2 = Image.open(r'sources\lunar02_raw.jpg')
img3 = Image.open(r'sources\lunar03_raw.jpg')

change_lunar(img1).save(r'first task\np001.jpg')
change_lunar(img2).save(r'first task\np002.jpg')
change_lunar(img3).save(r'first task\np003.jpg')
