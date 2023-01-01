import os
import sys
import zipfile
from tqdm import tqdm

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd = bytes(password,'utf-8'))
        return password
    except:
        return

def main():
    # If parameter -h is used, the help is shown
    if(len(sys.argv) > 1 and sys.argv[1] == "-h"):
        print("Usage: python3 esso.py -f <file_path> -w <wordlist>")
        print("Example: python3 esso.py -f file.zip -w wordlist.txt")
        exit(0)
    
    # If parameter -f is used, the file name is the first parameter, otherwise it is asked to the user
    if(len(sys.argv) > 2 and sys.argv[1] == "-f"):
        fileName = sys.argv[2]
    else:
        fileName = input("Insert the name of the file:")

    # Get filename, If the filename doesn't exist, exit
    try:
        protectedFile = zipfile.ZipFile(fileName)
    except:
        print("[-] File not found.")
        exit(0)

    # If parameter -w is used, the wordlist name is the third parameter, otherwise it is asked to the user
    if(len(sys.argv) > 4 and sys.argv[3] == "-w"):
        wordList = sys.argv[4]
    else:
        wordList = input("Insert the name of the wordlist:")

    # Get wordlist, If the wordlist doesn't exist, exit
    try:
        passFile = open(wordList, mode="r", encoding="latin-1")
    except:
        print("[-] Wordlist not found.")
        exit(0)

    # For each line in the wordlist, try to extract the file
    for line in tqdm(passFile.readlines()):
        password = line.strip("\n")
        guess = extractFile(protectedFile, password)
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