import numpy as np
from PIL import Image

def change_lunar(img):
    data = np.array(img)
    updated_data = (data - data.min())*(254/(np.unique(data).size))
    res_img = Image.fromarray(updated_data)
    if res_img.mode != 'RGB':
        res_img = res_img.convert('RGB')
    return res_img

img1 = Image.open(r'C:\Users\Anton\Downloads\lunar_images\lunar_images\lunar01_raw.jpg')
img2 = Image.open(r'C:\Users\Anton\Downloads\lunar_images\lunar_images\lunar02_raw.jpg')
img3 = Image.open(r'C:\Users\Anton\Downloads\lunar_images\lunar_images\lunar03_raw.jpg')

change_lunar(img1).save(r'C:\Users\Anton\Desktop\информатика\3_sem\np001.jpg')
change_lunar(img2).save(r'C:\Users\Anton\Desktop\информатика\3_sem\np002.jpg')
change_lunar(img3).save(r'C:\Users\Anton\Desktop\информатика\3_sem\np003.jpg')
