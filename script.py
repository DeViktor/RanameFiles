import runpy
import os
import shutil

folder = r'C:\Users\DeViktor\Documents\resources'


def renameFile(file):
    fileName, fileExtension = os.path.splitext(file)
    shortFileName = fileName.split('-')
    if shortFileName[0] == "gloves":
        return f'{fileName.replace(fileName, "Gloves-Dark")}{fileExtension}'
    if shortFileName[0] == "cloth":
        return f'{fileName.replace(fileName, "Cloth-Dark")}{fileExtension}'
    if shortFileName[0] == "skin":
        return f'{fileName.replace(fileName, "Skin-Dark")}{fileExtension}'

    return fileName, fileExtension


def fileLoop(root, dirs, files):
    for file in files:
        renamed = renameFile(file)
        # print(renamed[0],"\n")
        print(renamed)


def loop():
    for root, dirs, files in os.walk(folder):
        fileLoop(root, dirs, files)


if __name__ == '__main__':
    loop()
