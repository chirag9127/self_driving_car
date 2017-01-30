"""
Apply color and region filters to test image
"""
import matplotlib.pyplot as plt
import numpy as np

from color_selection import get_color_threshold
from helper import load_highway_image
from region_mask import get_region_coordinates


def convert_pixels():
    image, x_size, y_size = load_highway_image()
    copy = np.copy(image)
    line_image = np.copy(copy)
    left_bottom, right_bottom, apex = get_region_coordinates()
    rgb_threshold = get_color_threshold()

    fit_left = np.polyfit(
        (left_bottom[0], apex[0]), (left_bottom[1], apex[1]), 1)
    fit_right = np.polyfit(
        (right_bottom[0], apex[0]), (right_bottom[1], apex[1]), 1)
    fit_bottom = np.polyfit(
        (left_bottom[0], right_bottom[0]),
        (left_bottom[1], right_bottom[1]), 1)

    color_thresholds = (copy[:, :, 0] < rgb_threshold[0]) | \
                       (copy[:, :, 1] < rgb_threshold[1]) | \
                       (copy[:, :, 2] < rgb_threshold[2])

    XX, YY = np.meshgrid(np.arange(0, x_size), np.arange(0, y_size))
    region_thresholds = (YY > (XX*fit_left[0] + fit_left[1])) & \
                        (YY > (XX*fit_right[0] + fit_right[1])) & \
                        (YY < (XX*fit_bottom[0] + fit_bottom[1]))

    copy[color_thresholds | ~region_thresholds] = [0, 0, 0]
    line_image[~color_thresholds & region_thresholds] = [255, 0, 0]
    plt.imshow(image)
    x = [left_bottom[0], right_bottom[0], apex[0], left_bottom[0]]
    y = [left_bottom[1], right_bottom[1], apex[1], left_bottom[1]]
    plt.plot(x, y, 'b--', lw=4)
    plt.show()

    plt.imshow(copy)
    plt.show()
    plt.imshow(line_image)
    plt.show()


if __name__ == '__main__':
    convert_pixels()
