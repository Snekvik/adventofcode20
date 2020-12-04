# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:58:42 2020

@author: kristians
"""

import os

curdir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(curdir, "input3.txt"), "r") as f:

    # Number of Lines
    nol = len(f.readlines())


def tree_crashes(right=3, down=1):
    column = right

    number_of_trees = 0
    with open(os.path.join(curdir, "input3.txt"), "r") as f:
        line = f.readline()
        while line:
            for _ in range(down):
                line = f.readline().replace("\n", "")
            if len(line) > 0:
                line = "".join([line] * (right * int(nol / len(line)) + right))
            else:
                continue
            if line[column] == "#":
                number_of_trees += 1
            column += right
    return number_of_trees


# Product of number of trees
prod_not = 1

moves = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for move in moves:
    num_trees = tree_crashes(*move)
    prod_not = prod_not * num_trees
