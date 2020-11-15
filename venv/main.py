import numpy as np
from matplotlib import pyplot
from skimage.io import imread

if __name__ == "__main__":
    # Read data image as a grayscale two dimensional array.
    image = imread('data.jpg', as_gray=True)
    # Translate the two dimensional array into a one dimensional array.
    pixel_array = np.array(image.flatten())
    pixel_array *= 255 #Adjust floating point (0-1) to brightness (0-255) values.

    # Build and display the histogram.
    pyplot.hist(pixel_array, bins=range(255))
    pyplot.title("Pixel Brightness Counts for Grayscale Image")
    pyplot.xlabel("Brightness (0-255)")
    pyplot.ylabel("Number of Pixels")
    pyplot.show()