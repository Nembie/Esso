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