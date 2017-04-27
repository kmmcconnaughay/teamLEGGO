"""
Pixelates a given image.

Authors: Anil Patel, Onur Talu
"""
import math
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image
# import legolist


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


def grayscale_val():
    """
    Grayscales the colors of the lego bricks and returns two list of lists, the
    RGB values of the LEGO bricks and their grayscaled conterparts.
    """
    all_values = []
    for i in range(256):
        each = [i, i, i]
        all_values.append(each)

    legolist = all_values
    """
    legolist = [[251, 229, 8], [74, 184, 72], [236, 29, 35], [69, 140, 204],
                [255, 255, 255], [0, 0, 0], [206, 119, 42], [128, 128, 128],
                [247, 145, 47]]
                """

    colorsgray = []
    for color in legolist:
        r = color[0]
        g = color[1]
        b = color[2]
        gray = int(0.2989*r + 0.5870*g + 0.1140*b)
        colorsgray.append(gray)
    return legolist, colorsgray


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
    r = 255 - int(np.sum(red)/num_pix)
    g = 255 - int(np.sum(green)/num_pix)
    b = 255 - int(np.sum(blue)/num_pix)

    gray = int(0.2989*r + 0.5870*g + 0.1140*b)
    subtract = []
    legolist, colorsgray = grayscale_val()
    for color in colorsgray:
        subtracted = math.fabs(color - gray)
        subtract.append(subtracted)
    index = subtract.index(min(subtract))
    lego = legolist[index]
    r = int(lego[0])
    b = int(lego[1])
    g = int(lego[2])

    return [r, g, b]


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
    height = size[0] - size[0] % pixel_size  # height of the pic
    width = size[1] - size[1] % pixel_size   # width of the pic

    squaresize = pixel_size                    # side length of superpixel
    numcols = math.floor(width/squaresize)     # number of columns rounded down
    numrows = math.floor(height/squaresize)   # number of rows rounded down

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

    org_image = load_img('Obama.jpg')
    plt.imshow(org_image)
    plt.axis('off')
    plt.show()

    image_pix = pixelate_dat_ish('Obama.jpg', 25)
    plt.imshow(image_pix)
    plt.axis('off')
    plt.savefig("test.png", bbox_inches='tight')
    plt.show()
