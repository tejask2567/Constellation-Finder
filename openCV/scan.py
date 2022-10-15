import cv2 as cv

#img = cv.imread('Images/Sample.jpg')

#cv.imshow('Star', img)
# cv.waitKey(0)


cap = cv.VideoCapture('Video/Sample.mp4')
if (cap.isOpened() == False):
    print("Error opening video stream or file")

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow('Frame', frame)
        if cv.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv.destroyAllWindows()
