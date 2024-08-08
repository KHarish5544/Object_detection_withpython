import cv2
img = cv2.imread("1.png", cv2.IMREAD_COLOR)
cv2.imshow("image", img)
cv2.waitKey(0)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0)
Gaussian = cv2.GaussianBlur(img, (7, 7), 0)
cv2.imshow('Gaussian Blurring', Gaussian)
cv2.waitKey(0)
half = cv2.resize(img, (0, 0), fx = 0.1, fy = 0.1)
cv2.imshow("Resize",half)
cv2.waitKey(0)
image = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Rotate", image)
cv2.waitKey(0)
(h, w) = img.shape[:2]
print("Height",h,"\n","Width",w)
cv2.destroyAllWindows()