# **CMEEGroupWork - Week3 - Python**

## Table of Contents

- [**CMEECourseWork - Week3 - Python**](#cmeecoursework---week3---Python)
  - [**Table of Contents**](#table-of-contents)
  - [**Brief Description**](#brief-description)
  - [**Languages**](#languages)
  - [**Installation**](#installation)
  - [**Project structure and Usage**](#project-structure-and-usage)
    - [**Repo Structure introduction**](#repo-structure-introduction)
    - [**Scripts List**](#scripts-list)
  - [**Author and Contact**](#author-and-contact)

## **Brief Description**

Groupwork Practicals that focusing on **Python biological computing**. 

Includes sequence alignment (DNA 1-2) and data filtering (oaks practical) exercise. Use ipdb and doctest to debug the code.

These works are based on the Notebook and Data from https://github.com/mhasoba/TheMulQuaBio.git. Thanks a lot!

## **Languages**
```
Python
```
## **Installation**
```
git clone git@github.com:RayHan0305/05_Electric_Emus.git
```

## **Project structure and Usage**
```plaintext
05_Electric_Emus/
│
├── week3/
│   ├── code/
│   ├── data/
│   └── results/
└── README.md
```
Run scripts from the `code` directory, and all results are automatically saved in the `../results/` folder

### **Repo Structure introduction**

It contains directories called `code`, `data`, `results`

### **Scripts List**

```Group practices scripts```
| Script Name |Description | Arguments |
| ------ | ------ | ------ |
HEAD
| align_seqs_fasta.py    | Aligns two DNA sequences provided as separate FASTA files. It can take explicit file names as input or, if no arguments are provided, automatically picks two dafaut FASTA files from the data/ folder (e.g., `407228412.fasta` and `407228326.fasta`). The script outputs the best alignment and its score in `../results/best_alignment_fasta.txt`. | 1 -> A fasta file (default:`407228412.fasta`), 2 -> A fasta file (default:`407228326.fasta`)|
| align_seqs_better.py   | Calculate the match score between two seqs. Print and save all the possible alignment with the highest match score of it. | 1 -> A fasta file (default:`407228412.fasta`), 2 -> A fasta file (default:4`07228326.fasta`)|
| Groupwork_oaks_debugme.py    | This script filters species names in a `.csv` file, identifying those belonging to the Quercus genus (oak trees), and writes them to a new `.csv` file. | None |

## Example Commands
```
# Default mode (auto-pick two FASTA from data/)
python3 align_seqs_fasta.py

# Explicit input
python3 align_seqs_fasta.py ../data/407228326.fasta ../data/407228412.fasta

# Save all best alignments
python3 align_seqs_better.py

# Filter oak species
python3 Groupwork_oaks_debugme.py
```


## **Author and Contact**
**Name:** Paruit Lisa, Zhiquan Kang, Lawson-Hale Tasha L, Ruixuan Han, Ximan Ding.

**Institution:** CMEE Programme, Imperial College London
