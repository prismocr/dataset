import os
from PIL import Image, ImageDraw, ImageFont
from utils import *
from matplotlib import font_manager


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
        uppercase_path = os.path.join(local_path, "uppercase")
        lowercase_path = os.path.join(local_path, "lowercase")
        mkdir(uppercase_path)
        mkdir(lowercase_path)


def generate_dataset(path: str, fonts, fonts_path, font_size=28):
    n = 0
    path = os.path.join(path, "dataset")
    for font, font_path in zip(fonts, fonts_path):
        n += 1
        for i in range(26):
            char = chr(97 + i)
            local_path = os.path.join(path, char)
            uppercase_path = os.path.join(local_path, f"uppercase")
            lowercase_path = os.path.join(local_path, f"lowercase")
            try:
                fnt = ImageFont.truetype(font, font_size)
                write_on_image(fnt, chr(65 + i), uppercase_path, font)
                write_on_image(fnt, char, lowercase_path , font)
            except:
                print(f"Font : {font_path} is not loadable")
                n -= 1
                break
    print(f"saved {n} fonts")
        

def get_clear_font_name(fonts):
    clear = []
    for font in fonts:
        clear.append(os.path.split(font.strip(".ttf"))[-1])
    return clear


def write_on_image(font, text :str, path_to_save :str, font_name :str, size=(28, 28)):
    width, height = size
    img = Image.new("L", (width, height), color=0)
    draw = ImageDraw.Draw(img)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    draw.text(((width-w)/2, (height-h)/2), text=text, fill='white', font=font)
    path_to_save = os.path.join(path_to_save, f"{font_name.lower()}.bmp")
    img.save(path_to_save)


def get_all_fonts():
    fonts = []
    for x in font_manager.win32InstalledFonts():
        x = x[::-1]
        dot = x.find('.')
        slash = x.find('\\')
        x = x[slash-1:dot:-1]
        fonts += [x]
    fonts.sort()
    return fonts
    