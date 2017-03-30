"""
Take a saved brick image, get RGB value, save the RGB and file name as tuples in
a dictionary, and print the dictionary.

Author: Kerry McConnaughay

"""
import cv2
import PIL.Image as Image
import numpy as np
from skimage import data
d = {}

def load_image(filenames):
    """
    Load a brick image from the directory and return image size.
    """
    dimensions_images = []
    image_arrays = []
    path = '/home/kerry/teamLEGGO/Pick A Brick_LEGO_All_Bricks'
    for filename in filenames:
        image = Image.open(path + '//' + filename, 'r')
        image.load()
        width, height = image.size
        dimensions = width, height
        dimensions_images.append(dimensions)

        data = np.array(image)
        image_arrays.append(data)
    print(dimensions_images)
    print(image_arrays)
    return image_arrays, dimensions_images
"""

# AVERAGE COLOR VALUE OF EACH ROW OF pixels
# average_color_per_row = numpy.average(image, axis = 0)
# MAKE IMAGE OUT OF AVERAGE COLOR value
# average_color_img = numpy.array([[average_color]*100]*100, numpy.uint8)
# cv2.imwrite( "average_color.png", average_color_img )


def save_image(npdata, out_filename):
    image = Image.fromarray(np.array( ycc_uint8, 'RGB')
    image.save(out_filename)
"""

if __name__ == '__main__':
    filenames = ['Black', 'Brick yellow', 'Bright blue', 'Bright orange', 'Bright red',
    'Bright reddish violet', 'Bright yellow', 'Bright yellowish green', 'Dark green',
    'Dark stone grey', 'Light purple', 'Medium azur', 'Medium blue', 'Medium lavendel',
    'Medium lilac', 'Medium nougat', 'Medium stone grey', 'Reddish brown', 'Sand green',
    'White']
    # load_image_pixels()
    load_image(filenames)
