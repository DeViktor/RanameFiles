import runpy
import os
import shutil

folder = r'C:\Users\DeViktor\Documents\resources'


def renameFile(file):
    fileName, fileExtension = os.path.splitext(file)
    return fileName, fileExtension


def fileLoop(root, dirs, files):
    for file in files:
        rename = renameFile(file)
        print(rename)


def loop():
    for root, dirs, files in os.walk(folder):
        fileLoop(root, dirs, files)


if __name__ == '__main__':
    loop()
