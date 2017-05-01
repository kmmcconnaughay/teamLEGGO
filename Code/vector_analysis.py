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


class vectorStuff():
    def __init__(self):
        self.input_mat_size = 100
        """List of lego colors, will be replaced by a dictionary."""

        self.filenames = ['Brick yellow', 'Bright blue', 'Bright orange', 'Bright red',
                     'Bright reddish violet', 'Bright yellow',
                     'Bright yellowish green', 'Dark green', 'Dark stone grey',
                     'Light purple', 'Medium azur', 'Medium blue',
                     'Medium lavendel', 'Medium lilac', 'Medium nougat',
                     'Medium stone grey', 'Reddish brown', 'Sand green', 'White']

        """ initialize an empty list to be populated with all used lego names"""
        self.lego_nums = []
        self.legodict, self.legolist = load_image(self.filenames)


    def load_img(self, filename):
        """
        load an image from a file and return it as an array of rgb values.
        """
        img = Image.open(filename, 'r')  # load the image in read mode
        data = np.array(img)             # turns the image into an array of rgb
        return data                      # returns the array


    def get_square(self, array, row, col, size):
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


    def average_square(self, pixels):
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


    def compare(self, pixels):
        """Takes in a list of pixels and returns the closest match from the list
           of pre-determined lego colors to the average color of the group."""
        avg_color = self.average_square(pixels)

        r = avg_color[0]
        g = avg_color[1]
        b = avg_color[2]

        # return [r, g, b]

        min_dist = 100000000
        min_color = 0

        """ perform euclidian distance analysis between the determined avg color
            of the pixel set and the list of lego colors. Find closest color."""
        for i in range(len(self.legolist)):
            color = self.legolist[i]
            color_r = color[0]
            color_g = color[1]
            color_b = color[2]

            dist = math.sqrt(((r-color_r)*1)**2 + ((g - color_g)*1)**2 +
                             ((b - color_b)*1)**2)

            if dist < min_dist:
                min_dist = dist
                min_color = i

        lego_color = self.legolist[min_color]
        lego = self.filenames[min_color]
        self.lego_nums.append(lego)

        r = 255 - int(lego_color[0])
        g = 255 - int(lego_color[1])
        b = 255 - int(lego_color[2])

        # print()
        # print(r, g, b)
        return [r, g, b]


    def get_pixel(self, super_pixel):
        """
        creates a superpixel matrix consisting of all the average rgb values
        """

        values = self.average_square(super_pixel)   # grab average rgb values
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


    def lego_dat_ish(self, file_name, mat_size):
        """
        combine all functions into a fully lego'd image. Returns the array of the
        lego'd image.
        """

        array = self.load_img(file_name)  # create the image array
        size = array.shape                # determine size of the pic
        scaled_size = max([size[0], size[1]])
        pixel_size = round(scaled_size/mat_size)

        height = size[0] - size[0] % pixel_size  # height of the pic
        width = size[1] - size[1] % pixel_size   # width of the pic

        squaresize = pixel_size                   # side length of superpixel
        numcols = math.floor(width/squaresize)    # num columns rounded down
        numrows = math.floor(height/squaresize)   # num rows rounded down

        # create an empty array to add to
        pixelated = np.empty((height, width, 3))

        """run through all the rows and columns and populate the empty matrix
           with the pixelated and lego-adjusted pixels."""
        for col in range(0, numcols):
            for row in range(0, numrows):
                pixels = self.get_square(array, col, row, squaresize)
                super_pixel = self.compare(pixels)

                firstcol = col*pixel_size
                lastcol = firstcol+pixel_size

                firstrow = row*pixel_size
                lastrow = firstrow+pixel_size
                pixelated[firstrow:lastrow, firstcol:lastcol, :] = super_pixel

        return pixelated

    def lego_dat_brick(self, file_name, mat_size):
        """
        combine all functions into a fully lego'd image. Returns the array of
        the lego'd image.
        """
        brick_size = 27
        array = self.load_img(file_name)     # create the image array
        size = array.shape              # determine size of the pic
        scaled_size = max([size[0], size[1]])
        pixel_size = round(scaled_size/mat_size)

        height = size[0] - size[0] % pixel_size  # height of the pic
        width = size[1] - size[1] % pixel_size   # width of the pic

        squaresize = pixel_size                    # side length of superpixel
        numcols = math.floor(width/squaresize)     # number of columns rnd down
        numrows = math.floor(height/squaresize)   # number of rows rounded down

        height_lego = numcols*brick_size
        width_lego = numrows*brick_size

        # print(height_lego)
        # print(width_lego)

        # create an empty array to add to
        pixelated = np.empty((height_lego, width_lego, 3))
        brick = self.load_img('brick_template.png')

        """run through all the rows and columns and populate the empty matrix
           with the pixelated and lego-adjusted pixels."""
        for col in range(0, numcols-20):
            for row in range(0, numrows-20):
                # pixels = self.get_square(array, col, row, squaresize)
                # super_pixel = self.compare(pixels)

                firstcol = col*brick_size
                lastcol = firstcol+brick_size

                firstrow = row*brick_size
                lastrow = firstrow+brick_size

                # print(lastcol)
                brick = [255, 255, 255] - brick[:, :, 0:3]
                pixelated[firstrow:lastrow, firstcol:lastcol, :] = brick

        return pixelated

    def custom_color(self, red_val, green_val, blue_val):
        """testing function used to debug the color-displaying stuff."""
        red_matrix = red_val * np.ones((25, 25))
        green_matrix = green_val * np.ones((25, 25))
        blue_matrix = blue_val * np.ones((25, 25))
        final = np.dstack((red_matrix, green_matrix, blue_matrix))
        return final

    def make_hist(self):
        """makes a histogram of the legos used to make an image for pricing
           and inventory using in the GUI"""
        d = dict()
        for c in self.legolist:
            d[c] = d.get(c, 0) + 1

        return d

    def get_price(self, lego_nums, input_mat_size):
        """Gets the cumulative cost of the lego mat and the lego bricks.
            The price of lego mat is taken from a dictionary, while the price
            of 1x1 lego bricks is 7 cents each."""
        brick_cost = round(len(lego_nums)*.07)
        mat_cost = int(25)  # this should change after research
        total_cost = brick_cost+mat_cost

        print('The total number of bricks used is '+str(len(lego_nums)))
        print('The total cost is '+str(total_cost)+' dollars')

    def runPixel(self):

        # print('Please specify the size of your mat:')

        name = "teamLEGGO"
        extension = ".png"
        filename = name+extension
        # org_image = self.load_img(filename)
        # plt.imshow(org_image)
        # plt.axis('off')
        # plt.show()

        # image_pix = self.lego_dat_brick(filename, int(self.input_mat_size))
        image_pix = self.lego_dat_brick(filename, 50)
        # print(image_pix)
        plt.imshow(image_pix)
        plt.axis('off')
        plt.savefig(name+"_pix"+extension, bbox_inches='tight', origin='lower')
        plt.show()

        img = self.load_img('brick_template.png')
        plt.imshow(img)
        plt.axis('off')
        plt.show()

        # print(self.make_hist())
        self.get_price(self.lego_nums, self.input_mat_size)


if __name__ == "__main__":
    pic = vectorStuff()
    pic.runPixel()
