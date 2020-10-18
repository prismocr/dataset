import os
from PIL import Image
from utils import *


def mkdir(path):
    """ generate directory

    :param path: local path
    :return: None
    """
    try:
        if not os.path.exists(path):
            os.mkdir(path)
    except OSError:
        print(f"Creation of the directory {path} failed")


def generate_directories(path):
    """ generate directories

    :param path: local path
    :return:  None
    """
    path = os.path.join(path, "dataset")
    mkdir(path)
    for i in range(26):
        local_path = os.path.join(path, chr(97 + i))
        mkdir(local_path)
        mkdir(os.path.join(local_path, "clear"))


def generate_dataset_clear(path):
    """ generate a clear dataset if the folders exist

    :param path: local path
    :return: None
    """
    path_letter_init = os.path.join(path, "alphabet")
    path = os.path.join(path, "dataset")
    for i in range(26):
        local_path = os.path.join(path, chr(97 + i))
        path_letter = os.path.join(path_letter_init, chr(97 + i))

        path_load = path_letter + ".png"
        im_init = Image.open(path_load)

        for j in range(0, 10):
            im_offset = shift(im_init, 2 * (j + 1))
            path_save = os.path.join(local_path, os.path.join("clear", f"offset_{j}.png"))
            im_offset.save(path_save)
            im = rotate(im_offset, 2 * (j + 1))
            path_save = os.path.join(local_path, os.path.join("clear", f"offset_rotate_{j}.png"))
            im.save(path_save)
