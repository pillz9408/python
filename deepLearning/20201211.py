### 이미지 처리 ###
import cv2 as cv
import numpy as np

# Read image with option

# original_image = cv.imread('C:\\Users\\honesty\\Desktop\\test2.jpg', cv.IMREAD_COLOR)
original_image = cv.imread('./peng.jpg', cv.IMREAD_COLOR)
gray_image = cv.imread('./peng1.jpg', cv.IMREAD_GRAYSCALE)

#BGR 채널 분해 조립
b, g, r = cv.split(original_image) #나누기
inverse_bgr = cv.merge((r, g, b)) #합치기
inverse = cv.bitwise_not(original_image) #비트단위로 쪼개기
mask_red = original_image.copy();mask_green = original_image.copy();mask_blue = original_image.copy()
mask_red[:,:, 1] = 0  # bgr 순서대로 뭘 잡는다..
mask_red[:,:, 0] = 0
mask_green[:,:, 2] = 0
mask_green[:,:, 0] = 0
mask_blue[:,:, 2] = 0
mask_blue[:,:, 1] = 0

#변환처리 : Warp
height, width, channel = original_image.shape

# srcPoint=np.array([[300, 200], [400, 200], [500, 500], [200, 500]], dtype=np.float32)
# dstPoint=np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)
srcPoint=np.array([[30, 80], [400, 80], [400, 300], [30, 300]], dtype=np.float32)
dstPoint=np.array([[10, 10], [390, 100], [200, 350], [180, 350]], dtype=np.float32)
matrix = cv.getPerspectiveTransform(srcPoint, dstPoint)

warp_image = cv.warpPerspective(original_image, matrix, (width, height))

cv.imshow('Original', original_image)
# cv.imshow("Blue", mask_blue)
# cv.imshow("Green", mask_green)
# cv.imshow("Red", mask_red)
# cv.imshow("BGR <-> RGB", inverse_bgr)
# cv.imshow("inverse", inverse)
cv.imshow("Warp Perspective", warp_image)

cv.waitKey(0)
cv.destroyAllWindows()