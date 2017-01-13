import cv2


class DetectionViewer:

    def __init__(self, bgr_image):
        self.image = bgr_image

    def draw_rects(self, rects, bgr_color=(255, 255, 255)):
        for rect in rects:
            self.draw_rect(rect, bgr_color)

    def draw_rect(self, rect, bgr_color):
        cv2.rectangle(self.image, (rect[2], rect[0]), (rect[3], rect[1]),
                    bgr_color, 2)

    def show(self):
        cv2.imshow("result", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
