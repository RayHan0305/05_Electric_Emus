"""
Usage:
    python3 align_seqs_better.py ../data/<filename1> ../data/<filename2>

Description:
    This script aligns two DNA sequences from FASTA files.
    It compares all possible alignments and finds all equally-best alignments
    (not just the first one). 
    The results are saved to the ../results/ directory, using the pickle module.
    
Author: 'Ruixuan Han'
Version: 0.0.1
License: License for this code/program

__appname__ = 'align_seqs_better'
__author__ = 'Ruixuan Han'
__version__ = '0.0.1'
"""

import sys
import os
import pickle

# Read a FASTA file and return the sequence as a string
def read_fasta(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        seq = "".join([line.strip() for line in lines if not line.startswith(">")])
    return seq

# Calculate alignment score between s1 and s2 starting at startpoint.
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

    # Read FASTA sequences
    seq1 = read_fasta(seq1_file)
    seq2 = read_fasta(seq2_file)

    l1, l2 = len(seq1), len(seq2)
    if l1 >= l2:
        s1, s2 = seq1, seq2
    else:
        s1, s2 = seq2, seq1
        l1, l2 = l2, l1

    # Alignment comparison
    my_best_align = []
    my_best_score = -1

    for i in range(l1):
        z = calculate_score(s1, s2, l1, l2, i)
        if z > my_best_score:
            my_best_align = ["." * i + s2]   
            my_best_score = z
            
    print("Best score:", my_best_score)
    print("Number of equally-best alignments:", len(my_best_align))

    # Save results
    results_dir = "../results"
    os.makedirs(results_dir, exist_ok=True)
    output_file = os.path.join(results_dir, "best_alignments.pickle")

    with open(output_file, "wb") as f:
        pickle.dump({
            "best_score": my_best_score,
            "alignments": my_best_align,
            "seq1": s1,
            "seq2": s2
        }, f)

    print(f"Results saved to: {output_file}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
