# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 06:09:32 2020

@author: kristians
"""
import pandas as pd
import numpy as np
import os

curdir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(curdir, "input13.txt"), "r") as f:
    buss_info = f.readlines()

t0 = int(buss_info[0])
busses = [int(bus) for bus in buss_info[1].replace(",x", "").split(",")]


def bus_info(t0, busses):
    time_to_next = [np.ceil(t0 / bus) * bus - t0 for bus in busses]
    next_busses = pd.Series(dict(zip(busses, time_to_next)), name="Time to Next")
    return next_busses


target_delays = pd.Series({
    bus: buss_info[1].replace("\n", "").split(",").index(str(bus)) for bus in busses
}).sort_index().to_frame(name="Delay")
target_delays["MinDelay"] = target_delays.apply(lambda x: x % x.name, axis=1)


# check period of target delays for two busses first, then add one buss at a time

period = target_delays.index[1]
first_correct = period - target_delays.MinDelay.iloc[1]
for tdi in target_delays.iloc[1:].index:
    wrong_delay = True
    t0 = first_correct
    target_delays2 = target_delays.loc[:tdi].MinDelay
    while wrong_delay:
        next_busses = bus_info(t0, busses=target_delays.index.to_list()).loc[target_delays.index]
        next_busses2 = next_busses.loc[:tdi]
        if next_busses2.eq(target_delays2).all():
            wrong_delay = False
        else:
            t0 += period
    first_correct = t0
    t0 += period
    wrong_delay = True
    while wrong_delay:
        next_busses = bus_info(t0, busses=target_delays.index.to_list()).loc[target_delays.index]
        next_busses2 = next_busses.loc[:tdi]
        if next_busses2.eq(target_delays2).all():
            wrong_delay = False
        else:
            t0 += period
    period = t0 - first_correct
