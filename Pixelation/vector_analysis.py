"""
Takes in a picture, pixelates it, and then replaces the colors with closest
matching lego brick color.

Authors: Anil Patel, Onur Talu
"""
import math
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image
from brick_color_analysis import load_image

"""List of lego colors, will be replaced by a dictionary."""

"""
legolist = [[251, 229, 8], [74, 184, 72], [236, 29, 35], [69, 140, 204],
            [0, 0, 0], [206, 119, 42], [247, 145, 47],
            [26, 0, 255], [101, 67, 33], [255, 185, 2]]
"""
filenames = ['Brick yellow', 'Bright blue', 'Bright orange', 'Bright red',
             'Bright reddish violet', 'Bright yellow',
             'Bright yellowish green', 'Dark green', 'Dark stone grey',
             'Light purple', 'Medium azur', 'Medium blue',
             'Medium lavendel', 'Medium lilac', 'Medium nougat',
             'Medium stone grey', 'Reddish brown', 'Sand green']

""" initialize an empty list to be populated with all used lego names"""
lego_nums = []

legodict, legolist = load_image(filenames)
# print(legodict.values)


def load_img(filename):
    """
    load an image from a file and return it as an array of rgb values.
    """
    img = Image.open(filename, 'r')  # load the image in read mode
    data = np.array(img)             # turns the image into an array of rgb
    return data                      # returns the array


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
    r = int(np.sum(red)/num_pix)
    g = int(np.sum(green)/num_pix)
    b = int(np.sum(blue)/num_pix)
    return [r, g, b]


def compare(pixels):
    """Takes in a list of pixels and returns the closest match from the list
       of pre-determined lego colors to the average color of the group."""
    avg_color = average_square(pixels)

    r = avg_color[0]
    g = avg_color[1]
    b = avg_color[2]

    # return [r, g, b]

    min_dist = 100000000
    min_color = 0

    """ perform euclidian distance analysis between the determined avg color
        of the pixel set and the list of lego colors. Find closest color."""
    for i in range(len(legolist)):
        color = legolist[i]
        color_r = color[0]
        color_g = color[1]
        color_b = color[2]

        dist = math.sqrt(((r-color_r)*1)**2 + ((g - color_g)*1)**2 +
                         ((b - color_b)*1)**2)

        if dist < min_dist:
            min_dist = dist
            min_color = i

    lego_color = legolist[min_color]
    lego = filenames[min_color]
    lego_nums.append(lego)

    r = 255 - int(lego_color[0])
    g = 255 - int(lego_color[1])
    b = 255 - int(lego_color[2])

    # print()
    # print(r, g, b)
    return [r, g, b]


def get_pixel(super_pixel):
    """
    creates a superpixel matrix consisting of all the average rgb values
    """

    values = average_square(super_pixel)   # grab average rgb values
    pix = super_pixel.shape[0]             # determine pixel side length
    size = (pix, pix)                      # make a tuple of superpixel size

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


def lego_dat_ish(file_name, mat_size):
    """
    combine all functions into a fully lego'd image. Returns the array of the
    lego'd image.
    """

    array = load_img(file_name)     # create the image array
    size = array.shape              # determine size of the pic
    scaled_size = min([size[0], size[1]])
    pixel_size = round(scaled_size/mat_size)

    height = size[0] - size[0] % pixel_size  # height of the pic
    width = size[1] - size[1] % pixel_size   # width of the pic

    squaresize = pixel_size                    # side length of superpixel
    numcols = math.floor(width/squaresize)     # number of columns rounded down
    numrows = math.floor(height/squaresize)   # number of rows rounded down

    # create an empty array to add to
    pixelated = np.empty((height, width, 3))

    """run through all the rows and columns and populate the empty matrix
       with the pixelated and lego-adjusted pixels."""
    for col in range(0, numcols):
        for row in range(0, numrows):
            pixels = get_square(array, col, row, squaresize)
            super_pixel = compare(pixels)

            firstcol = col*pixel_size
            lastcol = firstcol+pixel_size

            firstrow = row*pixel_size
            lastrow = firstrow+pixel_size
            pixelated[firstrow:lastrow, firstcol:lastcol, :] = super_pixel

    return pixelated


def custom_color(red_val, green_val, blue_val):
    """testing function used to debug the color-displaying stuff."""
    red_matrix = red_val * np.ones((25, 25))
    green_matrix = green_val * np.ones((25, 25))
    blue_matrix = blue_val * np.ones((25, 25))
    final = np.dstack((red_matrix, green_matrix, blue_matrix))
    return final


def make_hist(legolist):
    """makes a histogram of the legos used to make an image for pricing
       and inventory using in the GUI"""
    d = dict()
    for c in legolist:
        d[c] = d.get(c, 0) + 1

    return d


if __name__ == "__main__":
    filename = "Obama.jpg"
    org_image = load_img(filename)
    plt.imshow(org_image)
    plt.axis('off')
    plt.show()

    image_pix = lego_dat_ish(filename, 100)
    plt.imshow(image_pix)
    plt.axis('off')
    plt.savefig("test.png", bbox_inches='tight', origin='lower')
    plt.show()

    print(make_hist(lego_nums))
