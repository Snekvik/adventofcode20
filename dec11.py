# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 07:13:46 2020

@author: kristians
"""

import os
import pandas as pd

curdir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(curdir, "input11.txt"), "r") as f:
    seats = [seat.replace("\n", "") for seat in f.readlines()]
seats = pd.DataFrame([list(seat) for seat in seats])
rows, columns = seats.shape

seats_changed = True
seats2 = seats.stack().to_frame(name="State").copy()

while seats_changed:
    seats2.index.names = ["Row", "Column"]

    # State of seats around
    seats2["N"] = seats2.State.groupby(level=0).shift().fillna("L")
    shifts = 1
    while seats2["N"].eq(".").any():
        shifts += 1
        seats2.loc[seats2["N"].eq("."), "N"] = (
            seats2.State.groupby(level=0).shift(shifts).fillna("L").loc[seats2["N"].eq(".")]
        )

    seats2["NW"] = (
        seats2.State.groupby(level=0).shift().fillna("L").groupby(level=1).shift().fillna("L")
    )
    shifts = 1
    while seats2["NW"].eq(".").any():
        shifts += 1
        seats2.loc[seats2["NW"].eq("."), "NW"] = (
            seats2.State.groupby(level=0).shift(shifts).fillna("L")
            .groupby(level=1).shift(shifts).fillna("L").loc[seats2["NW"].eq(".")]
        )

    seats2["W"] = seats2.State.groupby(level=1).shift().fillna("L")
    shifts = 1
    while seats2["W"].eq(".").any():
        shifts += 1
        seats2.loc[seats2["W"].eq("."), "W"] = (
            seats2.State.groupby(level=1).shift(shifts).fillna("L").loc[seats2["W"].eq(".")]
        )

    seats2["SW"] = (
        seats2.State.groupby(level=0).shift(-1).fillna("L").groupby(level=1).shift().fillna("L")
    )
    shifts = 1
    while seats2["SW"].eq(".").any():
        shifts += 1
        seats2.loc[seats2["SW"].eq("."), "SW"] = (
            seats2.State.groupby(level=0).shift(-shifts).fillna("L")
            .groupby(level=1).shift(shifts).fillna("L").loc[seats2["SW"].eq(".")]
        )

    seats2["S"] = seats2.State.groupby(level=0).shift(-1).fillna("L")
    shifts = 1
    while seats2["S"].eq(".").any():
        shifts += 1
        seats2.loc[seats2["S"].eq("."), "S"] = (
            seats2.State.groupby(level=0).shift(-shifts).fillna("L").loc[seats2["S"].eq(".")]
        )

    seats2["SE"] = (
        seats2.State.groupby(level=0).shift(-1).fillna("L").groupby(level=1).shift(-1).fillna("L")
    )
    shifts = 1
    while seats2["SE"].eq(".").any():
        shifts += 1
        seats2.loc[seats2["SE"].eq("."), "SE"] = (
            seats2.State.groupby(level=0).shift(-shifts).fillna("L")
            .groupby(level=1).shift(-shifts).fillna("L").loc[seats2["SE"].eq(".")]
        )

    seats2["E"] = seats2.State.groupby(level=1).shift(-1).fillna("L")
    shifts = 1
    while seats2["E"].eq(".").any():
        shifts += 1
        seats2.loc[seats2["E"].eq("."), "E"] = (
            seats2.State.groupby(level=1).shift(-shifts).fillna("L").loc[seats2["E"].eq(".")]
        )

    seats2["NE"] = (
        seats2.State.groupby(level=0).shift().fillna("L").groupby(level=1).shift(-1).fillna("L")
    )
    shifts = 1
    while seats2["NE"].eq(".").any():
        shifts += 1
        seats2.loc[seats2["NE"].eq("."), "NE"] = (
            seats2.State.groupby(level=0).shift(shifts).fillna("L")
            .groupby(level=1).shift(-shifts).fillna("L").loc[seats2["NE"].eq(".")]
        )

    seats_changed = False
    # Change state to occupied
    change_ind1 = seats2[pd.merge(
        seats2.iloc[:, 1:].ne("#").all(1).to_frame("AllEmpty"),
        seats2.iloc[:, 0].eq("L").to_frame("Seat"), left_index=True, right_index=True
    ).all(1)].index

    # Change state to free
    change_ind2 = seats2[pd.merge(
        seats2.iloc[:, 1:].eq("#").sum(1).ge(5).to_frame("TooCrowded"),
        seats2.iloc[:, 0].eq("#").to_frame("Seat"), left_index=True, right_index=True
    ).all(1)].index

    if len(change_ind1) > 0:
        seats_changed = True
        seats2.loc[change_ind1, "State"] = "#"

    if len(change_ind2) > 0:
        seats_changed = True
        seats2.loc[change_ind2, "State"] = "L"
