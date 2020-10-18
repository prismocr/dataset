import random
from PIL import ImageChops


def rotate(im, amount):
    """ rotate image

    :param im: image
    :param amount: 0 <= value <= 360
    :return: im
    """
    rand = int(random.random() * amount)
    side = -1 if round(random.random()) == 0 else 1
    return im.rotate(side * rand, fillcolor=(255, 255, 255))


def shift(im, amount):
    """ shift image

    :param im: image
    :param amount: amount to shift, could have issues if letter is out of bounds, (20 max seems right)
    :return: im
    """
    randx = int(random.random() * amount)
    randy = int(random.random() * amount)
    return ImageChops.offset(im, randx, randy)
