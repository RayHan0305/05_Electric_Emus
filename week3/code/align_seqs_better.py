"""
Usage:
    python3 align_seqs_better.py ../data/<filename> ../data/<filename>

Description:
    This script aligns two FASTA sequences and keeps *all* alignments
    with the highest score. Results are written to ../results/best_alignments.txt
"""

import sys
import os

def read_fasta(filename):
    """Read a FASTA file and return the sequence."""
    with open(filename, 'r') as f:
        lines = f.readlines()
        seq = "".join([line.strip() for line in lines if not line.startswith(">")])
    return seq

def calculate_score(s1, s2, l1, l2, startpoint):
    """Calculate alignment score for a given startpoint."""
    score = 0
    for i in range(l2):
        if (i + startpoint) < l1:
            if s1[i + startpoint] == s2[i]:
                score += 1
    return score

def main(argv):
    # Handle inputs
    if len(argv) != 3:
        print("No input FASTA files specified, using defaults from ../data/")
        seq1_file = "../data/seq1.fasta"
        seq2_file = "../data/seq2.fasta"
    else:
        seq1_file = argv[1]
        seq2_file = argv[2]

    # Read sequences
    seq1 = read_fasta(seq1_file)
    seq2 = read_fasta(seq2_file)

    # Assign longer and shorter
    l1, l2 = len(seq1), len(seq2)
    if l1 >= l2:
        s1, s2 = seq1, seq2
    else:
        s1, s2 = seq2, seq1
        l1, l2 = l2, l1

    # Alignment search
    my_best_score = -1
    best_alignments = []

    for i in range(l1):
        z = calculate_score(s1, s2, l1, l2, i)
        align = "." * i + s2

        if z > my_best_score:
            my_best_score = z
            best_alignments = [(align, z)]
        elif z == my_best_score:
            best_alignments.append((align, z))

    # Output summary
    print(f"\nFound {len(best_alignments)} best alignment(s) with score {my_best_score}.\n")
    for align, score in best_alignments:
        print(f"Alignment (score={score}): {align}")

    # Save to plain text file
    results_dir = "../results"
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    output_file = os.path.join(results_dir, "best_alignments.txt")
    with open(output_file, "w") as f:
        f.write(f"Best score: {my_best_score}\n")
        f.write(f"Number of best alignments: {len(best_alignments)}\n\n")
        for align, score in best_alignments:
            f.write(f"Alignment (score={score}): {align}\n")

    print(f"\nResults saved to {output_file}\n")

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
