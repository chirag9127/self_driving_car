"""
Apply Hough transform on the blurred image
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

from canny_edge import apply_gaussian_smoothing, apply_canny_edge_detection, \
    create_grayscale_image
from helper import load_exit_ramp_image


def apply_hough_transform(edges):
    rho = 2
    theta = np.pi / 180
    threshold = 15
    min_line_length = 40
    max_line_gap = 20
    lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]),
                            min_line_length, max_line_gap)
    return lines


def run():
    image, _, _ = load_exit_ramp_image()
    line_image = np.copy(image) * 0
    gray_image = create_grayscale_image(image)
    edges = apply_canny_edge_detection(apply_gaussian_smoothing(gray_image))

    lines = apply_hough_transform(edges)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)

    color_edges = np.dstack((edges, edges, edges))

    combo = cv2.addWeighted(color_edges, 0.8, line_image, 1, 0)

    plt.imshow(combo)
    plt.show()


if __name__ == '__main__':
    run()
