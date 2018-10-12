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
image = cv2.GaussianBlur(image, (5,5),0)


# Canny edge detector is a multi-step process. It involves blurring the image to remove noise, computing Sobel gradiant images in the x and y direction, suppressing edges, 
# and finally a hysteresis thresholding stage that determines if a pixel is "edge-like" or not.
# the first argument is our grayscale image
# then comes threshold1 and threshold2. Any gradient value larger than threshold2 is considered to be an edge. 
# any value below threshold 1 is considered not to be an edge. 
# values between threshold1 and threshold2 are either classified as edges or non-edges based on how their intensities are "connected"

canny = cv2.Canny(image, 30, 150)
cv2.imshow("Canny", canny)

cv2.waitKey(0)
