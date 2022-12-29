import zipfile
from tqdm import tqdm

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        return password
    except:
        return

def main():
    fileName = input("Insert the name of the file:")
    zFile = zipfile.ZipFile(fileName)
    wordList = input("Insert the name of the wordlist:")
    passFile = open(wordList, mode="r", encoding="latin-1")

    for line in tqdm(passFile.readlines()):
        password = line.strip("\n")
        guess = extractFile(zFile, password)
        if guess:
            print("[+] Password = " + password + "\n")
            exit(0)
    print("[-] Password not found.")

if __name__ == '__main__':
    main()
