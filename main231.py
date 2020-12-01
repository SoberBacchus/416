# alternate version of main.py
kmerLen = 14
read_wobble = 3
threshold = 3
max = 1000
def map_reads(read_set, genome):
    tik = time.time()

    #sketching
    sketch_tik = time.time()
    ref = {}
    for i in range(len(genome)-lenMer):
        ref[genome[i:i+lenMer]] = i
    sketch_tok = time.time()
    sketch_tiktok = sketch_tok-sketch_tik
    print("sketching used: ", sketch_tiktok)
    read_times = []
    errors = []
    reads =[]
    for set_read in read_set:
        reads.append(set_read)
    for set_read in reads:
        first_mer = set_read[1: lenMer+1]
        last_mer = set_read[-lenMer-1:-1]
        tic = time.time()
        if (first_mer in ref.keys() and last_mer in ref.keys()):
            genome_pos_acc = ((ref[last_mer]-(lenR-lenMer))-ref[first_mer])
            # if genome_pos_acc < 5:
            #     print("success")
            errors.append(genome_pos_acc)

        tok = time.time()
        tiktok = tok-tik
        read_times.append(tiktok)
    avgtime = sum(read_times)/len(read_times)
    avgerr = sum(errors)/len(errors)
    print("Avg time for two checks: ", avgerr)
    print("Avg time for two checks: ", avgtime)


    tok = time.time()
    tiktok = tok-tic
    print("Time: ", tiktok)

def seq_hash(str):
    """
    takes string length lenR and hashes to tuple
    """
    #hash
    sum = 0
    #different hash functionality
    val = {"A": 1, "G": 2, "C": 3, "T": 0} #TTT can create a problem

    #conversion of string to numbers using vals
    for i in range(len(str)):
        sum+=4**i * val[str[i]]
        #skip rolling hash for now
    return sum
def reverse_complement(str):
    """
    Outputs reverse reverse_complement"""
    val = {"A": "T", "G": "C", "C": "G", "T": "A"}
    rc = ""
    for i in range(len(str)):
        rc+=val[str[len(str)-1-i]]
    return rc

def inDict(int, dic):
    """
    Returns closestInt
    """
    #//every num in dictionary
    for num in dic.keys():
        if abs(num-int) < read_wobble:
            return num
    return -1



def update_bins(read_pos, hash, sketch, bin):
    if(not hash in sketch.keys()):
        return
    startPos = sketch[hash]-read_pos #adjusted

    #define in dictionary as close 'nuff to ke
    binKey = inDict(startPos, bin)
    if binKey > 0:
        bin[binKey]+=1
    else:
        bin[startPos] = 1
def checkOver(bin):
    """
    One value meets threshold of mapping
    Essentailly finding which value and pos
    has match rate > threshold=3/
    """
    for key, val in bin.items():
        if val >= threshold:
            return True, key

    return False, 69



def create_hashSketch(seq):
    sketch = {}

    for i in range(len(seq)):
        if i+kmerLen < len(seq):
            sketch[seq_hash(seq[i:i+kmerLen])] = i
        # if i < 10:
        #     # print(seq_hash(seq[i:i+kmerLen]))
    return sketch
    # returns hash value of kmer: position

def match_seq(genome_sketch, read):
    """
    Given sketches of genome and reads
    length of

    genome_sketch: {key, : value, }
    read_sketch: kmers in order
    """

    #only use every other kmer to map
    """maps position to count
    """
    positions = {}
    positions2 = {} #reverse
    #every overlapping kmer not tested
    i = 0
    while(i < len(read)):

        kmer = read[i:i+kmerLen]
        iKmer = seq_hash(kmer)
        reverseComplement = reverse_complement(kmer)
        iiKmer = seq_hash(reverseComplement)        # print(iKmer, genome_sketch)
        currPos = i
        update_bins(i, iKmer, genome_sketch, positions)
        # update_bins(i, iiKmer, genome_sketch, positions2)

        done1, val1 = checkOver(positions)
        done2, val2 = checkOver(positions2)
        if(done2):
            return val2
        if(done1):
            return val1

        i+=kmerLen
    return -1
a = {4:0, 3:1}
# update_bins(0 , 69, {69: 5},a)

# match = match_seq(genome_sketch, seq_hash(read))
import read_genome
read = "TTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATC" #GTAATAAAGGAGCTGGTGGCCATAGTT
g = read_genome.r()

# print(g) genome_sketch = create_hashSketch(setup.r())


if __name__ == "__main__":
    w = open("main23output", "w")
    count = 0

    genome = ""
    with open("ref.fasta", "r") as setupReader:
        while setupReader.readline() != "":
            genome+=(setupReader.readline().strip("\n"))
    gsketch = create_hashSketch(genome)

    with open("sample_1.fastq", "r") as reads:
        while count < 2000:
            id = reads.readline()
            read = reads.readline()
            reads.readline()
            reads.readline()
            id=id.strip("\n")
            read = read.strip("\n")
            matchPos = match_seq(gsketch, read)



            matchPos2 = -5
            if matchPos > 0:
                matchPos2 = matchPos+len(read)
            else:
                matchPos2 = -1


            # st = id + "\t" + matchPos + "\t"
            w.write(id)
            w.write("\t")
            w.write(str(matchPos))
            w.write("\t")
            w.write(str(matchPos2))
            w.write("\n")
            count+=1
    w.close()
