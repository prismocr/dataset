import os
from generate import *
from google_drive_downloader import GoogleDriveDownloader as gdd
import shutil
import zipfile

def compare_version(local, online):
    return online > local


def pull(path):
    path_tmp = os.path.join(path, "tmp")
    path_dataset = os.path.join(path, "dataset")
    print("Creating tmp folder")
    if not mkdir(path_tmp):
        print("failed to create tmp folder")
        print("Removing tmp folder")
        shutil.rmtree(path_tmp, ignore_errors=True)
        mkdir(path_tmp)
        if not mkdir(path_tmp):
            print("failed to create tmp folder")
    
    link_version = "1KDDPNgCE7AJbg3nBObsxyeqm9pPmBBjl"
    link_zip = "1BPmSzEkMmkfD_LIZP-xoYw_BSOkJcvU5"

    path_tmp_version = os.path.join(path_tmp, "version.txt")
    path_tmp_dataset_zip = os.path.join(path_tmp, "dataset.zip")
    path_dataset_version = os.path.join(path_dataset, "version.txt")

    try:
        gdd.download_file_from_google_drive(file_id=link_version, dest_path=path_tmp_version)
    except:
        print("failed to download version file")
        return
    
    if not os.path.exists(path_dataset):
        generate_dataset_directories(path)

    try:
        with open(path_dataset_version, "r") as f_local_version:
            local_version = f_local_version.readline()
    except FileNotFoundError:
        local_version = "!"

    with open(path_tmp_version, "r") as f_online_version:
        online_version = f_online_version.readline()

    if compare_version(local_version, online_version):
        print(f"New version available, removing version \"{local_version}\"")

        try:
            gdd.download_file_from_google_drive(file_id=link_zip, dest_path=path_tmp_dataset_zip)
        except:
            print("failed to download dataset zip file")
            return

        with open(path_dataset_version, 'w') as f_local_version:
            f_local_version.write(str(online_version))

        shutil.rmtree(path_dataset, ignore_errors=True)

        path_dataset_zip = os.path.join(path, "dataset.zip")
        if os.path.exists(path_dataset_zip):
            print("Removing old dataset.zip")
            os.remove(path_dataset_zip)
        shutil.move(path_tmp_dataset_zip, path_dataset_zip)
        print(f"Unzipping version \"{online_version}\"")
        unzip(path)
    
    else:
        print("Version up to date")
    print("Removing tmp folder")
    shutil.rmtree(path_tmp, ignore_errors=True)
