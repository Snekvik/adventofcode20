# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 09:00:19 2020

@author: kristians
"""

import os

CURDIR = os.path.abspath(os.path.dirname(__file__))

declarations = []
with open(os.path.join(CURDIR, "input6.txt"), "r") as f:
    line = f.readline()
    declaration = []
    while line:
        line = line.replace("\n", "")
        if len(line) >= 1:
            declaration.append(line)
        else:
            declarations.append(declaration)
            declaration = []
        line = f.readline()
    declarations.append(declaration)


def num_yes(declaration):
    unique_yes = ''
    for answer in declaration:
        unique_yes = unique_yes + answer
    return len(set(unique_yes))


def yes_in_all(declaration):
    yes_ans = set(declaration[0])
    for answer in declaration[1:]:
        yes_ans = yes_ans.intersection(set(answer))
    return len(yes_ans)


number_yes = [num_yes(declaration) for declaration in declarations]
nm_yes_all = [yes_in_all(declaration) for declaration in declarations]
