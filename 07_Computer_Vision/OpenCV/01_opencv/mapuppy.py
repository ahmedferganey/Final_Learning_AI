import cv2

img = cv2.imread('../ref/Computer-Vision-with-Python/Computer-Vision-with-Python/DATA/00-puppy.jpg')


while True:
    cv2.imshow('puppy', img)

    if cv2.waitKey(1) & 0Xff == 27:
        break

cv2.destroyAllWindows()