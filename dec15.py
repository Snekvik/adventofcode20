# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 06:33:53 2020

@author: kristians
"""


def find_numbers(start_numb, end_round=2020):

    turn_numb = start_numb
    start_round = max([sn for sn in start_numb]) + 1

    for turn in range(start_round, end_round + 1):

        # Prev Number Spoken
        prev_num = turn_numb[turn - 1]

        # Rounds where Number were spoken
        prev_rnd = [round for round in turn_numb if turn_numb[round] == prev_num]

        if len(prev_rnd) == 1:
            turn_numb[turn] = 0
        else:
            turn_numb[turn] = prev_rnd[-1] - prev_rnd[-2]

    return turn_numb


def find_numbers2(start_numb, end_round=2020):

    turn_numb = {sn: [0, turn + 1] for turn, sn in enumerate(start_numb)}
    start_round = len(start_numb) + 1

    # Prev Number Spoken
    prev_num = start_numb[-1]

    for turn in range(start_round, end_round + 1):

        # Turns since previous number was spoken is current number
        spoken = turn_numb[prev_num][0]
        start_numb.append(spoken)

        if spoken in turn_numb.keys():
            prev_turn = turn_numb[spoken][1]
            turn_numb[spoken] = [turn - prev_turn, turn]
        else:
            turn_numb[spoken] = [0, turn]

        prev_num = spoken

    return turn_numb, start_numb


# turn_numb = find_numbers({1: 16, 2: 1, 3: 0, 4: 18, 5: 12, 6: 14, 7: 19}, end_round=30000000)
# turn_numb = find_numbers({1: 16, 2: 1, 3: 0, 4: 18, 5: 12, 6: 14, 7: 19}, end_round=2020)
# turn_numb = find_numbers({1: 1, 2: 3, 3: 2})
# turn_numb = find_numbers({1: 2, 2: 1, 3: 3})
# turn_numb = find_numbers({1: 3, 2: 1, 3: 2})

# turn_numb2, start_numb = find_numbers2([16, 1, 0, 18, 12, 14, 19], end_round=30000000)
# turn_numb2, start_numb = find_numbers2([1, 3, 2])
# turn_numb2, start_numb = find_numbers2([2, 1, 3])
turn_numb2, start_numb = find_numbers2([3, 1, 2])
