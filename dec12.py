# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 06:40:31 2020

@author: kristians
"""

import os
import numpy as np

curdir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(curdir, "input12.txt"), "r") as f:
    directions = f.readlines()

# Let 0 degrees be eastward, 90 degrees southward etc
# This means that the first coordinate is W->E and the second N->S

# mapping from direction to degrees
dir_deg = {"E": 0, "S": 90, "W": 180, "N": 270}

# position of ship
position = [0, 0]

# Relative position of way point
pos_wp = [10, -1]

# initial angle
angle = np.rad2deg(np.arctan2(pos_wp[1], pos_wp[0]))

for direction in directions:
    if direction[0] in ["N", "S", "E", "W"]:
        dir_angle = np.deg2rad(dir_deg[direction[0]])
        pos_wp[0] = pos_wp[0] + np.round(int(direction[1:]) * np.cos(dir_angle))
        pos_wp[1] = pos_wp[1] + np.round(int(direction[1:]) * np.sin(dir_angle))
        angle = np.rad2deg(np.arctan2(pos_wp[1], pos_wp[0]))
    elif direction[0] == "R":
        angle = angle + int(direction[1:])
        if angle >= 360:
            angle = angle - 360
        dist_wp = np.linalg.norm(pos_wp)
        pos_wp[0] = np.round(dist_wp * np.cos(np.deg2rad(angle)))
        pos_wp[1] = np.round(dist_wp * np.sin(np.deg2rad(angle)))
    elif direction[0] == "L":
        angle = angle - int(direction[1:])
        if angle <= 0:
            angle = angle + 360
        dist_wp = np.linalg.norm(pos_wp)
        pos_wp[0] = np.round(dist_wp * np.cos(np.deg2rad(angle)))
        pos_wp[1] = np.round(dist_wp * np.sin(np.deg2rad(angle)))
    elif direction[0] == "F":
        position[0] = position[0] + np.round(
            int(direction[1:]) * np.linalg.norm(pos_wp) * np.cos(np.deg2rad(angle))
        )
        position[1] = position[1] + np.round(
            int(direction[1:]) * np.linalg.norm(pos_wp) * np.sin(np.deg2rad(angle))
        )
    else:
        print("This is not happening")
