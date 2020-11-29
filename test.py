"""

test classes for main.py

"""
# import main.py
import main
import numpy.random as npR
import numpy
import time
#rand seq

####### TESTING OTHER MAIN.PY FUNCTIONS #######
lenR = 140
kmerLen = 20
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
    for i in range(100):
        num = npR.choice(numpy.arange(0, 4), p=[aComp, cComp, tComp, gComp])
        seq+=base[num]
    print("Time elapsed, generate_ran_seq, ", time.time()-start)
    return seq
print(generate_ran_seq())
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

ex_gen, ex_reads = gen_problem()


def hash(st):
    return st
