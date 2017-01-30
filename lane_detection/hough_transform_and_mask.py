"""
Apply Hough transform on a masked region
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

from canny_edge import apply_gaussian_smoothing, apply_canny_edge_detection, \
    create_grayscale_image
from helper import load_exit_ramp_image
from hough_transform import apply_hough_transform


def get_mask(imshape, edges):
    mask = np.zeros_like(edges)
    ignore_mask_color = 255
    vertices = np.array(
        [[(0, imshape[0]), (450, 290), (490, 290), (imshape[1], imshape[0])]],
        dtype=np.int32)
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    masked_edges = cv2.bitwise_and(edges, mask)
    return masked_edges


def run():
    image, _, _ = load_exit_ramp_image()
    line_image = np.copy(image) * 0
    gray_image = create_grayscale_image(image)
    edges = apply_canny_edge_detection(apply_gaussian_smoothing(gray_image))

    masked_edges = get_mask(image.shape, edges)

    lines = apply_hough_transform(masked_edges)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)

    color_edges = np.dstack((edges, edges, edges))

    lines_edges = cv2.addWeighted(color_edges, 0.8, line_image, 1, 0)
    plt.imshow(lines_edges)

    plt.show()


if __name__ == '__main__':
    run()
