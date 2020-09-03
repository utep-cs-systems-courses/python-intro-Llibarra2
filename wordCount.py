from sys import argv, stdin, stderr
from re import sub, split

progName = argv[0]

def usage():
    print(f"Usage: {progName} inputFile outputFile", file=stderr)
    
try:
    inFileName = argv[1]
    outFileName = argv[2]
    
except:
    usage()
    exit(1)
    
def tryOpen(name, mode):
    try:
        return open(name, mode)
    except:
        print(f"{progName}: Can't open file '{name}' in mode '{mode}'", file=stderr)
        exit(1)
        
inFile = tryOpen(inFileName, "r")
outFile = tryOpen (outFileName, "w")

wordCounts = {}

for line in inFile.readLines():
    line = line +" "
    line = line.lower()
    line = sub(" [-.,:;'\n\t]"," ", line)
    line = sub(" +", " ", line)
    line = line[0: -1]
    
    if len(line)==0:
        continue
    for word in split (" ", line):
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word]=1
            
for word in sorted (wordCounts.keys()):
    print(f"{word} {wordCounts[word]}", file = outFile)

inFile.close()
outFile.close()