import os
import shutil


def remove_folder(path):
    if os.path.exists(path):
        shutil.rmtree(path)


def make_folder(path):
    if os.path.exists(path) is False:
        os.mkdir(path)


def get_filelist(path):
    filelist = os.listdir(path)
    if len(filelist) == 0:
        filelist = None
    return filelist
