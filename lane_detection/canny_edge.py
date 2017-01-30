"""
Implementing canny edge on exit ramp image
"""
import cv2
import matplotlib.pyplot as plt

from helper import load_exit_ramp_image


def create_grayscale_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return gray


def apply_gaussian_smoothing(image):
    kernel_size = 5
    blur_gray = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    return blur_gray


def apply_canny_edge_detection(image):
    low_threshold = 50
    high_threshold = 150
    edges = cv2.Canny(image, low_threshold, high_threshold)
    return edges


def run():
    image, x_size, y_size = load_exit_ramp_image()

    gray_image = create_grayscale_image(image)
    plt.imshow(gray_image, cmap='gray')
    plt.show()

    blur_gray = apply_gaussian_smoothing(gray_image)
    plt.imshow(blur_gray)
    plt.show()

    edges = apply_canny_edge_detection(blur_gray)
    plt.imshow(edges, cmap='Greys_r')
    plt.show()


if __name__ == '__main__':
    run()
