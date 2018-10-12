from __future__ import print_function
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# get blurred, thresh, and threshInv
# for the 3ird argument, by supplying cv2.ADAPTIVE_THRESH_MEAN_C, we indicate that we want to compute the mean of the neighborhood of pixels and threat it as our T value
# for the 5th argument, 1& means that we examine 11x11 pixel regions of the image, instead of trying to threshold the image globally
# the 6th argument is for fine-tune our thresholding
blurred = cv2.GaussianBlur(image, (5,5), 0)
thresh_mean1 = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11,4)
thresh_mean2 = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11,3)
thresh_mean3 = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 15,4)
thresh_mean4 = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 15,3)
thresh_gaussian1 = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11,4)
thresh_gaussian2 = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11,3)
thresh_gaussian3 = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15,4)
thresh_gaussian4 = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15,3)

thresh_mean = np.hstack([blurred, thresh_mean1, thresh_mean2, thresh_mean3, thresh_mean4])
thresh_gaussian = np.hstack([blurred, thresh_gaussian1, thresh_gaussian2, thresh_gaussian3, thresh_gaussian4])
cv2.imshow("adaptivetThreshold_mean", thresh_mean)
cv2.imshow("adaptivetThreshold_gaussian", thresh_gaussian)

cv2.waitKey(0)

# #show histogram
# hist = cv2.calcHist([image], [0], None, [256], [0, 256])
# plt.figure()
# plt.title("Color Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of Pixels")
# plt.plot(hist)
# plt.xlim([0,256])
# plt.show()