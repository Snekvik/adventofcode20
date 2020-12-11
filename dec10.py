# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 12:43:27 2020

@author: kristians
"""

import os
import pandas as pd

curdir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(curdir, "input10.txt"), "r") as f:
    jolts = [float(number) for number in f.readlines()]

jolts = pd.Series(jolts).sort_values().reset_index(drop=True)
jolts = jolts.append(pd.Series({-1: 0, len(jolts): jolts.iloc[-1] + 3})).to_frame().sort_index()
jolts_diff = jolts.diff().fillna(jolts.iloc[0])
jolts_diff_count = jolts_diff.groupby(jolts_diff[0].values).count()

jolts["Combinations"] = 0
jolts.loc[-1, "Combinations"] = 1
for jolt_ind in jolts.index:
    jolts2 = jolts.loc[jolt_ind:, [0]].iloc[1:, :]
    destinations = jolts2[jolts2.le(jolts.loc[jolt_ind] + 3).values].index
    jolts.loc[destinations, "Combinations"] = \
        jolts.loc[jolt_ind, "Combinations"] + jolts.loc[destinations, "Combinations"]
