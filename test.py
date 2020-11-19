"""

test classes for main.py

"""
# import main.py
import numpy.random as npR
import numpy
import time
#rand seq

lenR = 140
lenMer = 20
lenG = 30000
aComp = 42/100.
cComp = 33/100.
gComp = 16/100.
tComp = 9/100.

base = ['A', 'C', 'T', 'G']

def generate_ran_seq():
    """
    outputs sequence for problem use
    """
    start = time.time()
    seq = ""
    # reads = []
    # seq = ""
    for i in range(lenG):
        num = npR.choice(numpy.arange(0, 4), p=[aComp, cComp, tComp, gComp])
        seq+=base[num]
    print("Time elapsed, generate_ran_seq, ", time.time()-start)
    return seq

def gen_problem():
    g = generate_ran_seq()
    reads = set([])
    ###### Timing#######
    tic = time.time()
    for i in range(140):
        start = int(npR.random() * (len(g)-lenR))
        reads.add(g[start: start+lenR])
    tok = time.time()#current - tic
    tiktok = tok-tic
    print("Time creating test seq, ", tiktok)
    return reads, g


def map_reads(reads, genome):
    tik = time.time()

    #sketching
    sketch_tik = time.time()
    ref = {}
    for i in range(len(genome)-lenMer):
        ref[genome[i:i+lenMer]] = i

    read_times = []
    for j in range(len(reads)):
        first_mer = reads[j][1: lenMer]
        last_mer = reads[j][-lenMer-1:-1]
        tic = time.time()
        if (first_mer in ref.keys() and last_mer in ref.keys()):
            genome_pos_acc = (ref[last_mer]-(lenR-lenMer))-ref[first_mer]
            if genome_pos_acc < 10:
                print("success")

        tok = time.time()
        tiktok = tok-tik
        read_times.append(tiktok)

    print("Avg time for two checks: ", sum())

    sketch_tok = time.time()
    sketch_tiktok = sketch_tok-sketch_tik
    print("sketching used: ", sketch_tiktok)
    tok = time.time()
    tiktok = tok-tic
    print("Time: ", tiktok)


################ Testing for Main.py functionality ###############
Reads, Genome = gen_problem()
map_reads(Reads, Genome)




    #select base

    #simulate insertions
    #simulate deletions

    #simulate mutations
    #5% rate

    #check different mutation rate
