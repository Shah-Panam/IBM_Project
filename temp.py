import cv2

# Load the two images to be compared
img1 = cv2.imread("/workspaces/IBM_Project/image1.jfif")
img2 = cv2.imread("/workspaces/IBM_Project/Imagek.jfif")

# Convert images to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Detect keypoints and extract using SIFT
sift = cv2.xfeatures2d.SIFT_create()
keypoints1, descriptors1 = sift.detectAndCompute(gray1, None)
keypoints2, descriptors2 = sift.detectAndCompute(gray2, None)

# Use FLANN library to match the keypoints and return copy of it
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(descriptors1, descriptors2, k=2)

# Matches using Lowe's ratio test
good_matches = []
for m, n in matches:
    if m.distance < 0.7*n.distance:
        good_matches.append(m)

# Draw the matches on the images
img_matches = cv2.drawMatches(img1, keypoints1, img2, keypoints2, good_matches, None, flags=2)

#Image with the matches
cv2.imshow("Matches", img_matches)
cv2.waitKey(0)
cv2.destroyAllWindows()