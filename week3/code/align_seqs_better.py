
#!/usr/bin/env python3

"""
align_seqs_fasta.py: Simple Pairwise Sequence Alignment

This script performs an ungapped alignment search between two biological
sequences provided in FASTA files. It determines the optimal alignment
by sliding the shorter sequence across the entire length of the longer
sequence and calculating the position with the highest number of direct matches.
This script finds ALL optimal alignments within two sequences.
Uses hard-coded default files:
    python3 align_seqs_fasta.py """

__appname__ = 'Align DNA squences and find best match'
__author__ = 'Natasha Lawson-Hale (tll25@ac.ic.uk)'
__version__ = '0.0.1'

__appname__ = 'Align DNA squences and find best match'
__author__ = 'Natasha Lawson-Hale (tll25@ac.ic.uk)'
__version__ = '0.0.1'

import sys
import csv
import pickle
from pathlib import Path

script_dir = Path(__file__).parent

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

def read_fasta(filename):
    # Read fasta file
    with open(filename, 'r') as f:
        lines = f.readlines()
        seq = "".join([line.strip() for line in lines if not line.startswith(">")])
    return seq
def main(): 
    seq1, seq2 = "", ""
    try:
        seq1 = read_fasta("../data/407228326.fasta")
        seq2 = read_fasta("../data/407228412.fasta")
        print(f"DNA sequences loaded!")
    except FileNotFoundError:
        print(f"Error: File not found!")
        return 1  # exit with error

    ##Assign the longer sequence to s1, and the shorter to s2. 
    ##l1 is the longest and l2 that of the shortest.
    l1 = len(seq1)
    l2 = len(seq2)

    if l1 >= l2:
        s1 = seq1
        s2 = seq2
    else:
        s1 = seq2
        s2 = seq1
        l1, l2 = l2, l1 # swaps the two lengths if s2 is longer than s1

    ##
    my_best_aligns = []
    my_best_score = -1
    for i in range(l1):
        z, matched = calculate_score(s1, s2, l1, l2, i)
        
        if z > my_best_score:
            # Found a new, STRICTLY HIGHER best score:
            my_best_aligns = [] # Reset the list, discarding old, lower-scoring alignments
            my_best_aligns.append({
                "position" : i,
                "matched" : matched,
                "aligned_seq" : "." * i + s2
            })
            my_best_score = z
            
        elif z == my_best_score:
            # Found a score EQUAL to the current best:
            my_best_aligns.append({
                "position" : i,
                "matched" : matched,
                "aligned_seq" : "." * i + s2
            })
    print("\nAlignment results:")
    print(f"Best score: {my_best_score} matches")
    print(f"Total best shifts found: {len(my_best_aligns)}")


    output_dir = script_dir.parent / 'results'

    results_data = {
            "Sequence 1": s1,
            "Sequence 2": s2,
            "Best_alignment_score": my_best_score,
            "All_best_alignments": my_best_aligns # The list of all best shifts
        }
    try:
        with open (output_dir, 'wb') as f:
            pickle.dump(results_data, f)
            print(f"Detailed results saved to PICKLE file: {output_dir}")
    except Exception as e:
        print(f"Error saving pickle file: {e}")
    return 0

if __name__ == "__main__":
    sys.exit(main())