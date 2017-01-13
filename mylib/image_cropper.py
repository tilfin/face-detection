class ImageCropper(object):

    def __init__(self):

    def crop(self, image, rect):
        top = rect[0]
        bottom = rect[1]
        left = rect[2]
        right = rect[3]

        return image[top:bottom, left:right]
