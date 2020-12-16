# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 06:28:03 2020

@author: kristians
"""
import os
import pandas as pd
import copy

curdir = os.path.abspath(os.path.dirname(__file__))
mem = dict()


def _mask_bin(bin_value, mask):

    bin_value = list(bin_value)
    for replacement in ["0", "1"]:
        start_ind = 0
        mask_ind = 1
        while mask_ind > -1:
            mask_ind = mask.find(replacement, start_ind)
            if mask_ind == -1:
                continue
            bin_value[mask_ind] = mask[mask_ind]
            start_ind = mask_ind + 1
    bin_value = "".join(bin_value)
    return bin_value


def mask_input():
    with open(os.path.join(curdir, "input14.txt"), "r") as f:
        docking_input = f.readline().replace("\n", "")
        while docking_input:
            if docking_input.startswith("mask"):
                mask = docking_input[(docking_input.find(" = ") + 3):]
            elif docking_input.startswith("mem"):
                value = int(docking_input[(docking_input.find(" = ") + 3):])
                bin_value = bin(value)[2:]
                bin_value = bin_value.rjust(len(mask), "0")

                # Replace 0 and 1
                bin_value =_mask_bin(bin_value, mask)

                value = int("0b" + bin_value, 2)
                exec(docking_input[: (docking_input.find(" = ") + 3)] + str(value))

            docking_input = f.readline().replace("\n", "")
    return mem


def mask_address(docking_inputs):
    for docking_input in docking_inputs:
        docking_input = docking_input.replace("\n", "")
        if docking_input.startswith("mask"):
            mask = docking_input[(docking_input.find(" = ") + 3):]
        elif docking_input.startswith("mem"):
            value = int(docking_input[(docking_input.find(" = ") + 3):])
            address = docking_input[(docking_input.find("[") + 1): docking_input.find("]")]
            bin_address = bin(int(address))[2:]
            bin_address = bin_address.rjust(len(mask), "0")
            bin_address = list(bin_address)

            # Overwrite with 1
            start_ind = 0
            mask_ind = 1
            while mask_ind > -1:
                mask_ind = mask.find("1", start_ind)
                if mask_ind == -1:
                    continue
                bin_address[mask_ind] = "1"
                start_ind = mask_ind + 1

            # floating bits creates multiple addresses
            addresses = (bin_address, )
            start_ind = 0
            mask_ind = 1
            addresses2 = list()
            while mask_ind > -1:
                mask_ind = mask.find("X", start_ind)
                if mask_ind == -1:
                    continue

                for adrs in addresses:
                    adrs[mask_ind] = "1"
                    addresses2.append(copy.copy(adrs))
                    adrs[mask_ind] = "0"
                    addresses2.append(adrs)
                addresses = tuple(addresses2)
                addresses2 = list()
                start_ind = mask_ind + 1

            for bin_addrs in addresses:
                addrs = int("0b" + "".join(bin_addrs), 2)
                mem[addrs] = value

    return mem


with open(os.path.join(curdir, "input14.txt"), "r") as f:
    docking_input = f.readlines()


# docking_input = [
#     "mask = 000000000000000000000000000000X1001X",
#     "mem[42] = 100",
#     "mask = 00000000000000000000000000000000X0XX",
#     "mem[26] = 1"
# ]

# mem = mask_input()
mem = mask_address(docking_input)
# bin_value =_mask_bin("000000000000000000000000000000000000", "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", replacement="0")
# bin_value =_mask_bin(bin_value, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", replacement="1")

print(pd.Series(mem).sum())

