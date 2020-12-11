# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 11:48:23 2020

@author: kristians
"""

import os

CURDIR = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(CURDIR, "input7.txt"), "r") as f:
    bag_contents = f.readlines()
bag_contents = {bag_content[: bag_content.find(" bags")]: bag_content[
    (bag_content.find(" contain") + 9):
] for bag_content in bag_contents}

bag = "shiny gold"
bags_w_bags_w_bag = set([bag])
allbags_w_bag = set()

while len(bags_w_bags_w_bag) > 0:
    bags_w_bag = bags_w_bags_w_bag
    bags_w_bags_w_bag = set()
    for bag in bags_w_bag:
        with open(os.path.join(CURDIR, "input7.txt"), "r") as f:
            line = f.readline()
            while line:
                if line.find(bag) >= 0:
                    bags_w_bags_w_bag.add(line[: line.find(" bags")])
                line = f.readline()
        bags_w_bags_w_bag.discard(bag)
    allbags_w_bag = allbags_w_bag.union(bags_w_bags_w_bag)

bags_w_bags = set([bag, 1])
while bags_w_bags