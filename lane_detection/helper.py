"""
Helper functions for lane detection
"""
import matplotlib.image as mpimg
import numpy as np


def load_image(image_name):
    image = mpimg.imread(image_name)
    print('This image is: ', type(image),
          'with dimensions:', image.shape)
    # We work with the copy instead of the original image
    y_size = image.shape[0]
    x_size = image.shape[1]
    copy = np.copy(image)
    return copy, x_size, y_size


def load_highway_image(image_name='highway.jpg'):
    return load_image(image_name)


def load_exit_ramp_image(image_name='exit-ramp.jpg'):
    return load_image(image_name)
