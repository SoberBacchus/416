"""

test classes for main.py

"""
# import main.py
import numpy.random as npR
import numpy
import time
#rand seq

lenR = 140
lenG = 30000
aComp = 39/100.
cComp = 32/100.
tComp = 11/100.
gComp = 18/100.
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


import main.py
################ Testing for Main.py functionality ###############
create_sketch(generate_ran_seq(), 20)


generate_ran_seq()



    #select base

    #simulate insertions
    #simulate deletions

    #simulate mutations
    #5% rate

    #check different mutation rate
