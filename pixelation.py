"""
Pixelates a given image.

Authors: Anil Patel, Onur Talu
"""
import sys

import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image


def load_img(filename):
    # boilerplate code to open an image and make it editable
    img = Image.open(filename, 'r')
    data = np.array(img)
    return data


if __name__ == "__main__":
    x = load_img('input.png')
    print(x)
    plt.imshow(x, interpolation='nearest')
    plt.show()
