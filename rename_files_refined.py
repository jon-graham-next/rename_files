import os, sys, re, glob

def rename_utility(directory, chars_to_change, new_chars):
    changed_file_count = 0
    for fname in glob.glob(directory + '**/*', recursive=True):
        if fname.endswith('rename_files', 'rename_files_refined'):
            continue
        elif chars_to_change not in fname:
            continue
        else:
            changed_file_count += 1
            new_fname = fname.replace(chars_to_change, new_chars)
            os.rename(fname, new_fname)
    print(str(changed_file_count) + " changed files\n")

def capitalise_utility(directory):
    changed_file_count = 0
    for fname in glob.glob(directory + '**/*', recursive=True):
        if fname.endswith('rename_files', 'rename_files_refined'):
            continue
        else:
            changed_file_count += 1
            s = re.sub("(^|\s)(\S)", lambda m: m.group(1) + m.group(2).title(), os.path.splitext(fname)[0])
            new_fname = s + os.path.splitext(fname)[1]
            os.rename(fname, new_fname)
    print(str(changed_file_count) + " affected files\n")

if __name__ == '__main__':
    while True:
        print("Menu:")
        print("Select 1 to use rename utility")
        print("Select 2 to use capitalise utility")
        print("Select 3 to quit\n")

        try:
            selection = int(input('Select option: '))
        except ValueError:
            print("Invalid selection, please try again.\n")
            continue

        if selection == 1:
            # Rename utility
            directory = input("Enter directory path: ")
            chars_to_change = input("Enter char(s) to change: ")
            new_chars = input("Enter new char(s): ")
            rename_utility(directory, chars_to_change, new_chars)

        elif selection == 2:
            # Capitalise utility
            directory = input("Enter directory path: ")
            capitalise_utility(directory)

        elif selection == 3:
            # Quit
            sys.exit()

        else:
            print("Invalid selection, please try again.\n")
