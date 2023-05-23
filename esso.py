import os
import sys
import zipfile
import rarfile
from tqdm import tqdm

def print_banner():
    print(r"""
      ___           ___           ___           ___     
     /  /\         /  /\         /  /\         /  /\    
    /  /::\       /  /::\       /  /::\       /  /::\   
   /  /:/\:\     /__/:/\:\     /__/:/\:\     /  /:/\:\  
  /  /::\ \:\   _\_ \:\ \:\   _\_ \:\ \:\   /  /:/  \:\ 
 /__/:/\:\ \:\ /__/\ \:\ \:\ /__/\ \:\ \:\ /__/:/ \__\:\
 \  \:\ \:\_\/ \  \:\ \:\_\/ \  \:\ \:\_\/ \  \:\ /  /:/
  \  \:\ \:\    \  \:\_\:\    \  \:\_\:\    \  \:\  /:/ 
   \  \:\_\/     \  \:\/:/     \  \:\/:/     \  \:\/:/  
    \  \:\        \  \::/       \  \::/       \  \::/   
     \__\/         \__\/         \__\/         \__\/    
    """)
    print("Esso - Easy and Simple Zip/Rar cracker")
    print("Author: @Nembie")

def print_help():
    print("Usage: python esso.py -f <file_name> -w <wordlist_name>")
    print("Options:")
    print("-f <file_name>     Specify the name of the file to crack")
    print("-w <wordlist_name> Specify the name of the wordlist to use")
    print("-h                 Print this help")

def extract_zip_file(z_file, password):
    try:
        z_file.extractall(pwd=bytes(password, 'utf-8'))
        return password
    except Exception:
        return None

def zip_worker(file_name, wordlist_lines):
    # Open the protected file only once
    try:
        protected_file = zipfile.ZipFile(file_name)
    except zipfile.BadZipFile:
        print("[-] Invalid zip file.")
        exit(0)

    # For each line in the wordlist, try to extract the file
    for line in tqdm(wordlist_lines):
        password = line.strip("\n")
        guess = extract_zip_file(protected_file, password)
        # If the password is correct, print it and exit
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
    # If parameter -f is used, the file name is the first parameter, otherwise it is asked to the user
    file_name = (sys.argv[2] if len(sys.argv) > 2 and sys.argv[1] == "-f" else input("Insert the name of the file: "))
    # If parameter -w is used, the wordlist name is the third parameter, otherwise it is asked to the user
    word_list = (sys.argv[4] if len(sys.argv) > 4 and sys.argv[3] == "-w" else input("Insert the name of the wordlist: "))

    # Get filename and wordlist, If the file or the wordlist doesn't exist, exit
    if not os.path.exists(file_name) or not os.path.exists(word_list):
        print("[-] File or wordlist not found.")
        exit(0)

    # Read all lines from the wordlist at once
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
    if len(sys.argv) > 1 and sys.argv[1] == "-h":
        print_help()
        exit(0)
    try:
        main()
    except KeyboardInterrupt:
        print("\n[-] Exiting...")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
