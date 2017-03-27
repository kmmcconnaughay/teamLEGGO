"""
Pixelates a given image.

Authors: Anil Patel, Onur Talu
"""
import math
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image


def load_img(filename):
    """
    load an image from a file and return it as an array of rgb values.
    """
    img = Image.open(filename, 'r')
    data = np.array(img)
    return data


def get_square(array, row, col, size):
    """
    gets all of the pixels of a supersquare in the array for a given row,
    column, and size for each superpixel.
    """

    # figure out where in the full image array the pixels are
    firstcol = col*size
    firstrow = row*size
    lastcol = firstcol+size
    lastrow = firstrow+size

    # return only those pixels we've determined to be in the desired superpixel
    pixels = array[firstcol:lastcol, firstrow:lastrow, :]
    return pixels


def average_square(pixels):
    """
    Take in a list of pixels and return the average rgb values of the list
    """

    # unpack all values of each color from all pixels
    red = pixels[:, :, 0]
    green = pixels[:, :, 1]
    blue = pixels[:, :, 2]

    # calculate number of pixels being input
    num_pix = red.shape[0]**2

    # sum color values and divide to get the average value
    avg_r = 255 - int(np.sum(red)/num_pix)
    avg_g = 255 - int(np.sum(green)/num_pix)
    avg_b = 255 - int(np.sum(blue)/num_pix)

    return [avg_r, avg_g, avg_b]


def get_pixel(super_pixel):
    """
    creates a superpixel matrix consisting of all the average rgb values
    """

    values = average_square(super_pixel)   # grab average rgb values
    pix = super_pixel.shape[0]             # determine pixel side length
    size = (pix, pix)                       # make a tuple of superpixel size

    # unpack rgb averages
    red_val = values[0]
    green_val = values[1]
    blue_val = values[2]

    # create matrices of superpixel size with all average values
    red_matrix = red_val * np.ones(size)
    green_matrix = green_val * np.ones(size)
    blue_matrix = blue_val * np.ones(size)

    # stack matrices on top of each other
    final = np.dstack((red_matrix, green_matrix, blue_matrix))
    return final


def pixelate_dat_ish(file_name, pixel_size):
    """
    combine all functions into a fully pixelated image
    """

    array = load_img(file_name)     # create the image array
    size = array.shape              # determine size of the pic
    height = size[0]                # height of the pic
    width = size[1]                 # width of the pic

    squaresize = pixel_size                    # side length of superpixel
    numcols = math.floor(width/squaresize)     # number of columns rounded down
    numrows = math.floor(height/squaresize)    # number of rows rounded down

    # create an empty array to add to
    pixelated = np.empty((height, width, 3))

    for col in range(0, numcols):
        for row in range(0, numrows):
            pixels = get_square(array, col, row, squaresize)
            super_pixel = get_pixel(pixels)

            firstcol = col*pixel_size
            lastcol = firstcol+pixel_size

            firstrow = row*pixel_size
            lastrow = firstrow+pixel_size
            pixelated[firstrow:lastrow, firstcol:lastcol, :] = super_pixel

    return pixelated


def custom_color(red_val, green_val, blue_val):
    red_matrix = red_val * np.ones((25, 25))
    green_matrix = green_val * np.ones((25, 25))
    blue_matrix = blue_val * np.ones((25, 25))
    final = np.dstack((red_matrix, green_matrix, blue_matrix))
    return final


if __name__ == "__main__":
    
    x = load_img('wallaby.jpg')
    plt.imshow(x)
    plt.axis('off')
    plt.show()
    """
    x = load_img('wallaby.jpg')
    super_square1 = get_square(x, 1, 1, 25)
    superpixel1 = average_square(super_square1)
    print(average_square(super_square1))
    plt.imshow(get_pixel(super_square1))
    # plt.imshow(x)
    plt.axis('off')
    plt.show()

    """
    image_pix = pixelate_dat_ish('wallaby.jpg', 25)
    plt.imshow(image_pix)
    plt.axis('off')
    plt.savefig("test.png", bbox_inches='tight')
    plt.show()
