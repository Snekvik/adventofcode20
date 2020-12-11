# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 11:06:31 2020

@author: kristians
"""

import os

curdir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(curdir, "input8.txt"), "r") as f:
    commands0 = tuple(f.readlines())


def val_acc(commands):
    used = []
    pos = 0
    command = commands[pos]
    accumulator = 0
    while pos not in used:
        used.append(pos)

        if command[:command.find(" ")] == "acc":
            accumulator = accumulator + eval(command[command.find(" "):command.find("\n")])
        if command[:command.find(" ")] in ["acc", "nop"]:
            pos += 1
        else:
            pos = pos + eval(command[command.find(" "):command.find("\n")])
        if pos >= len(commands):
            return pos, accumulator
        command = commands[pos]

    return pos, accumulator


final_pos = 0
com_number = -1

while final_pos < len(commands0):
    commands = [cmd for cmd in commands0]
    com_number += 1
    command = commands[com_number]
    if command[:command.find(" ")] == "acc":
        continue
    if command[:command.find(" ")] == "jmp":
        command = command.replace("jmp", "nop")
    elif command[:command.find(" ")] == "nop":
        command = command.replace("nop", "jmp")
    commands[com_number] = command
    final_pos, accumulator = val_acc(commands)

    #

