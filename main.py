"""
for python program
PRINCIPLES
include print statements in tests and not methods.
Easily bypass by doing it before and after method calls.

"""
import Bio

import random.random as ran

kmerLen = 10

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

    #different hash functionality
    val = {"A": 1, "G": 2, "C": 3, "T": 4}

    #conversion of string to numbers using vals
    numStr =[]
    num = 0
    for i in range(len(str)):
        numStr.append(val[str[i]])
    for i in range(len(numStr)):
        num+=2**i * numStr[i]
    return num
# print(seq_hash("ATG"))

def match_seq(genome_sketch, read_sketch):
    """
    Given sketches of genome and reads
    length of

    genome_sketch: {key, : value, }
    read_sketch: kmers in order
    """

    ### compare

    # matches based on kmer

    first_mer = read_sketch[0]
    if first_mer in genome_sketch:
        if (len(genome_sketch[first_mer]) > 1):
            print("wow, here's an exception")

        start_pos = first_mer
    return start_pos


def create_sketch(seq, type):
    """
    Creates sketch of genome seq.
    """
    sketch = {}
    sketch_fin = {}
    for posx in range(len(seq)-kmerLen):
        sketch[seq[i: i+kmerLen]] = posx
    # Now: {hashed str: keys}
    for mer in sketch.keys():
        sketch_fin[seq_hash(mer)] = sketch[mer]
    return sketch_fin



def m():
    """
    read io of fasta and fastq
    """


    g_sketch = create_sketch(genome)
    read_sketches = []
    for read in reads:
        read_sketches.append(create_sketch(read))

    matched = []
    for readSketch in read_sketches:
        first = "" + read  + ""
        second = match_seq(g_sketch, readSketch)
        third = second + lenR
        matched.append((first, second, third))

    return read_mapped

m()
#
# from Bio import SeqIO

# short_sequences = []  # Setup an empty list
# for record in SeqIO.parse("cor6_6.gb", "genbank"):
#     if len(record.seq) < 300:
#         # Add this record to our list
#         short_sequences.append(record)
#
# print("Found %i short sequences" % len(short_sequences))
#
# SeqIO.write(short_sequences, "short_seqs.fasta", "fasta")
