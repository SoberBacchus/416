# alternate version of main.py
kmerLen = 10
kmerFrameShift = 5
kmerMatchThreshold = 10
kmerThrowThreshold =  3 # after halfway how many iterations
wiggleRoom = 3
sketch = {}

numReads = 100
fileName = ""
 ##for now



def reverse_complement(str):
    """
    Outputs reverse reverse_complement"""
    val = {"A": "T", "G": "C", "C": "G", "T": "A"}
    rc = ""
    for i in range(len(str)):
        rc+=val[str[len(str)-1-i]]
    return rc



def hashSeq(st):
    hashKeys = {"A": 1, "C": 2, "T": 3, "G": 4}
    #fixed to distinguish zero values
    base = 5
    hashVal = 0
    for sI in range(len(st)):
        s = st[sI]
        hashVal = hashKeys[s]*(base**sI)+hashVal

    return hashVal

def part1(sequence, read):
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
    Finds max
    """
    Key = -1
    max = 0
    for key, val in dict.items():
        if val > max:
            max = val
            Key = key
    return Key, max


def match_seq(sequence, read):
    sequence = sequence
    #create sketch

    Read = read
    rRead = reverse_complement(read)
    mapPos, placesRead =  gen_match_seq_places(sequence, Read)
    mapInvPos, placesInvRead = gen_match_seq_places(sequence, rRead)

    if mapPos > 0 and (mapPos > mapInvPos):
        return mapPos # automatic return
    elif mapInvPos > 0 and (mapInvPos > mapPos):
        return mapInvPos

    maxForRead, pos1 = find_Max(placesRead)
    maxInvRead, pos2 = find_Max(placesInvRead)

    if maxForRead>=kmerMatchThreshold:
        return pos1
    if maxInvRead>=kmerMatchThreshold:
        return pos2
    return -5
"""    if maxForRead > maxInvRead:
        print("Places Read")
    else:
        print("Reached End Inverse Read Likely")
