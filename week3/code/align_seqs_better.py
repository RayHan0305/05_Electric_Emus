
#!/usr/bin/env python3

"""A script which takes a .csv input file with two DNA sequences and outputs a .txt file containting the best alignment of the two
sequences. Additionally a score showing the number of alignment matches made. This code takes a .csv input file called 
align_seqs_test.csv from "../data/file_name". Finally this code also imports softwares for use within the script. 
It imports: sys and csv"""

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
    print("The matched sequence result:", matched)
    return score, matched


def main(): 
    """Checks for .csv input file, displays sequences if found, displays error if not found"""
    input_path = script_dir.parent / 'data' / 'align_seqs_test.csv'
    try:
        with open(input_path, 'r') as f:
            reader = csv.DictReader(f)
            for column in reader:
                if column ['Sequence_number'] == 'seq1':
                    seq1 = column[" Data"].strip()
                elif column ['Sequence_number'] == 'seq2':
                    seq2 = column[" Data"].strip()
        print(f"DNA sequences loaded: Sequence 1: {seq1}, Sequence 2: {seq2}")
    except FileNotFoundError:
        print(f"Error: File not found at {input_path}")
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
        z = calculate_score(s1, s2, l1, l2, i)
        if z >= my_best_score:
            my_best_aligns = 
            my_best_aligns.append({
                "position" : i
                "matched" : matched
                "aligned_seq" : "." * i + s2
            })
            my_best_score = z
        elif z == my_best_score and z > -1:
            my_best_aligns.append({
                "position" : i
                "matched" : matched
                "aligned_seq" : "." * i + s2
            })
    print("\nAlignment results:")
        print(f"Best score: {my_best_score} matches")
        print(f"Total optimal shifts found: {len(all_best_aligns)}")
        print(f"First Best Alignment at Shift Position: {best_align_data['shift_pos']}")

    #Saves alignment and creates .txt file
    output_path = script_dir.parent / 'results' / 'align_sequs_results.txt'
    with open (output_path, 'w') as f:
        f.write(f"Best alignment:\n{my_best_align}\n")
        f.write(f"Best score: {my_best_score}\n")
    print(f"Results saved to {output_path}")

    return 0

if __name__ == "__main__":
    sys.exit(main())