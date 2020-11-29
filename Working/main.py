# alternate version of main.py
kmerLen = 10
kmerFrameShift = 5  # how much to move away through the read
kmerMatchThreshold = 15 #what the req for mapping successful is.
kmerThrowThreshold =  3 # after halfway how many iterations
wiggleRoom = 3
sketch = {}

numReads = 100
fileName = ""
 ##for now

#FOR INTERNAL REF
readNum = -1
readId = ""
def reverse_complement(str):
    #outputs reverse_complement
    val = {"A": "T", "G": "C", "C": "G", "T": "A"}
    rc = ""
    for i in range(len(str)):
        rc+=val[str[len(str)-1-i]]
    return rc



def hashSeq(st):
    """
    Hash function is standard.
    """
    hashKeys = {"A": 1, "C": 2, "T": 3, "G": 4}
    #fixed to distinguish zero values
    base = 5
    hashVal = 0
    for sI in range(len(st)):
        s = st[sI]
        hashVal = hashKeys[s]*(base**sI)+hashVal

    return hashVal

def part1(sequence, read):
    """
    Creates a sketch.
    """
    for seqI in range(len(sequence)-kmerLen):
        #basically map
        mer = sequence[seqI: seqI+kmerLen]

        hashSequence = hashSeq(mer)
        if hashSequence not in sketch:
            sketch[hashSequence] = set([])
            sketch[hashSequence].add(seqI) #crucial piece that was missing
        else:
            sketch[hashSequence].add(seqI)

def find_Max(dict):
    """
    Finds max in dictionary
    """
    Key = -1
    max = 0
    for key, val in dict.items():
        if val > max:
            max = val
            Key = key
    return Key, max


def match_seq(sequence, read):
    """
    Matches sequence to read
    """
    sequence = sequence
    #create sketch

    Read = read
    rRead = reverse_complement(read)
    mapPos, placesRead =  gen_match_seq_places(sequence, Read)
    mapInvPos, placesInvRead = gen_match_seq_places(sequence, rRead)

    #should already return here. Non-mismatched reads.
    if mapPos > 0 and (mapPos > mapInvPos):
        return mapPos # automatic return
    elif mapInvPos > 0 and (mapInvPos > mapPos):
        return mapInvPos
    return -1



def gen_match_seq_places(sequence, read):
    """
    Helper function: maps sequence to specific read.
    """
    #place mapped to freq
    placesOfInterest = {}
    mapPos = -1
    mapFreq = 0

    readIndex = 0
    while readIndex < len(read):
        # print("supposed pos ", sequence.find(read[readIndex, kmerLen+readInd]))
        read_mer = hashSeq(read[readIndex: kmerLen+readIndex])
        hash = hashSeq(read[readIndex: kmerLen+readIndex])
        if hash in sketch.keys():
            alreadyIn = False #only matters if it's verified
            vals = sketch[hash] # all hashed no readdos
            # positions = vals
            # print("midway: ", positions, hash)
            for position in vals:
                #check if position is close enough to key of placesOfInterest
                for keyOfInterest in placesOfInterest.keys():
                    # print("diff:", keyOfInterest-(position-readIndex))
                    if(keyOfInterest-(position-readIndex) < wiggleRoom):
                        #update freq
                        placesOfInterest[keyOfInterest] +=1
                        #TO SEE: check if can break
                        #update max
                        if placesOfInterest[keyOfInterest] > mapFreq:
                            mapFreq = placesOfInterest[keyOfInterest]
                            mapPos = keyOfInterest
                        #threshold met?
                        if mapFreq > kmerMatchThreshold:
                            exit = readIndex
                            return mapPos, placesOfInterest
                        alreadyIn = True
            #check in future.
            if(alreadyIn == False):
                placesOfInterest[position-readIndex] = 1 #good

        #Not this 5'-> 3'
        if readIndex > len(read)*4//8 and (mapFreq < kmerThrowThreshold):
            return -1, placesOfInterest

        readIndex+=kmerFrameShift
    #NOT GOOD
    return -1, placesOfInterest


def runengine(mainNum, seqPath, readsPath):
    #setup
    genome = ""
    setupReader = open(seqPath, "r")
    genomeLines = setupReader.readlines()
    genome = ""
    for line in genomeLines:
        if(line != genomeLines[0]):
            genome+=line.strip("\n")
    part1(genome, genome)
    output = open("output.txt", "w")
    fastq = open(readsPath, "r")
    readNum = 0
    #iter
    for i in range(mainNum):
        seqId = fastq.readline().strip("\n")
        readId = seqId
        seqRead = fastq.readline().strip("\n")
        for k in range(2):
            fastq.readline()
        match = -1
        match = match_seq(sketch, seqRead)

        #matched, now to final processing.
        left = str(match)
        right = str(match + len(seqRead))
        seqPrint = seqId.strip("@") + "\t" + left + "\t" + right + "\n"
        output.write(seqPrint)

        readNum=1+readNum
