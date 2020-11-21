
##### How many reads appear?
num_reads = 500000
def get_reads():
    r = open("sample1.txt", "r")
    gathered_reads = []

    while(len(gathered_reads < num_reads)):
        prev = r.readline()
        this = r.readline()f
        if prev.strip("\n") == "+":
            gathered_reads.append(this.strip("\n"))


    w = open("reads1.txt", "w")
    for read in gathered_reads:
        w.write(read + "\n")
    w.close()
get_reads()


from Bio import SeqIO
####
bad_read = 0.01
insertion = 0.01
deletion = 0.01
aComp = 42/100.
cComp = 33/100.
gComp = 16/100.
tComp = 9/100.
def sample():
    """
    Cuts ground_truth.txt

    """

    truth = open("truth.txt", "r")

    tests = []

    i = 0
    while (i < 100000):
        read = truth.readline()
        tests.append(read.split(" "))
        i = i+1
    return tests

def form_reads(s, t):
    """
    Gives back array
    """

    reads = []
    for i in range(len(t)):
        posStart = t[i][1]
        posStop = t[i][2]
        seq = s[posStart:posStop+1]
        reads.append(seq)
    quick_anal(t)
    return reads
def quick_anal(st):
    """
    Take average distance
    """

    reads = []
    for i in range(len(st)):
        reads.append(st[i][2]-st[i][1])

    print("on average: ", sum(reads)*1./len(reads))


def reverse_complement(seq):
    b ={"G":"C", "A": "T", "T": "A", "C": "G"}
    seq_ = ""
    for i in range(len(seq)):
        seq_ = seq_ + b[seq[len(seq)-1-i]]
    return seq_
seq=  reverse_complement("ATG")
# print(seq)

def mess_up(reads):
    bases = ["A", "C", "T", "G"]
    reads_ = []
    for i in range(len(reads)):
        curr_read = reads[i]
        reads_.append(curr_read)
        reads_.append(reverse_complement(reads[i]))

        read2 = ""
        for i in range(len(curr_read)):

            type, p = ["mis", "ins", "del", "skip"], [bad_read, insertion, deletion, 1-(bad_read+
                        insertion+deletion)]
            change = npR.choice(type, p=p)
            if change == "mis":
                type, p = [x  for x in bases if x != curr_read[i]], [0.3]*3
                base = npR.choice(type, p=p)
                read2.append(base)
            elif change == "ins":
                type, p = [x for x in bases], [aComp, cComp, tComp, gComp]
                read2.append(npR.choice(type, p=p))
            elif change == "del":
                continue
            else:
                read2.append(curr_read[i])
        reads_.append(read2)
    return reads_


def main():
    test = sample()

    ### open truth.truth
    reader = open("seq.txt", "r")
    seq = reader.read()

    reads = form_reads(seq, test)

    sim_reads = mess_up(reads)

    reads_writer = open("reads.txt", "w")
    for sim_read in sim_reads:
        st = sim_read + "\n" #what to write
        reads_writer.write(st)
    reads_writer.close()
