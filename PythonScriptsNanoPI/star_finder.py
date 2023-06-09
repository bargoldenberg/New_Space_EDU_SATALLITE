import numpy as np
import cv2
import sys

# main runing function
def get_stars(image, size, threshold=127):
    circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 2, 20,
                               param1=250, param2=1, minRadius=2, maxRadius=6)

    # no need for more that 20 star, try to reduce the number
    desired_size = 20
    length = len(circles[0, :])
    if length > desired_size:
        for t in range(1, 6):
            circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 20,
                                       param1=250, param2=t, minRadius=2, maxRadius=6)
            length = len(circles[0, :])
            if length < desired_size:
                break

    if circles is None:
        return []
    circles = np.uint16(np.around(circles))
    circles_cordinates = []
    for i in circles[0, :]:
        if i[0] < size[0] and i[1] < size[1]:
            circles_cordinates.append(
                (int(i[0]), int(i[1]), i[2] + 5,  int(image[i[0], i[1]])))

    return circles_cordinates


def get_stars_coordinates(filepath='./fr1.jpg', size=(600, 600)):
    img1 = np.array(cv2.resize(cv2.imread(filepath), size))
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    return get_stars(img1_gray, size)


# run main function
if __name__ == '__main__':
    filepath = None
    if len(sys.argv) >= 2:
	filepath = sys.argv[1]
    
    print(get_stars_coordinates(filepath))
