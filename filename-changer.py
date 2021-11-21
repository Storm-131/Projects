# ---------------------------------------------------------*\
#  * Title: Filename-Changer
#  * Author: Tom Maus (2021)
# ---------------------------------------------------------*/
#!/usr/bin/env python3

import os

# 1) Set the directory w/ files to rename
dir = "/Users/tom/GitHub/Gotham-Python/Playground"
os.chdir(dir)


# 2) Set variable w/ Word to add:
var = "Fake_"


# 3) Apply the changes
def fileChanger():
    """ This can be used to change any filename in a folder by a given pattern """
    for filename in os.listdir(dir):
        os.rename(filename, var + filename)
        print("Successfully renamed: " + filename + " -> " + var + filename)


def fileRevert():
    for filename in os.listdir(dir):
        os.rename(filename, filename.replace(var, ""))
        print("Successfully renamed: " + filename +
              " -> " + filename.replace(var, ""))


# 4) Call the methods:
fileChanger()
# fileRevert()


# -------------------------Notes-----------------------------------------------*\
#
# -----------------------------------------------------------------------------*\
