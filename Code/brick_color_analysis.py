"""
Take a saved brick image, get RGB value, save the RGB and file name as tuples in
a dictionary, and print the dictionary.

Author: Kerry McConnaughay

"""
import cv2
import PIL.Image as Image
import numpy as np
import os


def load_image(filenames):
    """
    Load a brick image from the directory and return image size.
    """
    brick_pixels = {}
    image_middle_pixels = []
    cwd = os.getcwd()
    i = len(cwd)
    path = '/Pick A Brick_LEGO_All_Bricks'
    for filename in filenames:
        image = Image.open(cwd[0:i-5] + path + '//' + filename, 'r')
        image.load()
        width, height = image.size

        data = np.array(image)
        middle_pixel = data[int(height/2), int(0.6 * width)]
        brick_pixels[filename] = middle_pixel
        image_middle_pixels.append(middle_pixel)
    return brick_pixels, image_middle_pixels


if __name__ == '__main__':
    filenames = ['Brick yellow', 'Bright blue', 'Bright orange', 'Bright red',
                 'Bright reddish violet', 'Bright yellow',
                 'Bright yellowish green', 'Dark green', 'Dark stone grey',
                 'Light purple', 'Medium azur', 'Medium blue',
                 'Medium lavendel', 'Medium lilac', 'Medium nougat',
                 'Medium stone grey', 'Reddish brown', 'Sand green', 'White']
    list_of_colors = load_image(filenames)
