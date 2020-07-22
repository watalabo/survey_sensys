#!/usr/bin/env python
# -*- coding: utf-8 -*-

import openpyxl
import argparse
import sys
import io
import re

def illegal_char_remover(data):
    ILLEGAL_CHARACTERS_RE = re.compile(
        r'[\000-\010]|[\013-\014]|[\016-\037]|[\x00-\x1f\x7f-\x9f]|[\uffff]')
    """Remove ILLEGAL CHARACTER."""
    if isinstance(data, str):
        return ILLEGAL_CHARACTERS_RE.sub("", data)
    else:
        return data


parser = argparse.ArgumentParser(description="excel hoge hoge")
parser.add_argument("filename", help="filename hog hoge")

args = parser.parse_args()
filename = args.filename

fp = open(filename, "r", encoding="cp932")

text = fp.read()
lines = text.split("\n")

affidb = set()

for line in lines:
#    print(line)
    affi_start = line.find("(")

    while affi_start > 0:
        affi_start = affi_start + 1
        affi_end = line.find(")", affi_start)
        affiliation = line[affi_start:affi_end]
        affiliation = affiliation.strip()
        affiliation = affiliation.replace("HKUST", "Hong Kong University of Science and Technology")
        affiliation = affiliation.replace("Nanyang Technological University, Singapore", "Nanyang Technological University")
        affiliation = affiliation.replace("Nokia Bell Labs and TU Delft", "Nokia Bell Labs")
        affiliation = affiliation.replace("Nokia Bell Labs and University College London", "Nokia Bell Labs")
        affiliation = affiliation.replace("UCL and Nokia Bell Labs", "Nokia Bell Labs")
        affiliation = affiliation.replace("NorthWest University", "Northwest University")
        affiliation = affiliation.replace("Peking University, China", "Peking University")
        affiliation = affiliation.replace("Politecnico di Milano and RI.SE SICS", "Politecnico di Milano")
        affiliation = affiliation.replace("Politecnico di Milano, SICS Swedish ICT", "Politecnico di Milano")
        affiliation = affiliation.replace("SUNY Buffalo, Buffalo, NY USA", "SUNY Buffalo")
        affiliation = affiliation.replace("SUNY University at Buffalo", "SUNY Buffalo")
        affiliation = affiliation.replace("Shanghai Jiao Tong University", "Shanghai Jiaotong University")
        affiliation = affiliation.replace("Stanford University", "Stanford")
        affiliation = affiliation.replace("State University of New York Buffalo", "SUNY Buffalo")
        affiliation = affiliation.replace("State University of New York at Buffalo", "SUNY Buffalo")
        affiliation = affiliation.replace("Stevens Insititute of Technology", "Stevens Institute of Technology")
        affiliation = affiliation.replace("University of California, Berkeley", "UC Berkeley")
        affiliation = affiliation.replace("University of California, Davis", "UC Davis")
        affiliation = affiliation.replace("University of California, Irvine", "UC Irvine")
        affiliation = affiliation.replace("University of California, Merced", "UC Merced")
        affiliation = affiliation.replace("University of Colorado, Denver", "University of Colorado Denver")
        affiliation = affiliation.replace("University of Illinois at Urbana-Champaign", "University of Illinois at Urbana Champaign")
        affiliation = affiliation.replace("University of Maryland, Baltimore County", "University of Maryland")
        affiliation = affiliation.replace("University of Minnsota, twin cities", "University of Minnsota")
        affiliation = affiliation.replace("Uppsala University and RISE SICS AB, Sweden", "Uppsala University")
        affiliation = affiliation.replace("Uppsala University, SICS Swedish ICT", "Uppsala University")
        affiliation = affiliation.replace("Uppsala University, Sweden", "Uppsala University")
        affiliation = affiliation.replace("Uppsala University,Sweden", "Uppsala University")
        affiliation = affiliation.replace("WINLAB, Rutgers University", "Rutgers University")
        affiliation = affiliation.replace("Yonsei University, South Korea", "Yonsei University")
#        print(affiliation)
        affidb.add(affiliation)
        affi_start = line.find("(", affi_end)
    continue

affidb = sorted(affidb)

for name in affidb:
    print(name, end=", ")
#    print(name)
