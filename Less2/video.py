import cv2

face_cascades = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


# img =cv2.imread("fave.jpg")
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# faces = face_cascades.detectMultiScale(img_gray)

# for (x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y), (x+w,y+h),(255 ,1, 55),1)
# cv2.imshow('1',img)
# cv2.waitKey(0)

cap = cv2.VideoCapture("D:\GBPhyton\OpenCV\IMG_0323.MOV")

while True:
    _, frame = cap.read()

    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascades.detectMultiScale(img_gray)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 1, 55), 3)
    cv2.imshow('1',frame)   
    if cv2.waitKey(123) & 0xff == ord('q'):
        break
