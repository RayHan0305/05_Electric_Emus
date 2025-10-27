#!/usr/bin/env python3

"""
Description: This script filters species names in a CSV file, identifying those 
belonging to the Quercus genus (oak trees), and writes them to a new CSV file. 
It reads from an input file, processes the data, and saves the results to an output file.
Additionally, it includes a function with built-in tests using doctest.

Author: 'Zhiquan Kang'
Version: 0.0.1
License: License for this code/program
"""

__appname__ = 'Groupwork_oaks_debugme'
__author__ = 'Zhiquan Kang'
__version__ = '0.0.1'


import csv
import sys
import os

# Ensure the output directory exists, creating it if necessary
results_dir = '../results'
try:
    os.makedirs(results_dir, exist_ok=True)
except OSError as e:
    print(f"Error creating directory '{results_dir}': {e}")
    exit(1)  # Exit with an error code if directory creation fails


def is_an_oak(name):
    """ 
    Returns True if the name starts with 'quercus or Quercus'  

    Examples:
    >>> is_an_oak('Fagus sylvatica') 
    False

    >>> is_an_oak('Quercus sylvatica')
    True

    >>> is_an_oak('Quercuss sylvatica') 
    False
    """
    return name.split()[0] in ('quercus', 'Quercus') 

#print(str(is_an_oak('Quercuss sylvatica')) + " test complete" + '\n')
#gives false

    
def main(argv): 

    # Open the input and output files
    with open('../data/TestOaksData.csv', 'r') as f, open('../results/JustOaksData.csv', 'w', newline='') as g:
        taxa = csv.reader(f)
        csvwrite = csv.writer(g)
        oaks = set()
        
        # Write column headers for the output CSV
        csvwrite.writerow(["Genus", "Species"])
        next(taxa)  # Skip the 'Genus' and 'Species' headers in the input file

        # Iterate through rows in the input CSV
        for row in taxa:
            print(row)
            print("The genus is:") 
            print(row[0] + '\n')
            if is_an_oak(row[0]):
                print('FOUND AN OAK!\n')
                csvwrite.writerow([row[0], row[1]])

    print("Oak names have been written to", '../results/JustOaksData.csv')
    
    return 0

    
if (__name__ == "__main__"):
    status = main(sys.argv)