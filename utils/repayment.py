#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Jinzhong Xu
# @Contact : jinzhongxu@csu.ac.cn
# @Time    : 2020/11/13 19:20
# @File    : repayment.py
# @Software: PyCharm


def monthly_repayment(capital=1600000, interest_rate=0.054, years=25):
    """
    计算等额本金情况下每月的还款额
    :param capital: 本金
    :param interest_rate: 年利率
    :param years: 贷款年限
    :return: 每月还款额
    """
    monthly_interest_rate = interest_rate / 12
    months = years * 12
    return capital * (monthly_interest_rate * (1 + monthly_interest_rate) ** months) / (
            (1 + monthly_interest_rate) ** months - 1)


if __name__ == '__main__':
    month_repayment = monthly_repayment()
    print(month_repayment)
