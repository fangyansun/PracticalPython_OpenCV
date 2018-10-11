import numpy as np
import argparse
import imutils
import cv2

rectangle = np.zeros((300,300), dtype="uint8")
cv2.rectangle(rectangle, (40,40),(260,260),255,-1)
cv2.imshow("Rectangle", rectangle)
cv2.waitKey(0)

circle = np.zeros((300,300), dtype="uint8")
cv2.circle(circle, (150,150),140,255,-1)
cv2.imshow("Circle", circle)
cv2.waitKey(0)

# we can do different operation for "AND", "OR", "XOR", "NOT" with "bitwise_and", "bitwise_or", "bitwise_xor", "bitwise_not"
bitwiseAnd = cv2.bitwise_and(rectangle,circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)