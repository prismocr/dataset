from generate import *
from matplotlib import font_manager



if __name__ == "__main__":
    path = os.getcwd()
    fonts = get_all_fonts()

    fonts_clear = get_clear_font_name(fonts)
    generate_directories(path)
    generate_dataset(path, fonts_clear, fonts)
