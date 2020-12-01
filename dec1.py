# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 08:50:47 2020

@author: kristians
"""

import pandas as pd
import os

curdir = os.path.abspath(os.path.dirname(__file__))


def get_expenses():

    with open(os.path.join(curdir, "input1.txt"), "r") as f:
        expenses = f.readlines()

    expenses = pd.DataFrame([float(exp) for exp in expenses])

    return expenses


def sum_2e(expenses):
    """
    Sum of two expenses

    Returns
    -------
    sum_exp : TYPE
        DESCRIPTION.

    """

    sum_exp = (
        pd.concat([expenses] * len(expenses), axis=1)
        + pd.concat([expenses.T] * len(expenses), axis=0).values
    )
    sum_exp.columns = sum_exp.index

    return sum_exp


def sum_3e(expenses):

    sum_2exp = sum_2e(expenses).stack()

    sum_exp = (
        pd.concat([sum_2exp] * len(expenses), axis=1)
        + pd.concat([expenses.T] * len(sum_2exp), axis=0).values
    )

    return sum_exp


expenses = get_expenses()

sum_2exp = sum_2e(expenses)

prod_2e = expenses[(sum_2exp == 2020).any(0)].product()

sum_3exp = sum_3e(expenses)

prod_3e = expenses[(sum_3exp==2020).any(0)].product()

# sum_exp[sumsum_exp_exp == 2020]