#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Jinzhong Xu
# @Contact : jinzhongxu@csu.ac.cn
# @Time    : 2020/11/13 19:28
# @File    : house.py
# @Software: PyCharm

from utils import repayment


def loan_details(price=44800, area=89, first_rate=0.3, provident_fund=1200000, pro_fund_rate=0.0325, LPR=0.0465,
                 years=25):
    """
    计算购买一套房子需要贷款和还款金额
    :param price: 房屋每平米价格
    :param area: 房屋面积
    :param first_rate: 首付比例
    :param provident_fund: 公积金贷款额度
    :param pro_fund_rate: 公积金贷款利率
    :param LPR: LPR即商贷利率
    :param years: 贷款年限
    :return: 贷款和等额本金还款信息
    """
    # 房屋总价格
    total_price = price * area
    # 首付
    first_pay = total_price * first_rate
    # 总剩余还款额
    total_remainder = total_price - first_pay
    # 剔除公积金贷款后，商业贷款额
    commercial_pay = total_remainder - provident_fund
    # 公积金贷款每月还款额
    pro_fund_pay_month = repayment.monthly_repayment(capital=provident_fund, interest_rate=pro_fund_rate, years=years)
    # 商业贷款每月还款额
    business_pay_month = repayment.monthly_repayment(capital=commercial_pay, interest_rate=LPR, years=years)
    print(
        "{6} 平米(area)的房子，当单价(price)是 {0} 元，首付比例(firstRate)是 {1}，公积金最高贷款额度(providentFund)是 {2} 元，"
        "公积金贷款利率(providentFundRate)是 {3}，当期 LPR(lpr) 是 {4}，"
        "贷款年限是 {5} 年时：".format(price, first_rate, provident_fund, pro_fund_rate, LPR, years, area))
    print("\t总价是 {} 元".format(total_price))
    print("\t首付是 {} 元".format(first_pay))
    print("\t总剩余还款额是 {} 元".format(total_remainder))
    print("\t商业贷款应贷款额是 {} 元".format(commercial_pay))
    print("\t商业贷款每月还款额是 {} 元".format(business_pay_month))
    print("\t公积金每月还款额是 {} 元".format(pro_fund_pay_month))
    print("\t每月共需还款额是 {} 元".format(pro_fund_pay_month + business_pay_month))


if __name__ == '__main__':
    loan_details()
