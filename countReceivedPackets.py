name = "textPacketCaptureFileName"
filename= name + ".txt"
print(filename)

fd = open(filename)

dictHosts={}
for line in fd:
        sourceHost = line
        sourceHost = sourceHost.split(' ')[2].strip()

        if sourceHost not in dictHosts.keys():
                dictHosts[sourceHost] = 0
              
        else:
                dictHosts[sourceHost] = dictHosts[sourceHost] + 1

fd.close()

for i in dictHosts:
        print(i + '\t' + str(dictHosts[i]))
