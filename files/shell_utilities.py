# here we will look over the shell utilities. There are used to manipulate files and directories

import os
from os import path
import shutil  # this is the shell utilities lib
from shutil import make_archive  # this is used to make a zip file
# this is used to have a greater control over the zip file
from zipfile import ZipFile


def main():
    if path.exists("mytext.txt"):
        # lets do a copy of the file
        src = path.realpath("mytext.txt")
        # 1st we should back a backup of the file, and define the destination
        dst = src + ".bak"
        # 2nd we should copy the file
        # shutil.copy(src, dst)  # this copies the file into a backup destination

        # renaming the file:
        # os.rename("mytext.txt.bak", "newfile_backup.txt")

        # lets make a zip of this directory
        # -- here '[0]' is used to get the path only and not the full scr
        # dir = path.split(path.realpath("newfile_backup.txt"))[0]
        # -- this creates a zip file of the directory, the first parameter is the name of the archive
        # shutil.make_archive("my_zipper", "zip", dir)

        # lets have a greater control over the files using hte zip file lib
        # --'with' allows us to create a local scope
        # this creates a new zip file and allows to write it
        with ZipFile("testzip.zip", "w") as newzip:
            # this will add the file to the zip manually
            newzip.write("mytext.txt")
            newzip.write("newfile_backup.txt")


if __name__ == "__main__":
    main()
