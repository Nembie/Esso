import os
import sys
import zipfile
from tqdm import tqdm


def extract_file(z_file, password):
    try:
        z_file.extractall(pwd=bytes(password, 'utf-8'))
        return password
    except Exception:
        return None


def main():
    # If parameter -h is used, the help is shown
    if len(sys.argv) > 1 and sys.argv[1] == "-h":
        print("Usage: python3 esso.py -f <file_path> -w <wordlist>")
        print("Example: python3 esso.py -f file.zip -w wordlist.txt")
        exit(0)

    # If parameter -f is used, the file name is the first parameter, otherwise it is asked to the user
    if len(sys.argv) > 2 and sys.argv[1] == "-f":
        file_name = sys.argv[2]
    else:
        file_name = input("Insert the name of the file: ")

    # Get filename, If the filename doesn't exist, exit
    if not os.path.exists(file_name):
        print("[-] File not found.")
        exit(0)

    # If parameter -w is used, the wordlist name is the third parameter, otherwise it is asked to the user
    if len(sys.argv) > 4 and sys.argv[3] == "-w":
        word_list = sys.argv[4]
    else:
        word_list = input("Insert the name of the wordlist: ")

    # Get wordlist, If the wordlist doesn't exist, exit
    if not os.path.exists(word_list):
        print("[-] Wordlist not found.")
        exit(0)

    with open(word_list, mode="r", encoding="latin-1") as pass_file:
        # Read all lines from the wordlist at once
        wordlist_lines = pass_file.readlines()

    # Open the protected file only once
    try:
        protected_file = zipfile.ZipFile(file_name)
    except zipfile.BadZipFile:
        print("[-] Invalid zip file.")
        exit(0)

    # For each line in the wordlist, try to extract the file
    for line in tqdm(wordlist_lines):
        password = line.strip("\n")
        guess = extract_file(protected_file, password)
        # If the password is correct, print it and exit
        if guess:
            print("[+] Password = " + password + "\n")
            exit(0)

    print("[-] Password not found.")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nInterrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
