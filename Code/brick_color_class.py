"""
Take a saved brick image, get RGB value, save the RGB and file name as tuples in
a dictionary, and print the dictionary.

Author: Kerry McConnaughay

"""
import cv2
import PIL.Image as Image
from PIL import Image
import numpy as np


class Brick():
    def __init__(self):
        """ Initialize the class, Brick.
        """
        self.height = 75
        self.width = 75
        self.cwd = os.getcwd()
        i = len(cwd)
        self.cwd = self.cwd[0:i-5]
        self.path = self.cwd + '/Pick A Brick_LEGO_All_Bricks'
        self.filenames = ['Brick yellow', 'Bright blue', 'Bright orange', 'Bright red',
        'Bright reddish violet', 'Bright yellow', 'Bright yellowish green', 'Dark green',
        'Dark stone grey', 'Light purple', 'Medium azur', 'Medium blue', 'Medium lavendel',
        'Medium lilac', 'Medium nougat', 'Medium stone grey', 'Reddish brown', 'Sand green'
        ]

    def load(self):
        """ Load image of each brick color.
        """
        self.bricks = []
        for filename in self.filenames:
            image = Image.open(self.path + '//' + filename, 'r')
            image.load()
            self.bricks.append(image)
        return self.bricks

    def get_colors(self):
        """ Get a list and dictionary of the RGB values of the middle pixels of
        each LEGO brick image.
        """
        self.brick_pixels = {}
        self.image_middle_pixels = []

        self.load()

        for brick in self.bricks:
            self.data = np.array(brick)
            self.middle_pixel = self.data[int(self.height/2), int(0.6 * self.width)]
            self.image_middle_pixels.append(self.middle_pixel)
        print(self.image_middle_pixels)
        return  self.brick_pixels, self.image_middle_pixels





if __name__ == '__main__':
    image = Brick()
    image.get_colors()