"""


def gen_match_seq_places(sequence, read):

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
                    if(keyOfInterest-(position-readIndex) < 1
                    or (keyOfInterest-(position-readIndex) < wiggleRoom)): #DEL?
                     # adjusted value might be too big
                        #set
                        placesOfInterest[keyOfInterest] +=1
                        #check if can break

                        #update max
                        if placesOfInterest[keyOfInterest] > mapFreq:
                            mapFreq = placesOfInterest[keyOfInterest]
                            mapPos = keyOfInterest
                        #threshold met?
                        if mapFreq > kmerMatchThreshold:
                            exit = readIndex
                            return mapPos, placesOfInterest

                        alreadyIn = True


            # print("reached")
            if(alreadyIn == False):
                placesOfInterest[position-readIndex] = 1 #good

        #OPTIMIZATION #HALFPOINT
        if readIndex > len(read)*4//8 and (mapFreq < kmerThrowThreshold):
            return -1, placesOfInterest

        readIndex+=kmerFrameShift
        #now all checked...
        #so
    #once over check so...
    return -1, placesOfInterest


# def test_main():
#     genome = ""
#     setupReader = open("ref.fasta", "r")
#     genomeLines = setupReader.readlines()
#     genome = ""
#     for line in genomeLines:
#         if(line != genomeLines[0]):
#             genome+=line.strip("\n")
#
#     output = open("output.txt", "w") #<--- sTART OF THE DAWN
#     fastq = open("sample_1.fastq", "r")
#     for i in range(100):
#         seqId = fastq.readline().strip("\n")
#         seqRead = fastq.readline().strip("\n")
#         for k in range(2):
#             fastq.readline()
#         match = -1
#         match = match_seq(genome, seqRead)
#     #with open("sample_1.fastq", "w"):
#         #for i in range(mainNum):
#
#         left = str(match)
#         right = str(match + len(seqRead))
#         seqPrint = seqId + "\t" + left + "\t" + right + "\n"
#         readPrint = seqRead + "\n"
#         output.write(seqPrint)
#         output.write(readPrint)
#     output.close()
# test_main()
def main(mainNum):
    #setup
    genome = ""
    setupReader = open("ref.fasta", "r")
    genomeLines = setupReader.readlines()
    genome = ""
    for line in genomeLines:
        if(line != genomeLines[0]):
            genome+=line.strip("\n")
    part1(genome, genome)
    output = open("output.txt", "w") #setup
    fastq = open("sample_1.fastq", "r")
    for i in range(mainNum):
        seqId = fastq.readline().strip("\n")
        seqRead = fastq.readline().strip("\n")
        for k in range(2):
            fastq.readline()
        match = -1
        match = match_seq(sketch, seqRead)
    #with open("sample_1.fastq", "w"):
        #for i in range(mainNum):

        left = str(match)
        right = str(match + len(seqRead))
        seqPrint = seqId + "\t" + left + "\t" + right + "\n"
        output.write(seqPrint)
main(1000)
# 
# import Bio
#
# from random import *
#
# kmerLen = 10
# #dist from kmer hash (accounting for displacement for kmer) to supposed
# #startPos
# wiggleRoom = 5
#
# def map_reads(read_set, genome):
#     tik = time.time()
#
#     #sketching
#     sketch_tik = time.time()
#     ref = {}
#     for i in range(len(genome)-lenMer):
#         ref[genome[i:i+lenMer]] = i
#     sketch_tok = time.time()
#     sketch_tiktok = sketch_tok-sketch_tik
#     print("sketching used: ", sketch_tiktok)
#     read_times = []
#     errors = []
#     reads =[]
#     for set_read in read_set:
#         reads.append(set_read)
#     for set_read in reads:
#         first_mer = set_read[1: lenMer+1]
#         last_mer = set_read[-lenMer-1:-1]
#         tic = time.time()
#         if (first_mer in ref.keys() and last_mer in ref.keys()):
#             genome_pos_acc = ((ref[last_mer]-(lenR-lenMer))-ref[first_mer])
#             # if genome_pos_acc < 5:
#             #     print("success")
#             errors.append(genome_pos_acc)
#
#         tok = time.time()
#         tiktok = tok-tik
#         read_times.append(tiktok)
#     avgtime = sum(read_times)/len(read_times)
#     avgerr = sum(errors)/len(errors)
#     print("Avg time for two checks: ", avgerr)
#     print("Avg time for two checks: ", avgtime)
#
#
#     tok = time.time()
#     tiktok = tok-tic
#     print("Time: ", tiktok)
#
# def seq_hash(str):
#     """
#     takes string length lenR and hashes to tuple
#     """
#
#     #different hash functionality
#     val = {"A": 1, "G": 2, "C": 3, "T": 4}
#
#     #conversion of string to numbers using vals
#     for i in range():
#
#
#     return finVal
# print(seq_hash("ATGGATTTTTTTTTTT"))
#
# def match_seq(genome_sketch, read):
#     """
#     Given sketches of genome and reads
#     length of
#
#     genome_sketch: {key, : value, }
#     read_sketch: kmers in order
#     """
#     bins = {}
#     bin = 0
#
#     counter = 0
#     while(counter < len(read)):
#         hash_val = seq_hash(read[counter:counter+1+kmerLen])
#         noBins = True
#         for key, val in bins.items():
#             if(Math.abs(hash_val-key) < 5):
#                 #update bin counter
#                 bins[key]=1+bins[key]
#                 #set boolean to False
#                 noBins = False
#                 #update bin counter
#                 if(bins[key] > bin):
#                     bin = bins[key]
#         #after iteration
#         if(noBins):
#             bins[hash_val] = 1
#         #FINISHED
#         if bin > 3:
#             print("finised read_num, ", read)
#             break
#         else:
#             counter+=kmerLen
#
#
#
# def create_sketch(seq, type):
#     """
#     Creates sketch of genome seq.
#     """
#     sketch = {}
#     sketch_fin = {}
#     for posx in range(len(seq)-kmerLen):
#         sketch[seq[i: i+kmerLen]] = posx
#     # Now: {hashed str: keys}
#     for mer in sketch.keys():
#         sketch_fin[seq_hash(mer)] = sketch[mer]
#     return sketch_fin
#
#
#
# def m():
#     """
#     read io of fasta and fastq
#     """
#
#
#     g_sketch = create_sketch(genome)
#     read_sketches = []
#     for read in reads:
#         read_sketches.append(create_sketch(read))
#
#     matched = []
#     for readSketch in read_sketches:
#         first = "" + read  + ""
#         second = match_seq(g_sketch, readSketch)
#         third = second + lenR
#         matched.append((first, second, third))
#
#     return read_mapped
# #
# # m()
# #
#
#
# #
# # from Bio import SeqIO
#
# # short_sequences = []  # Setup an empty list
# # for record in SeqIO.parse("cor6_6.gb", "genbank"):
# #     if len(record.seq) < 300:
# #         # Add this record to our list
# #         short_sequences.append(record)
# #
# # print("Found %i short sequences" % len(short_sequences))
# #
# # SeqIO.write(short_sequences, "short_seqs.fasta", "fasta")
