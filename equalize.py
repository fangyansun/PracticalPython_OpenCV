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

eq = cv2.equalizeHist(image)

combine = np.hstack([image, eq])

cv2.imshow("Histogram Equalization", combine)
cv2.waitKey(0)

hist = cv2.calcHist([image], [0], None, [256], [0, 256])
hist_eq = cv2.calcHist([eq], [0], None, [256], [0, 256])
plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist, color = "r")
plt.plot(hist_eq, color = "g")
plt.xlim([0,256])
plt.show()
cv2.waitKey(0)