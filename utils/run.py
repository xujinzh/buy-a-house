#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Jinzhong Xu
# @Contact : jinzhongxu@csu.ac.cn
# @Time    : 2020/11/13 19:37
# @File    : run.py
# @Software: PyCharm

from utils import house
import argparse


def just_do_it():
    ap = argparse.ArgumentParser()
    ap.add_argument('-p', '--price', required=False, type=float, default=44800, help='price per area')
    ap.add_argument('-a', '--area', required=False, type=float, default=88, help='total area of house')
    ap.add_argument('-f', '--firstRate', required=False, type=float, default=30, help='down payment ratio')
    ap.add_argument('-v', '--providentFund', required=False, type=float, default=1200000, help='provident fund loan')
    ap.add_argument('-d', '--providentFundRate', required=False, type=float, default=3.25, help='provident fund rate')
    ap.add_argument('-l', '--lpr', required=False, type=float, default=5.4, help='LPR')
    ap.add_argument('-y', '--years', required=False, type=int, default=25, help='years')
    ap.add_argument('-t', '--floatingRate', required=False, type=float, default=5.0, help='floating rate')
    args = vars(ap.parse_args())
    house.loan_details(price=args['price'], area=args['area'], first_rate=args['firstRate'],
                       provident_fund=args['providentFund'], pro_fund_rate=args['providentFundRate'], lpr=args['lpr'],
                       years=args['years'], floating_rate=args['floatingRate'])
