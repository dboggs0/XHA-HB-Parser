import os, sys
binName = 'listFiles'

def main():
    lastDir = os.getcwd()
    targetDir = ''
    outFile = ''
    
    try:
        targetDir = sys.argv[1]
        outFile = sys.argv[2]
    except:
        print("usage:  " + binName + " <DirectoryAbsolutePath>")
        exit

    os.chdir(targetDir)
    
    files = os.listdir()

    #change back to where the script was run from to output to file
    os.chdir(lastDir)
    fd = open(outFile,'w')
    for i in files:
        fd.write(targetDir + "/" + i + '\n')
    fd.close()
    
if __name__ == '__main__':
    sys.argv.append("//ftlpsupport01.citrite.net/ftlpsuppfs01_prod/Sup_info/Case_Data/79801265/6-23/XAPI DBs")
    sys.argv.append("test.txt")
    main()
