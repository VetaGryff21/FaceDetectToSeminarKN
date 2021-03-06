import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
id = input('Enter user id: ')
sampleN = 0;

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        sampleN = sampleN + 1;
        cv2.imwrite("facesData/User." + str(id) +
                    "." + str(sampleN) + ".jpg", gray[y:y + h, x:x + w])
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.waitKey(100)
    cv2.imshow('img', img)
    cv2.waitKey(1)

    if sampleN > 200:
        break

cap.release()
cv2.destroyAllWindows()

#
# def grab(self):
#     if (self.video is None or self.faceClassifier is None):
#         logging.error('Either VideoCapture or Classifier is not available.')
#         return
#
#     # Grab image
#     ret, cameraFrame = self.video.read()
#     if (not ret):
#         return (None, [])
#
#     if (self.mirror):
#         cv2.flip(cameraFrame, 1)
#
#     # Detect faces
#     faces = self.faceClassifier.detectMultiScale(cameraFrame,
#                                                  scaleFactor=self.scaleFactor,
#                                                  minNeighbors=self.minNeighbors,
#                                                  minSize=(self.minWidth, self.minHeight),
#                                                  flags=cv2.cv.CV_HAAR_SCALE_IMAGE
#                                                  )
#
#     return (cameraFrame, faces)
#
#
# def terminate(self):
#     if (not self.video is None):
#         self.video.release()
#     logging.info('Terminating FaceDetector...')