import os
import sys
import zipfile
import rarfile
from tqdm import tqdm
from func.helper import print_banner
import argparse

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

def main(args):
    file_name = args.file
    word_list = args.wordlist

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
    parser = argparse.ArgumentParser(description="Zip/Rar password cracker.")
    parser.add_argument("-f", dest="file", help="File name", required=True)
    parser.add_argument("-w", dest="wordlist", help="Wordlist file name", required=True)
    args = parser.parse_args()

    print_banner()
    try:
        main(args)
    except KeyboardInterrupt:
        print("\n[-] Exiting...")
        sys.exit(0)
