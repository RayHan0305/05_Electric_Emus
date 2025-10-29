"""
align_seqs_fasta.py: Simple Pairwise Sequence Alignment

This script performs an ungapped alignment search between two biological
sequences provided in FASTA files. It determines the optimal alignment
by sliding the shorter sequence across the entire length of the longer
sequence and calculating the position with the highest number of direct matches.
Usage:
    # To align two specific FASTA files:
    python3 align_seqs_fasta.py <seq1_file_path> <seq2_file_path>
    *NOTE*: these files should each only contain ONE sequence. 

    # To use hard-coded default files:
    python3 align_seqs_fasta.py """

__appname__ = 'Align DNA squences and find best match'
__author__ = 'Natasha Lawson-Hale (tll25@ac.ic.uk)'
__version__ = '0.0.1'


import sys

def read_fasta(filename):
    # Read fasta file
    with open(filename, 'r') as f:
        lines = f.readlines()
        seq = "".join([line.strip() for line in lines if not line.startswith(">")])

    return seq
def calculate_score(s1, s2, l1, l2, startpoint):
    """A function that computes a 'score' by returning the number of matches starting 
    from the beggining of the longest sequence. This function sets the start point of 0 and
    loops through every posisble alignment, it then saves the best alignment into 'match' and 
    'score' showing at how many points in the sequence it aligns.

    Doctests:
    >>> calculate_score("ATGC", "ATGC", 4, 4, 0)
    (4, '****')
    >>> calculate_score("ATCC", "ATGC", 4, 4, 0)
    (3, '**-*')
    >>> calculate_score("TTGCAA", "ATGC", 6, 4, 0)
    (3, '-***')
    >>> calculate_score("AATGC", "ATTGCAG", 5, 7, 0)
    (4, '*-***')
    >>> calculate_score("GGG", "AAAAAA", 3, 6, 0)
    (0, '---')
    """
    matched = "" # to hold string displaying alignements
    score = 0
    for i in range(l2):
        if (i + startpoint) < l1: #ensures the function doesnt run past the end of s1
            if s1[i + startpoint] == s2[i]: # if the bases match
                matched = matched + "*"
                score = score + 1
            else:
                matched = matched + "-"
    return score, matched

def main(argv):
    """
    Handles command-line arguments, reads sequences, performs the sliding
    alignment, and reports the single best alignment score and position.
    """
    if len(argv) == 1:
     # Read the seq
        seq1 = read_fasta("../data/407228326.fasta")
        seq2 = read_fasta("../data/407228412.fasta")
        print("No files provided, using default lines: 407228326.fasta and 407228412.fasta")

    elif len(argv) != 3:
        seq1 = argv[1]
        seq2 = argv[2]
        print("Input found! Aligning.....")

    else:
        print ("Error: too few/many arguments or file error!")
        ("\nInput 3 arguments: align_seq_fasta.py and two fasta files: <seq1_file> <seq2_file>")
        print("\n OR Input ONLY: align_seq_fasta.py to use the default files.")
        sys.exit(0)

    # Compare
    l1, l2 = len(seq1), len(seq2)
    if l1 >= l2:
        s1, s2 = seq1, seq2
    else:
        s1, s2 = seq2, seq1
        l1, l2 = l2, l1

    # Compare the calculation
    my_best_align = None
    my_best_score = -1

    for i in range(l1):
        z = calculate_score(s1, s2, l1, l2, i)
        if z > my_best_score:
            my_best_align = "." * i + s2
            my_best_score = z

    print("The best align:", my_best_align)
    print("The best score:", my_best_score)

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))