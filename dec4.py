# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 12:04:08 2020

@author: kristians
"""

import os

CURDIR = os.path.abspath(os.path.dirname(__file__))

passports = {}
pp_num = 0
with open(os.path.join(CURDIR, "input4.txt"), "r") as f:
    line = f.readline()
    passport = {}
    while line:
        line = line.replace("\n", "")
        if len(line) > 0:
            line_ind2 = 0
            line_ind1 = 0
            while line_ind2 < len(line):
                line_ind2 = line.find(" ", line_ind1) if (
                    line.find(" ", line_ind1) >= 0
                ) else len(line)
                field = line[line_ind1: line.find(":", line_ind1)]
                value = line[(line.find(":", line_ind1) + 1): line_ind2]
                passport[field] = value
                line_ind1 = line_ind2 + 1
        else:
            passports[pp_num] = passport
            pp_num += 1
            if len(passports) == 275:
                print("add one more")
            passport = {}
        line = f.readline()
    passports[pp_num] = passport

invalid_pps = {}
invalid_pp = {passport: passports[passport] for passport in passports if len(
    {'byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid'} - {pk for pk in passports[passport].keys()}
) != 0}
invalid_pps = {**invalid_pps, ** invalid_pp}

# Birth Year
valid_passports = [passport for passport in valid_passports if (
    (int(passport["byr"]) >= 1920) & (int(passport["byr"]) <= 2002)
)]

# Issure Year
valid_passports = [passport for passport in valid_passports if (
    (int(passport["iyr"]) >= 2010) & (int(passport["iyr"]) <= 2020)
)]

# Expire Year
valid_passports = [passport for passport in valid_passports if (
    (int(passport["eyr"]) >= 2020) & (int(passport["iyr"]) <= 2030)
)]

# Height
passports_cm = [passport for passport in valid_passports if (
    (passport["hgt"][-2:] == "cm")
)]
val_pp_cm = [passport for passport in passports_cm if (
    (int(passport["hgt"][:passport["hgt"].find("cm")]) >= 150)
    & (int(passport["hgt"][:passport["hgt"].find("cm")]) <= 193)
)]
passports_in = [passport for passport in valid_passports if (
    (passport["hgt"][-2:] == "in")
)]
val_pp_in = [passport for passport in passports_in if (
    (int(passport["hgt"][:passport["hgt"].find("in")]) >= 150)
    & (int(passport["hgt"][:passport["hgt"].find("in")]) <= 193)
)]
valid_passports = val_pp_cm + val_pp_in

# hair color
valid_passports = [passport for passport in valid_passports if passport["hcl"][0] == "#"]
hcl_chars = [str(n) for n in range(10)] + ["a", "b", "c", "d", "e", "f", "#"]


def valid_hcl_char(word):
    for hcl_char in word:
        if hcl_char not in hcl_chars:
            return False
    return True


valid_passports = [passport for passport in valid_passports if valid_hcl_char(passport["hcl"])]

# Eye color
eyecolors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
valid_passports = [passport for passport in valid_passports if len(passport["ecl"]) == 3]
valid_passports = [passport for passport in valid_passports if passport["ecl"] in eyecolors]

# Passport ID
valid_passports = [passport for passport in valid_passports if len(passport["pid"]) == 9]

# print([passport["pid"] for passport in valid_passports])

int(234)
