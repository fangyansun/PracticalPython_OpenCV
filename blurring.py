import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
# cv2.imshow("Original", image)

blurred = np.hstack([image, cv2.blur(image,(3,3)), cv2.blur(image, (5,5)), cv2.blur(image, (7,7))])
cv2.imshow("Averaged", blurred)
cv2.waitKey(0)

# gaussian blurring is similar to average blurring. However, instead of a simple mean, we are now using a weighted mean, where neighborhood pixels that are closer to the central pixel contribute more "weight" to the average
# the result is that, our image is less blurred, but more naturally blurred
# by setting the second argument of cv2.GaussianBlur to 0, we are asking OPENCV to automatically compute them based on our kernel size
blurred = np.hstack([image, cv2.GaussianBlur(image,(3,3),0), cv2.GaussianBlur(image, (5,5),0), cv2.GaussianBlur(image, (7,7),0)])
cv2.imshow("Gaussian", blurred)
cv2.waitKey(0)


# traditionnly, the median blur method has been most effective when removing salt-and-pepper noise
blurred = np.hstack([image, cv2.medianBlur(image,3), cv2.medianBlur(image,5), cv2.medianBlur(image,7)])
cv2.imshow("Median", blurred)
cv2.waitKey(0)

# bilateral blurring
# in cv2.bilateralFilter function, the first argument is the image, the second is the size on which we apply the kernel, for exemple 5 means 5*5. 
# The 3rd argument is the spatial sigma, that is, pixels that appear close together in the (x,y) coordinate space of the iamge will be considered.
# The 4th argument is the color sigam, ensuring that only pixels with similar intensity are included in the actual computation of the blur
blurred = np.hstack([image, cv2.bilateralFilter(image,5, 21, 21), cv2.bilateralFilter(image,7, 31, 31), cv2.bilateralFilter(image,9, 41, 41)])
cv2.imshow("Bilateral", blurred)
cv2.waitKey(0)