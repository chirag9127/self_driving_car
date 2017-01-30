"""
Given the test image, find all the pixels which are white
Run as /usr/bin/python color_selection.py
"""
import matplotlib.pyplot as plt

from helper import load_highway_image


def get_color_threshold():
    red_threshold = 200
    green_threshold = 200
    blue_threshold = 200
    return [red_threshold, green_threshold, blue_threshold]


def convert_pixels():
    copy, x_size, y_size = load_highway_image()
    rgb_thresholds = get_color_threshold()

    thresholds = (copy[:, :, 0] < rgb_thresholds[0]) \
        | (copy[:, :, 1] < rgb_thresholds[1]) \
        | (copy[:, :, 2] < rgb_thresholds[2])
    copy[thresholds] = [0, 0, 0]
    plt.imshow(copy)
    plt.show()


if __name__ == '__main__':
    convert_pixels()
