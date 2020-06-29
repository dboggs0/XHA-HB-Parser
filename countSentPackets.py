
'''
counts the packets sent to each host that appears in the capture
'''
name = "textPacketCapturefilename"
filename= name + ".txt"
print(filename)

fd = open(filename)

dictHosts={}
for line in fd:
        destHost = line
        destHost = destHost.split('>')[1].split(':')[0]
        destHost = destHost.strip()

        if destHost not in dictHosts.keys():
                dictHosts[destHost]=0
        else:
                dictHosts[destHost]=dictHosts[destHost]+1
fd.close()

for i in dictHosts:
        print(i + '\t' + str(dictHosts[i]))

