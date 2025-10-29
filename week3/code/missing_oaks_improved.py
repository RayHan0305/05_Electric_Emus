#!/usr/bin/env python3

"""This script will read a file named TestOaksData.csv in ../data/TestOaksData.csv containing the genus and species of trees.
it will output information into another file called JustOaksData.csv. The script does two things, it will print each genus and identify
if the genus is 'Quercus' if it is, it will the print the full scientific name into the output file. This script can be used to identify
oaks within a data set. This script imports: sys and csv"""

__appname__ = 'Oaks debug me'
__author__ = 'Natasha Lawson-Hale' '(tll25@ac.ic.uk)'
__version__ = '0.0.1'

import csv
import sys

#Define function
def is_an_oak(name):
    """ Returns True if name starts with 'quercus'
    Basic tests:
    >>> is_an_oak("Quercus ilex")
    True
    >>> is_an_oak("Acer campestre")
    False
    >>> is_an_oak("Quillaja saponaria")
    False

    Extra spaces:
    >>> is_an_oak("Quercus petraea")
    True

    Case insensitivity:
    >>> is_an_oak("QUERCUS ILEX")
    True
    >>> is_an_oak("quercus cerris")
    True
    
    Typos:
    >>> is_an_oak("Qercus robur")
    False
    
    Punctuation:
    >>> is_an_oak("Quecrus petraea'")
    False
    >>> is_an_oak("Quercus, palustris")
    True"""
    name = name.strip().lower()
    name = name.replace(",", "").replace("'", "").replace('"', "")
    return name.lower().startswith('quercus')   

def main(argv): 
    """This section opens two input and output files and assigns variables which allow the for loop to work.
    The for loop then prints the name of the genus of each species, runs the is_an_oak and writes the
    outputs into a .csv file with headings."""
    #Opens input and output files
    f = open('../data/TestOaksData.csv','r')
    g = open('../data/JustOaksData.csv','w')
    #Assigns variables
    taxa = csv.reader(f) 
    csvwrite = csv.writer(g)
    oaks = set()
    next(taxa) #skips headers
    csvwrite.writerow(["Genus", "Species"]) #writes headers into output file
    #For loop which prints which Genus each species is and runs is_and_oak func
    #Writes it into output file
    for row in taxa:
        print(row)
        print ("The genus is: ") 
        print(row[0] + '\n')
        if is_an_oak(row[0]):
            print('FOUND AN OAK!\n')
            csvwrite.writerow([row[0], row[1]])    
    return 0

if (__name__ == "__main__"):
    status = main(sys.argv)
