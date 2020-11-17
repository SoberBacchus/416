"""
for python program
"""


def match_seq():
    """
    Inputs: Genome sketch, Read sketch
    """


def create_sketch():
    """
    Creates sketch of genome seq. Same for
    both sketches
        pass
    """

def home_base():
    """
    read io of fasta and fastq
    """

from Bio import SeqIO

short_sequences = []  # Setup an empty list
for record in SeqIO.parse("cor6_6.gb", "genbank"):
    if len(record.seq) < 300:
        # Add this record to our list
        short_sequences.append(record)

print("Found %i short sequences" % len(short_sequences))

SeqIO.write(short_sequences, "short_seqs.fasta", "fasta")
