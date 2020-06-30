"""
Prints the absolute path (in python-readable form) of files in a specified directory to the console
"""
import os, sys
binName = 'listFiles'

def main():
    targetDir = ''
    
    try:
        targetDir = sys.argv[1]
    except:
        print("usage:  " + binName + " <DirectoryAbsolutePath>")
        exit

    os.chdir(targetDir)
    files = os.listdir()

    for i in files:
        print(targetDir +  i)

if __name__ == '__main__':
    main()
