"""
Usage:
    python3 align_seqs_fasta.py ../data/<filename> ../data/<filename>
    
Description: 
    This script calculate the match score between two seqs from to seqerate fasta files. 
    Print and save the best score and the last best alignment of it

Author: 'Ximan Ding'
Version: 0.0.1
License: License for this code/program

__appname__ = 'align_seqs_fasta'
__author__ = 'XimanDing'
__version__ = '0.0.1'

"""

import sys

# Read a FASTA file and return the sequence as a string
def read_fasta(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        seq = "".join([line.strip() for line in lines if not line.startswith(">")])
    return seq

# Calculate alignment score
def calculate_score(s1, s2, l1, l2, startpoint):
    score = 0
    for i in range(l2):
        if (i + startpoint) < l1:
            if s1[i + startpoint] == s2[i]:
                score += 1
    return score

def main(argv):
    if len(argv) != 3:
        sys.exit(0)

    seq1_file = argv[1]
    seq2_file = argv[2]

    #  Read FASTA sequences
    seq1 = read_fasta(seq1_file)
    seq2 = read_fasta(seq2_file)

    l1, l2 = len(seq1), len(seq2)
    if l1 >= l2:
        s1, s2 = seq1, seq2
    else:
        s1, s2 = seq2, seq1
        l1, l2 = l2, l1

    # Alignment comparision
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