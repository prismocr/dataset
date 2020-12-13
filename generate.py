import os
import csv
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from utils import *
from matplotlib import font_manager
import zipfile
from skimage.measure import block_reduce

def mkdir(path):
    """ generate directory

    :param path: local path
    :return: None
    """
    try:
        if not os.path.exists(path):
            os.mkdir(path)
            return True
    except OSError:
        print(f"Creation of the directory {path} failed")
        return False


def generate_dataset_directories(path):
    path = os.path.join(path, "dataset")
    mkdir(path)
    path = os.path.join(path, "images")
    mkdir(path)


def generate_dataset(path: str, fonts, fonts_path, version, font_size=24):
    n = 0
    index = 1
    path_to_csv = os.path.join(path, "dataset", "data.csv")
    path_to_version = os.path.join(path, "dataset", "version.txt")
    path = os.path.join(path, "dataset", "images")
    with open(path_to_version, "w") as f_version:
        f_version.write(str(version))

    with open(path_to_csv, "w", newline='', encoding='utf-8') as f_csv: 
        f_writer = csv.writer(f_csv, delimiter='§')
        i = 0
        while(fonts):
            fonts_index = random.randrange(0, len(fonts))
            font, font_path = fonts[fonts_index], fonts_path[fonts_index]
        # for font, font_path in zip(fonts, fonts_path):
            try:
                fnt = ImageFont.truetype(font, font_size)
            except:
                print(f"Font : {font_path} is not loadable")
                fonts.pop(fonts_index)     
                fonts_path.pop(fonts_index)
                continue
            n += 1
            for r in range(1, 4, 2):
                for i in range(26):  # Letters
                    chars = [chr(97 + i), chr(65 + i)]
                    for char in chars:
                        filename = f"image_{index}.bmp"
                        write_on_image(fnt, char, path, filename, r)
                        index += 1
                        f_writer.writerow([char.lower()] + [filename] + [font])
                
                i_dont_want_u = ["#", "$", "%", "&", "+", "*", "<", ">", "=", "@", "/"]
                for i in range(33, 65): #(33, 65):  # Specials Chars
                    char = chr(i)
                    if char in i_dont_want_u:
                        continue
                    filename = f"image_{index}.bmp"
                    write_on_image(fnt, char, path, filename, r)
                    index += 1
                    f_writer.writerow([char] + [filename] + [font])

            fonts.pop(fonts_index)       
            fonts_path.pop(fonts_index)       
        print(f"saved {n} fonts")
        

def get_clear_font_name(fonts):
    clear = []
    for font in fonts:
        clear.append(os.path.split(font.strip(".ttf"))[-1])
    return clear



def check_black_row(img, row, size):
    for i in range(size):
        if img[i][row][0]:
            return True
    return False

def check_black_col(img, col, size):
    for i in range(size):
        if img[col][i][0]:
            return True
    return False

def trim(img, size, space):
    left = right = top = bot = 0

    for i in range(size):
        if check_black_col(img, i, size):
            top = i
            break

    for i in range(size):
        if check_black_row(img, i, size):
            left = i
            break

    for i in range(size):
        if check_black_col(img, size-i-1, size):
            bot = size-i
            break

    for i in range(size):
        if check_black_row(img, size-i-1, size):
            right = size-i
            break

    """
    if (right - left < 6):
        right += 3
        left -= 3

    if (bot - top < 6):
        bot += 3
        top -= 3

    """

    top -= space
    bot += space
    right += space
    left -= space
    
    if top < 0:
        top = 0
    
    if left < 0:
        left = 0

    if bot >= size:
        bot = size-1
    
    if right >= size:
        right = size-1

    return left, top, right, bot

def resize(im, d1, d2, size):
    #print("resize", d1, d2, d1/28, d2/28)
    shape = im.size
    if d1 > d2:
        ratio = 28*d2/d1
        img = im.resize((size, int(ratio)))
    else:
        ratio = ratio = 28*d1/d2
        img = im.resize((int(ratio), size))
    return img

def add_black(im, size_m):
    shape = im.size    
    image = Image.new('RGB', (size_m, size_m))
    if shape[0] == size_m:
        obj = size_m - shape[1]
        if not obj:
            return im
        image.paste(im, (0, obj//2))
        return image
    else:
        obj = size_m - shape[0]
        if not obj:
            return im
        image.paste(im, (obj//2, 0))
        return image

def write_on_image(font, text :str, path_to_save :str, name_to_save :str, space :int, size=(28, 28)):
    width, height = size
    img = Image.new("RGB", (width, height), color=0)
    draw = ImageDraw.Draw(img)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.2)
    draw.text(((width-w)/2, (height-h)/2), text=text, fill='white', font=font)

    np_im = np.array(img)
    left, top, right, bottom = trim(np_im, size[0], space)

    img = img.crop((left, top, right, bottom))
    #print(img.size)
    #print(name_to_save)
    img = resize(img, right - left, bottom - top, size[0])
    #print(img.size)
    img = add_black(img, size[0])
    ##print(img.size)
    #print()

    path_to_save = os.path.join(path_to_save, name_to_save)
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
    

def remove_fonts(fonts :list, fonts_to_remove :list):
    for font in fonts_to_remove:
        try:
            fonts.remove(font)
        except:
            print(f"font : {font} could not be remove")


def zip_dataset():
    zipf = zipfile.ZipFile('dataset.zip', 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk("dataset"):
        for file in files:
            zipf.write(os.path.join(root, file))
    zipf.close()


def unzip(path):
    path_dataset = os.path.join(path, "dataset.zip")
    with zipfile.ZipFile(path_dataset, 'r') as zip_ref:
        zip_ref.extractall()
