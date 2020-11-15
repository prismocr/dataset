import os
import csv
from PIL import Image, ImageDraw, ImageFont
from utils import *
from matplotlib import font_manager
import zipfile


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


def generate_dataset(path: str, fonts, fonts_path, version, font_size=36):
    n = 0
    index = 1
    path_to_csv = os.path.join(path, "dataset", "data.csv")
    path_to_version = os.path.join(path, "dataset", "version.txt")
    path = os.path.join(path, "dataset", "images")
    with open(path_to_version, "w") as f_version:
        f_version.write(str(version))

    with open(path_to_csv, "w", newline='', encoding='utf-8') as f_csv: 
        f_writer = csv.writer(f_csv, delimiter='§')
        for font, font_path in zip(fonts, fonts_path):
            try:
                fnt = ImageFont.truetype(font, font_size)
            except:
                print(f"Font : {font_path} is not loadable")
                continue
            n += 1
            for i in range(26):  # Letters
                chars = [chr(97 + i), chr(65 + i)]
                for char in chars:
                    filename = f"image_{index}.bmp"
                    write_on_image(fnt, char, path, filename)
                    index += 1
                    f_writer.writerow([char] + [filename] + [font])
            for i in range(33, 65):  # Specials Chars
                char = chr(i)
                filename = f"image_{index}.bmp"
                write_on_image(fnt, char, path, filename)
                index += 1
                f_writer.writerow([char] + [filename] + [font])

                
        print(f"saved {n} fonts")
        

def get_clear_font_name(fonts):
    clear = []
    for font in fonts:
        clear.append(os.path.split(font.strip(".ttf"))[-1])
    return clear


def write_on_image(font, text :str, path_to_save :str, name_to_save :str, size=(40, 40)):
    width, height = size
    img = Image.new("RGB", (width, height), color=0)
    draw = ImageDraw.Draw(img)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    draw.text(((width-w)/2, (height-h)/2), text=text, fill='white', font=font)
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