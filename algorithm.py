import random


def salt_and_peper(im, amount):
    """ salt and peper algorithm

    :param im: image
    :param amount: 0 <= value <= 100
    :return: image
    """
    size = im.size
    for x in range(size[0]):
        for y in range(size[1]):
            rand = random.random()
            if rand < amount/100:
                value = (0, 0, 0) if int(rand*100) % 2 == 0 else (255, 255, 255)
                im.putpixel((x, y), value)
    return im
