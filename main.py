from generate import *
from matplotlib import font_manager
from gdrive import *

path = os.getcwd()

if __name__ == "__main__":
    while True:
        command = input("Command to run: ")

        if command == "exit":
            break

        elif command == "generate":
            version = input("Version: ")
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

            #fonts = ["calibri.ttf"]#, "LiberationSerif-Regular.ttf", "arial.ttf", "georgia.ttf", "DejaVuSans.ttf"]
            fonts2 = ["georgia.ttf", "arial.ttf", "calibri.ttf"]
            
            for _ in range(10):
                for f in fonts2:
                    if not f in fonts:
                        fonts.append(f)
            
            fonts_clear = get_clear_font_name(fonts)
            generate_dataset_directories(path)
            generate_dataset(path, fonts_clear, fonts, version)
            print("Zipping...")
            zip_dataset()

        elif command == "pull":
            pull(path)

        elif command == "unzip":
            unzip(path)

        elif command == "zip":
            zip_dataset()

        else:
            print("command is invalid")
