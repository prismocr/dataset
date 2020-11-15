from generate import *
from matplotlib import font_manager



if __name__ == "__main__":
    path = os.getcwd()
    fonts = get_all_fonts()

    #region fonts_to_remove
    fonts_to_remove = [
    "AmiriQuran",
    "EmojiOneColor-SVGinOT",
    "Inkfree",
    "KacstBook",
    "KacstOffice",
    "MiriamCLM-Book",
    "NotoKufiArabic-Regular",
    "NotoNaskhArabic-Bold",
    "NotoNaskhArabic-Regular",
    "NotoNaskhArabicUI-Bold",
    "NotoNaskhArabicUI-Regular",
    "NotoSansArabic-Bold",
    "NotoSansArabic-Regular",
    "NotoSansArabicUI-Bold",
    "NotoSansArabicUI-Regular",
    "NotoSansArmenian-Bold",
    "NotoSansArmenian-Regular",
    "NotoSansGeorgian-Bold",
    "NotoSansGeorgian-Regular",
    "NotoSansHebrew-Bold",
    "NotoSansHebrew-Regular",
    "NotoSansLao-Bold",
    "NotoSansLao-Regular",
    "NotoSansLisu-Regular",
    "NotoSerifArmenian-Bold",
    "NotoSerifArmenian-Regular",
    "NotoSerifGeorgian-Bold",
    "NotoSerifGeorgian-Regular",
    "NotoSerifHebrew-Bold",
    "NotoSerifHebrew-Regular",
    "NotoSerifLao-Bold",
    "NotoSerifLao-Regular",
    "Scheherazade-Regular",
    "himalaya",
    "holomdl2",
    "opens___",
    "segmdl2",
    "segoesc",
    "sylfaen",
    "webdings",
    "wingding",
    "MiriamCLM-Bold",
    "NotoKufiArabic-Bold",
    "segoescb",
    "symbol"
    ]
    #endregion fonts_to_remove

    remove_fonts(fonts, fonts_to_remove)
    #fonts = ["calibri.ttf", "LiberationSerif-Regular.ttf", "arial.ttf", "georgia.ttf", "DejaVuSans.ttf"]

    fonts_clear = get_clear_font_name(fonts)
    generate_dataset_directories(path)
    generate_dataset(path, fonts_clear, fonts)
