from __future__ import print_function
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11,11),0)
cv2.imshow("Image", image)

edged = cv2.Canny(blurred, 30, 150)
cv2.imshow("Edges", edged)
cv2.waitKey(0)


# count the number of coins
(_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("I count {} coins in this image".format(len(cnts)))


# to add green color contour to the coins
coins = image.copy()
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Coins", coins)
cv2.waitKey(0)

# crop each individual coin from the image
for (i, c) in enumerate(cnts):
	(x, y, w, h) = cv2.boundingRect(c)

	# we can find the zone of each coin thanks to cnts. We find the minimum circle that includes the coin.
	coin = image[y:y+h, x:x+w]
	mask = np.zeros(image.shape[:2], dtype = "uint8")
	((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
	cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
	mask = mask[y:y+h, x:x+w]

	# show each masked coin
	print("Coin #{}".format(i + 1))
	cv2.imshow("Coin # {}".format(i+1), cv2.bitwise_and(coin, coin, mask = mask))

	cv2.waitKey(0)
