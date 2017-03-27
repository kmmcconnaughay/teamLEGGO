import PIL, Image
import numpy as np

""" This code will take a saved brick image, get that image's RGB value, and
save the RGB and file name as tuples in a dictionary, then print the dictionary"""
d = {}
filenames = []

def load_image(in_filename):
    for file in filenames:
        image = Image.open(filename)
        image.load()
        data = np.asarray(image, dtype = 'int32')
    return data

def save_image(npdata, out_filename)
    image = Image.fromarray(np.array( ycc_uint8, 'RGB')
    image.save(out_filename)
