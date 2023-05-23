import os
import sys
import zipfile
import rarfile
from tqdm import tqdm
from func.helper import print_banner, print_help


def extract_zip_file(z_file, password):
    try:
        z_file.extractall(pwd=bytes(password, 'utf-8'))
        return password
    except Exception:
        return None


def zip_worker(file_name, wordlist_lines):
    try:
        protected_file = zipfile.ZipFile(file_name)
    except zipfile.BadZipFile:
        print("[-] Invalid zip file.")
        exit(0)

    for line in tqdm(wordlist_lines):
        password = line.strip("\n")
        guess = extract_zip_file(protected_file, password)
        if guess:
            print("[+] Password = " + password + "\n")
            exit(0)
    print("[-] Password not found.")


def rar_worker(rf, wordlist_lines):
    for line in tqdm(wordlist_lines):
        password = line.strip("\n")
        try:
            rf.setpassword(password)
            rf.extractall()
        except rarfile.BadRarFile:
            pass
        except:
            print("[+] Password found: " + password)
            exit(0)


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "-h":
        print_help()
        exit(0)

    file_name = sys.argv[2] if len(sys.argv) > 2 and sys.argv[1] == "-f" else input("Insert the name of the file: ")
    word_list = sys.argv[4] if len(sys.argv) > 4 and sys.argv[3] == "-w" else input("Insert the name of the wordlist: ")

    if not os.path.exists(file_name) or not os.path.exists(word_list):
        print("[-] File or wordlist not found.")
        exit(0)

    with open(word_list, mode="r", encoding="latin-1") as pass_file:
        wordlist_lines = pass_file.readlines()

    if zipfile.is_zipfile(file_name):
        zip_worker(file_name, wordlist_lines)
    elif rarfile.is_rarfile(file_name):
        with rarfile.RarFile(file_name) as rf:
            rar_worker(rf, wordlist_lines)
    else:
        print("[-] Invalid file type.")
        exit(0)


if __name__ == '__main__':
    print_banner()
    try:
        main()
    except KeyboardInterrupt:
        print("\n[-] Exiting...")
        sys.exit(0)
