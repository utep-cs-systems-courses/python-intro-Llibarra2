from sys import argv, stdin, stderr
from re import sub, split

progName = argv[0]

def usage():
    print(f"Usage: {progName} inputFile outputFile", file=stderr)
    
try:
    inFileName = argv[1] #takes input file
    outFileName = argv[2] #takes output file
    
except:
    usage()#no input and/or output files submitted
    exit(1)
    
def tryOpen(name, mode):#opens file
    try:
        return open(name, mode)#valid file
    except:
        print(f"{progName}: Can't open file '{name}' in mode '{mode}'", file=stderr)#invalid file
        exit(1)
        
inFile = tryOpen(inFileName, "r")#reads input file
outFile = tryOpen (outFileName, "w")#writes on output file

wordCounts = {}#keeps track of all words in input file

for line in inFile.readLines():#traverses each line on input file
    line = line +" "
    line = line.lower()
    line = sub(" [-.,:;'\n\t]"," ", line)
    line = sub(" +", " ", line)
    line = line[0: -1]
    
    if len(line)==0:# skips white space
        continue
    for word in split (" ", line):#splits line into words
        if word not in wordCounts:
            wordCounts[word] = 1 #new word found 
        else:
            wordCounts[word]=+1 #appearance of an already found word
            
for word in sorted (wordCounts.keys()):
    print(f"{word} {wordCounts[word]}", file = outFile)#displays all words and counts for each

#closes files
inFile.close()
outFile.close()