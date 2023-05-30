# THIS SCRIPT WILL ENABLE YOU TO BULK RENAME FILES & BULK CAPITALISE FILENAMES.
#
# RUN IT FROM THE DIRECTORY THAT CONTAINS THE FILES YOU WISH TO EDIT.
#
# THE RENAME FUNCTION WORKS BY ASKING YOU FOR A STRING OF CHARACTERS THAT
# YOU WANT TO CHANGE AND A STRING OF CHARACTERS THAT YOU WANT TO REPLACE
# THEM WITH. IT WILL APPLY THE CHANGE TO ALL FILES IN THE CURRENT DIRECTORY
# AND SUBDIRS THAT CONTAIN THE STRING OF CHARS TO CHANGE.
#
# THE CAPITALISE FUNCTION WILL RENAME ALL FILES IN THE CURRENT DIRECTORY AND
# ALL SUBDIRS, SO THAT EACH WORD BEGINS WITH A CAPITAL LETTER.
#
# THE MENU WILL REPEAT AFTER EACH SUCCESSFUL EXECUTION UNTIL THE PROGRAM
# IS QUIT.
#
# JON GRAHAM, SEPT 2019


import os, sys
import glob
import re
from pathlib import Path, PurePath

rootdir = os.getcwd()


def menu():
    print("Menu:")
    print("Select 1 to use rename utility")
    print("Select 2 to use capitalise utility")
    print("Select 3 to quit\n")


def selection():
    selection = int(input('Select option: '))
    return selection


def rename_utility():
    chars_to_change = input("Enter char(s) to change: ")
    new_chars = input("Enter new char(s): ")
    changed_file_count = 0
    for fname in glob.glob(os.path.join(rootdir, '**/*'), recursive=True):
        path = os.path.join(rootdir, fname)
        if os.path.isdir(path):
            # skip directories
            continue
        elif (chars_to_change.lower() == "stop") or (new_chars.lower() == "stop"):
            sys.exit()
        elif PurePath(fname).stem == 'rename_files':
            continue
        else:
            if chars_to_change not in fname:
                continue
            changed_file_count += 1
            os.rename(fname, fname.replace(chars_to_change, new_chars))
    print(str(changed_file_count) + " changed files\n")


def repl_func(m):
    # process regular expression match groups for word upper-casing problem
    return m.group(1) + m.group(2).upper()


def capitalise_utility():
    changed_file_count = 0
    for fname in glob.glob(os.path.join(rootdir, '**/*'), recursive=True):
        path = os.path.join(rootdir, fname)
        s = PurePath(fname).stem
        s = re.sub("(^|\s)(\S)", repl_func, s)
        if os.path.isdir(path):
            # skip directories
            continue
        elif PurePath(fname).stem == 'rename_files':
            continue
        else:
            changed_file_count += 1
            os.rename(fname, fname.replace(PurePath(fname).stem, s))
    print(str(changed_file_count) + " affected files\n")


if __name__ == '__main__':
    while True:
        menu()
        c = selection()
        if c == 1:
            rename_utility()
        elif c == 2:
            capitalise_utility()
        elif c == 3:
            sys.exit()
        else:
            print("Invalid selection, please try again.\n")
