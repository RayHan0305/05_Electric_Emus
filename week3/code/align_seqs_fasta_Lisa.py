#! /usr/bin/env python3

### Module imports ###
import sys 
import csv


### Functions ###

# extract DNA sequences from fasta file where each column corresponds to one organism and lines are seauences or fragments of sequences
def extract_seqs(fasta_path):
    """
    Extracts sequences from a fasta file and returns them as a string.
    """
    with open(fasta_path, "r") as MySeqs:
        fastaread = MySeqs.readlines()
        content = [ row.strip() for row in fastaread ] # creates a list of strings
        content = "".join(content[1:])
        #seq1, seq2 = content[0].strip(), content[1].strip() # extracts the two sequences from the first row
    return content # returns the sequence in the second line

# Assign the longer sequence s1, and the shorter to s2
# l1 is length of the longest, l2 that of the shortest
def ordered_seqs(seq1, seq2):
    """
    Takes seq1 and seq2 and returns them in order of length such that s1 is the longer sequence and s2 the shorter one, along with their respective lengths l1 and l2.
    OUTPUT = s1, s2, l1, l2 
    """
    l1 = len(seq1)
    l2 = len(seq2)
    if l1 >= l2:
        s1 = seq1
        s2 = seq2
    else:
        s1 = seq2
        s2 = seq1
        l1, l2 = l2, l1 # swap the two lengths
    return s1, s2, l1, l2

# A function that computes a score by returning the number of matches starting
# from arbitrary startpoint (chosen by user)
def calculate_score(s1, s2, l1, l2, startpoint):
    """returns the score for a given alignment of s1 and s2 where s2 starts at startpoint of s1"""
    score = 0
    for i in range(l2):
        if (i + startpoint) < l1:
            if s1[i + startpoint] == s2[i]: # if the bases match
                score = score + 1
            else:
                continue

    return score

def print_alignment(s1, my_best_align, StartPt):
    """
    returns a string that shows where the sequences match
    """
    matching_letters = " " * StartPt
    for i in range(StartPt,len(my_best_align),1):
        matching_letters += "*" if s1[i] == my_best_align[i] else " "
    return matching_letters


### Main loop ###
# now try to find the best match (highest score) for the two sequences
def main(argv):
    """
    Main loop of the program
    """
    #1. Extract sequences from fasta files or default files
    if len(sys.argv) == 3:
        fasta1 = sys.argv[1]
        fasta2 = sys.argv[2]
    else:

        fasta1 = "../data/407228326.fasta"
        fasta2 = "../data/407228412.fasta"
    seq1 = extract_seqs(fasta1)
    seq2 = extract_seqs(fasta2)

    #2. Order sequences by length
    s1, s2, l1, l2 = ordered_seqs(seq1, seq2)

    #3. Store the score for each starting point
    MyList = [] # stores (start.pt. , score) values
    for i in range(l1):
        score = calculate_score(s1, s2, l1, l2, i)
        MyList.append((i, score))

    #4. get the best score and print the corresponding result
    my_best_align = None
    my_best_score = -1
    for StartPt, Score in MyList:
        if Score > my_best_score:
            my_best_align = "." * StartPt + s2
            my_best_score = Score
            my_best_match = print_alignment(s1, my_best_align, StartPt)
    print("The best alignment is: \n")
    print(my_best_match)
    print(my_best_align)
    print(s1)
    print('\n',f"with score {my_best_score}")


if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)

    

