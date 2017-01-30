"""
Given the test image, find all the pixels in a given region
"""
import matplotlib.pyplot as plt
import numpy as np

from helper import load_highway_image


def get_region_coordinates():
    left_bottom = [130, 539]
    right_bottom = [800, 539]
    apex = [485, 310]
    return left_bottom, right_bottom, apex


def convert_pixels():
    region_select, x_size, y_size = load_highway_image()
    left_bottom, right_bottom, apex = get_region_coordinates()
    fit_left = np.polyfit(
        (left_bottom[0], apex[0]), (left_bottom[1], apex[1]), 1)
    fit_right = np.polyfit(
        (right_bottom[0], apex[0]), (right_bottom[1], apex[1]), 1)
    fit_bottom = np.polyfit(
        (left_bottom[0], right_bottom[0]),
        (left_bottom[1], right_bottom[1]), 1)
    XX, YY = np.meshgrid(np.arange(0, x_size), np.arange(0, y_size))
    region_thresholds = (YY > (XX*fit_left[0] + fit_left[1])) & \
                        (YY > (XX*fit_right[0] + fit_right[1])) & \
                        (YY < (XX*fit_bottom[0] + fit_bottom[1]))
    region_select[region_thresholds] = [255, 0, 0]
    plt.imshow(region_select)
    plt.show()


if __name__ == '__main__':
    convert_pixels()
