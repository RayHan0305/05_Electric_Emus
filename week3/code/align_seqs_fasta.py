#!/usr/bin/env python3

"""
align_seqs_fasta.py
This script will align any two DNA sequences from FASTA files in data/.

Usage: 
    This script will take any two fasta sequences (in seperate file in data folder) to be aligned as input.

    Method 1(default):
    No parameters (It will try to use ../data/seq1.fasta and seq2.fasta by default, and if they’re not there, it will automatically pick the first two FASTA files it finds in the ../data/ directory.)

    python3 align_seqs_faster.py

    Method 2:
    Explicitly specify two fasta files as input.
    python3 align_seqs_fasta.py seq1.fasta seq2.fasta
    (for example: python3 align_seqs_fasta.py ../data/407228326.fasta ../data/407228412.fasta)
    There are three fasta files in data/ now which are 407228326.fasta; 407228412.fasta; E.coli.fasta
"""

__appname__ = 'align_seqs_faster'
__author__ = 'Ximan Ding'
__version__ = '0.0.1'
__license__ = "License for this code/program"

from pathlib import Path
import sys
from typing import Tuple, List
import argparse

def read_fasta(p: Path) -> str:
    """Read a (single-sequence) FASTA and return uppercase sequence."""
    return "".join(
        line.strip() for line in p.read_text().splitlines()
        if line and not line.startswith(">")
    ).upper()

def score_at_start(longer: str, shorter: str, start: int) -> int:
    L1, L2 = len(longer), len(shorter)
    score = 0
    for i in range(L2):
        j = start + i
        if j >= L1: break
        if longer[j] == shorter[i]:
            score += 1
    return score

def match_line(longer: str, shorter: str, start: int) -> str:
    L1, L2 = len(longer), len(shorter)
    marks = []
    for i in range(L2):
        j = start + i
        if j >= L1: break
        marks.append("*" if longer[j] == shorter[i] else "-")
    return "." * start + "".join(marks)

def best_alignment(a: str, b: str):
    """Return (longer, padded_shorter, match_visual, best_score, best_start)."""
    longer, shorter = (a, b) if len(a) >= len(b) else (b, a)
    best_score, best_start = -1, 0
    for start in range(len(longer)):
        sc = score_at_start(longer, shorter, start)
        if sc > best_score:
            best_score, best_start = sc, start
    padded_shorter = "." * best_start + shorter
    return longer, padded_shorter, match_line(longer, shorter, best_start), best_score, best_start

def auto_two_fastas(data_dir: Path):
    files = sorted(list(data_dir.glob("*.fa")) + list(data_dir.glob("*.fasta")) + list(data_dir.glob("*.fna")))
    if len(files) < 2:
        raise SystemExit(f"[ERROR] Need at least 2 FASTA in {data_dir}")
    return files[0], files[1]

def save_result(out_path: Path, f1: Path, f2: Path, longer: str, padded: str, vis: str, score: int, start: int):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        "# align_seqs_fasta.py result\n"
        f"Input 1: {f1}\nInput 2: {f2}\n\n"
        f"Best score: {score}\nStart on longer (0-based): {start}\n\n"
        f"{longer}\n{padded}\n{vis}\n"
    )

def main(argv):
    proj = Path(__file__).resolve().parent.parent
    data_dir = proj / "data"
    out_file = proj / "results" / "align_seqs_fasta_result.txt"

    if len(argv) == 3:
        f1, f2 = Path(argv[1]), Path(argv[2])
    elif len(argv) == 1:
        f1, f2 = auto_two_fastas(data_dir)
        print(f"[INFO] Using defaults from {data_dir}: {f1.name}, {f2.name}")
    else:
        print("Usage: python3 align_seqs_fasta.py <seq1.fasta> <seq2.fasta>")
        return 1

    s1, s2 = read_fasta(f1), read_fasta(f2)
    longer, padded, vis, score, start = best_alignment(s1, s2)

    print("\n=== Best alignment ===")
    print(f"Score: {score}    Start(on longer): {start}\n")
    print(longer)
    print(padded)
    print(vis)

    save_result(out_file, f1, f2, longer, padded, vis, score, start)
    print(f"\n[OK] Result saved to: {out_file}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))