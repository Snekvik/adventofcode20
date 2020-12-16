# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 06:18:16 2020

@author: kristians
"""

import os

MY_TICKET = [
    109, 101, 79, 127, 71, 59, 67, 61, 173, 157, 163, 103, 83, 97, 73, 167, 53, 107, 89, 131
]

CURDIR = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(CURDIR, "input16a.txt"), "r") as f:
    valid_values = f.readlines()

valid_numbers = dict()
for vv in valid_values:
    pos1 = vv.find(": ") + 2
    pos2 = vv.find("-", pos1)
    pos3 = vv.find(" ", pos2)
    pos4 = vv.find("-", pos3)
    num1 = vv[pos1: pos2]
    num2 = vv[(pos2 + 1): pos3]
    num3 = vv[(pos3 + 4): pos4]
    num4 = vv[(pos4 + 1):].replace("\n", "")
    field = vv[:vv.find(":")]
    valid_numbers[field] = set([r for r in range(int(num1), int(num2) + 1)]).union(
        set([r for r in range(int(num3), int(num4) + 1)])
    )

with open(os.path.join(CURDIR, "input16b.txt"), "r") as f:
    f.readline()
    tickets = f.readlines()

all_valid = set()
for vn in valid_numbers:
    all_valid.update(valid_numbers[vn])

tickets_list = [[int(num) for num in ticket.replace("\n", "").split(",")] for ticket in tickets]

invalid_values = []
invalid_tickets = []
for ticket in tickets_list:
    discard_ticket = False
    for value in ticket:
        if value not in all_valid:
            invalid_values.append(value)
            discard_ticket = True
    if discard_ticket:
        invalid_tickets.append(ticket)

for it in invalid_tickets:
    tickets_list.remove(it)

correct_field = dict()
remaining_fields = [vnk for vnk in valid_numbers.keys()]
while len(correct_field) < 20:
    for value_number in range(len(valid_values)):
        values = set([ticket[value_number] for ticket in tickets_list])
        the_field = []
        for field in remaining_fields:

            # values not in field
            vnif = values.difference(valid_numbers[field])
            if len(vnif) == 0:
                the_field.append(field)
        if len(the_field) == 1:
            correct_field[the_field[0]] = value_number
            remaining_fields.remove(the_field[0])

print([MY_TICKET[field] for field in [
    correct_field[cf] for cf in correct_field if cf.startswith("departure")
]])