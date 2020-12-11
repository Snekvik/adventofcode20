# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 08:00:52 2020

@author: kristians
"""

import os
import pandas as pd

curdir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(curdir, "input5.txt"), "r") as f:
    seats = f.readlines()


def find_row(seat):
    seat_row = 0
    for n in range(7):
        if seat[n] == "B":
            seat_row = seat_row + 2 ** (6 - n)
    return seat_row


def find_column(seat):
    seat_col = 0
    for n in range(3):
        if seat[n + 7] == "R":
            seat_col = seat_col + 2 ** (2 - n)
    return seat_col


rows = [find_row(seat) for seat in seats]
cols = [find_column(seat) for seat in seats]
seat_info = pd.DataFrame({"Code": seats, "Row": rows, "Column": cols})
seat_info["ID"] = seat_info["Row"] * 8 + seat_info["Column"]
seat_info = seat_info.set_index("ID").sort_index()
print(seat_info[(seat_info.reset_index().ID.diff() == 2).values])