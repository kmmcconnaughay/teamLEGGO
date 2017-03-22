"""
Pixelates a given image.

Authors: Anil Patel, Onur Talu
"""
import math
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image


def load_img(filename):
    img = Image.open(filename, 'r')
    data = np.array(img)
    return data


def get_square(array, row, col, size):
    """
    gets all of the pixels of a supersquare in the array for a given row,
    column, and size for each superpixel.
    """
    firstcol = col*size
    firstrow = row*size
    lastcol = firstcol+size
    lastrow = firstrow+size

    pixels = array[firstcol:lastcol, firstrow:lastrow, :]
    return pixels


if __name__ == "__main__":
    x = load_img('wallaby.jpg')
    # plt.imshow(x)
    # plt.show()

    size = x.shape
    width = size[1]
    height = size[0]
    squaresize = 25  # side length of superpixel
    numcols = math.floor(width/squaresize)
    numrows = math.floor(height/squaresize)
    super_square1 = get_square(x, 1, 1, squaresize)
    print(super_square1.shape)
