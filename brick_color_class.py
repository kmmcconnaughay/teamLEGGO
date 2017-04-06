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
    def load(self):
        """ Load image of each brick color.
        """
        self.path = '/home/kerry/teamLEGGO/Pick A Brick_LEGO_All_Bricks'
        self.filenames = ['Brick yellow', 'Bright blue', 'Bright orange', 'Bright red',
        'Bright reddish violet', 'Bright yellow', 'Bright yellowish green', 'Dark green',
        'Dark stone grey', 'Light purple', 'Medium azur', 'Medium blue', 'Medium lavendel',
        'Medium lilac', 'Medium nougat', 'Medium stone grey', 'Reddish brown', 'Sand green'
        ]
        self.bricks = []
        for filename in self.filenames:
            image = Image.open(self.path + '//' + filename, 'r')
            image.load()
            width, height = image.size
            self.bricks.append(image)
        return self.bricks

    def get_colors(self):
        self.brick_pixels = {}
        self.image_middle_pixels = []

        self.load()

        for brick in self.bricks:
            self.data = np.array(image)
            self.middle_pixel = self.data[int(height/2), int(0.6 * width)]
            self.brick_pixels[filename] = self.middle_pixel
            self.image_middle_pixels.append(self.middle_pixel)
            # print(filename, middle_pixel)
            # print(middle_pixel)
        return  brick_pixels, image_middle_pixels


if __name__ == '__main__':
    image = Brick()
    image.get_colors()
    print(self.brick_pixels)
    print(self.image_middle_pixels)