"""
Stuff that does not work. An alternative trial for pixelation.

Authors: Onur Talu
"""
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image
from math import floor


def load_image(filename):
    # boilerplate code to open an image and make it editable
    img = Image.open(filename, 'r')
    data = np.array(img)
    return data


def dimensions(filename, no_columns=256):
    img = load_image(filename)
    pixelx = float(img.shape[1] / no_columns)
    no_rows = int(floor(img.shape[0] / pixelx))
    pixely = float(img.shape[0] / no_rows)
    return [pixelx, pixely, no_rows, no_columns]


if __name__ == "__main__":
    img = load_image('input.png')
    dimensions(img)
    # plt.imshow(img, interpolation='nearest')
    # plt.show()
