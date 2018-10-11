import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

resized = imutils.resize(image, width = 100)
cv2.imshow("resized image", resized)
cv2.waitKey(0)

resized = imutils.resize(image, height = 500)
cv2.imshow("resized image", resized)
cv2.waitKey(0)