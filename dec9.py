# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 11:13:41 2020

@author: kristians
"""

import os
import pandas as pd

curdir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(curdir, "input9.txt"), "r") as f:
    numbers = [float(number) for number in f.readlines()]


def get_sums(prev_numbers):
    prev_sums = (
        pd.concat([prev_numbers] * len(prev_numbers), axis=1)
        + pd.concat([prev_numbers.T] * len(prev_numbers), axis=0).values
    )
    # prev_sums.index = prev_numbers.set_index(0).index
    # prev_sums.columns = prev_numbers.set_index(0).index
    prev_sums = prev_sums.stack().drop_duplicates()

    return prev_sums


def get_invalid_num(numbers):
    is_sum = True
    pos = 25
    while is_sum:
        prev_numbers = pd.DataFrame([float(pn) for pn in numbers[(pos - 25):pos]])
        prev_sums = get_sums(prev_numbers)
        if prev_sums.eq(numbers[pos]).any():
            pos += 1
        else:
            is_sum = False
    return pos


# invpos = get_invalid_num(numbers)
invpos = 659
invnum = numbers[invpos]
numbers = pd.Series(numbers)
wrong_sum = True
pos = 0
while wrong_sum:
    num_csum = numbers.loc[pos:].cumsum()
    pos2 = numbers.loc[pos:][num_csum.ge(invnum)].index[0]
    if num_csum.loc[pos2] == invnum:
        wrong_sum = False
    else:
        pos += 1

if numbers.loc[pos:pos2].sum() == invnum:
    sum_minmax = numbers.loc[pos:pos2].apply([min, max]).sum()
