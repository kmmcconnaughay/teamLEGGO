"""
Take a saved image, convert to black and white, and apply a color filter
to the image. Display the final filtered image in a window.

Author: Kerry McConnaughay
"""
import math
import matplotlib.pyplot as plt
import cv2
import PIL.Image as Image
import numpy as np
from skimage import data, color
from skimage import img_as_float

class Mini_Mosaic():
    def __init__(self):
        self.path = '/home/kerry/teamLEGGO/'
        self.file = 'sunflower.png'

    def load_bw(self):
        image = Image.open(self.path + '//' + self.file)
        image.load()
        # L = R * 299/1000 + G * 587/1000 + B * 114/1000
        self.bw = image.convert('1')
        return self.bw

    """
    def colorize(image, hue, saturation=1):
        hue_gradient = np.linspace(0, 1)
        hsv = np.ones(shape=(1, len(hue_gradient), 3), dtype=float)
        hsv[:, :, 0] = hue_gradient

        all_hues = color.hsv2rgb(hsv)

        fig, ax = plt.subplots(figsize=(5, 2))
        # Set image extent so hues go from 0 to 1 and the image is a nice aspect ratio.
        ax.imshow(all_hues, extent=(0, 1, 0, 0.2))
        ax.set_axis_off()
        hsv = color.rgb2hsv(image)
        hsv[:, :, 1] = saturation
        hsv[:, :, 0] = hue
        return color.hsv2rgb(hsv)
    """
    def display_bw(self):
        self.load_bw()
        plt.imshow(self.bw)
        plt.axis('off')
        plt.show()
        self.final_image = plt.savefig('black_and_white.png', bbox_inches='tight', origin='lower')
        return self.final_image

    def get_data(self):
        self.data = np.array(self.final_image)
        print(self.data)
        return self.data
"""
    def filter_it(self):
        # grayscale_image = img_as_float(data.camera()[::2, ::2])
        # image = color.gray2rgb(grayscale_image)
        self.display_bw()
        red_multiplier = [1, 0, 0]
        yellow_multiplier = [1, 1, 0]

        fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8, 4), sharex=True, sharey=True)
        ax1.imshow(red_multiplier * self.final_image)
        ax2.imshow(yellow_multiplier * self.final_image)
        ax1.set_adjustable('box-forced')
        ax2.set_adjustable('box-forced')
"""


if __name__ == '__main__':
    image = Mini_Mosaic()
    image.display_bw()
    image.get_data()
    #image.filter_it()
    # image.colorize()
