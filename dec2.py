# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 13:39:20 2020

@author: kristians
"""

import os

curdir = os.path.abspath(os.path.dirname(__file__))


def first_problem():

    valid_passwds = 0

    with open(os.path.join(curdir, "input2.txt"), "r") as f:
        line = 1
        while line:
            line = f.readline()
            l1 = line[:line.find(":")]
            try:
                letter = l1[-1]
            except IndexError as ie:
                print(ie)
                continue
            min_count = int(l1[:l1.find("-")])
            max_count = int(l1[(l1.find("-") + 1): l1.find(" ")])
            l2 = line[(line.find(":") + 1):]
            letter_count = l2.count(letter)
            if letter_count >= min_count:
                if letter_count <= max_count:
                    valid_passwds += 1

    return valid_passwds()


valid_passwds = 0

with open(os.path.join(curdir, "input2.txt"), "r") as f:
    line = 1
    while line:
        line = f.readline()
        l1 = line[:line.find(":")]
        try:
            letter = l1[-1]
        except IndexError as ie:
            print(ie)
            continue
        l2 = line[(line.find(":") + 1):]
        first_pos = int(l2[int(l1[:l1.find("-")])] == letter)
        secnd_pos = int(l2[int(l1[(l1.find("-") + 1): l1.find(" ")])] == letter)
        if first_pos + secnd_pos == 1:
            valid_passwds += 1
