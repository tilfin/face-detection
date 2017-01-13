from os import path
import cv2
import dlib


class FaceDetector:
    def detect(self):
        raise NotImplementedError


class DlibCVFaceDetector(FaceDetector):

    def __init__(self):
        self.face_detector = dlib.get_frontal_face_detector()

    def detect(self, image):
        #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        results = self.face_detector(image, 1)
        if (results is None):
            return ()

        rects = []
        for face in results:
            left = face.left()
            top = face.top()
            right = face.right()
            bottom = face.bottom()
            rects.append((top, bottom, left, right))

        return rects


class OpenCVFaceDetector(FaceDetector):

    def __init__(self):
        dir_path = path.dirname(path.abspath( __file__ ))
        cascade_path = dir_path + "/haarcascade_frontalface_default.xml"
        self.face_cascade = cv2.CascadeClassifier(cascade_path)
        self.min_size = (100, 100)

    def detect(self, image):
        results = self.face_cascade.detectMultiScale(image, 1.1, 3,
                                    minSize=self.min_size)
        if (results is None):
            return ()

        rects = []
        for (x, y, w, h) in results:
            left = x
            top = y
            right = x + w
            bottom = y + h
            rects.append((top, bottom, left, right))

        return rects
