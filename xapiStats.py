'''
Input is xapi-db.xml converted to json (in a file)
provides stats on database contents for consistency checking
'''
import json,sys
binName='xapiStats.py'

def getXapiStats(fileName):
    fd = open(fileName,'r')
    xapi =json.load(fd)
    fd.close

    xapiClassStats= {}
    totalXapiKeys=0

    #count number of classes
    totalXapiKeys = len(xapi.keys())

    #count objects per class
    for i in xapi.keys():
        xapiClassStats[i] = (len(xapi[i]))

    return xapiClassStats

def printXapiStatsInCSV(xapiStats):
    for i in xapiStats:
        print(i + ',' + str(xapiStats[i]))


if __name__ == '__main__':
    try:
        fileName = sys.argv[1]
    except:
        print(sys.argv)
        print("usage:  " + binName + " <path>")
        exit()

    d = getXapiStats(fileName)
    printXapiStatsInCSV(d)
