import sys
import cv2
from mylib.detection_viewer import DetectionViewer
from mylib.face_detector import *


if len(sys.argv) != 2:
    sys.exit("argument error")

file_path = sys.argv[1]

bgr_img = cv2.imread(file_path)
rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)

viewer = DetectionViewer(bgr_img)

dlib_detector = DlibCVFaceDetector()
opencv_detector = OpenCVFaceDetector()

rects = opencv_detector.detect(bgr_img)
viewer.draw_rects(rects, bgr_color=(255, 0, 255)) # Magenta

rects = dlib_detector.detect(rgb_img)
viewer.draw_rects(rects, bgr_color=(0, 255, 0)) # Lime green

viewer.show()
