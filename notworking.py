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

"""
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

    avg_r = sum(sum(red))/red.shape[0]**2
    avg_g = sum(sum(green))/green.shape[0]**2
    avg_b = sum(sum(blue))/blue.shape[0]**2

    return [avg_r, avg_g, avg_b]


def get_pixel(super_square):
    values = average_square(super_square)
    red_val = values[0]
    green_val = values[1]
    blue_val = values[2]

    red_matrix = red_val * np.ones((25, 25))
    green_matrix = green_val * np.ones((25, 25))
    blue_matrix = blue_val * np.ones((25, 25))
    final = np.dstack((red_matrix, green_matrix, blue_matrix))
    return final


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
    superpixel1 = average_square(super_square1)
    # print(average_square(super_square1))
    plt.imshow(get_pixel(super_square1))
    plt.show()
"""
