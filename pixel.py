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


def average_square(pixels):
    red = pixels[:, :, 0]
    green = pixels[:, :, 1]
    blue = pixels[:, :, 2]

    num_pix = red.shape[0]**2
    avg_r = np.sum(red)/num_pix
    avg_g = np.sum(green)/num_pix
    avg_b = np.sum(blue)/num_pix

    return [avg_r, avg_g, avg_b]


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
    super_square1 = get_square(x, 18, 18, squaresize)

    superpixel1 = average_square(super_square1)
    print(average_square(super_square1))
