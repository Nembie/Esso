import sys
import zipfile
from tqdm import tqdm

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
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
    zFile = zipfile.ZipFile(fileName)

    # If parameter -w is used, the wordlist name is the third parameter, otherwise it is asked to the user
    if(len(sys.argv) > 4 and sys.argv[3] == "-w"):
        wordList = sys.argv[4]
    else:
        wordList = input("Insert the name of the wordlist:")
    
    # Open the wordlist
    passFile = open(wordList, mode="r", encoding="latin-1")

    # For each line in the wordlist, try to extract the file
    for line in tqdm(passFile.readlines()):
        password = line.strip("\n")
        guess = extractFile(zFile, password)
        # If the password is correct, print it and exit
        if guess:
            print("[+] Password = " + password + "\n")
            exit(0)
    print("[-] Password not found.")

if __name__ == '__main__':
    main()
