import cv2

def rotateImage(image, code):
    rotated = cv2.rotate(image,code)
    return rotated

def resizeImage(cols, rows, image):
    resized = cv2.resize(image,(cols, rows))
    return resized

if __name__ == "__main__":
    image = cv2.imread("moon.jpg")
    cv2.imshow("Moon", image)

    resized_image = resizeImage(800, 1500, image)
    cv2.imshow("resized moon", resized_image)

    rotated_image = rotateImage(image, cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow("rotated moon", rotated_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()