"""
Usage:
    python3 align_seqs_fasta ../data/<filename> ../data/<filename>
"""

import sys

def read_fasta(filename):
    # Read fasta file
    with open(filename, 'r') as f:
        lines = f.readlines()
        seq = "".join([line.strip() for line in lines if not line.startswith(">")])
    return seq

def calculate_score(s1, s2, l1, l2, startpoint):
    # Calculate the score
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

    # Read the seq
    seq1 = read_fasta(seq1_file)
    seq2 = read_fasta(seq2_file)

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