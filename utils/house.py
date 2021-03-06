#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Jinzhong Xu
# @Contact : jinzhongxu@csu.ac.cn
# @Time    : 2020/11/13 19:28
# @File    : house.py
# @Software: PyCharm

from utils import repayment


def loan_details(price=44800, area=88, first_rate=30, provident_fund=1200000, pro_fund_rate=3.25, lpr=5.4, years=25,
                 floating_rate=5.0):
    """
    计算购买一套房子需要贷款和还款金额
    :param floating_rate: 根据具体楼层、朝向在±5%的范围内调整销售价格
    :param price: 房屋每平米价格
    :param area: 房屋面积
    :param first_rate: 首付比例
    :param provident_fund: 公积金贷款额度
    :param pro_fund_rate: 公积金贷款利率
    :param lpr: LPR 即商贷利率
    :param years: 贷款年限
    :return: 贷款和等额本金还款信息
    """
    truth_price = price * (1 + (floating_rate / 100))
    pro_fund_rate = pro_fund_rate / 100
    lpr = lpr / 100
    first_rate = first_rate / 100
    # 房屋总价格
    total_price = truth_price * area
    # 首付
    first_pay = total_price * first_rate
    # 总剩余还款额
    total_remainder = total_price - first_pay
    # 剔除公积金贷款后，商业贷款额
    commercial_pay = total_remainder - provident_fund
    # 公积金贷款每月还款额
    pro_fund_pay_month = repayment.monthly_repayment(capital=provident_fund, interest_rate=pro_fund_rate, years=years)
    # 商业贷款每月还款额
    business_pay_month = repayment.monthly_repayment(capital=commercial_pay, interest_rate=lpr, years=years)
    print(
        "{6} 平米(area)的房子，当单价(price)是 {0} 元，销售价格调整比例(floatingRate)是 {7}%，首付比例(firstRate)是 {1}%，"
        "公积金最高贷款额度(providentFund)是 {2} 元，"
        "公积金贷款利率(providentFundRate)是 {3}%，当期 LPR(lpr) 是 {4}%，"
        "贷款年限是 {5} 年(years)时：".format(price, first_rate * 100, provident_fund, pro_fund_rate * 100, lpr * 100,
                                      years, area, floating_rate))
    print("\t真实单价是 {} 元/平米".format(truth_price))
    print("\t总价是 {} 元".format(total_price))
    print("\t首付是 {} 元".format(first_pay))
    print("\t总剩余还款额是 {} 元".format(total_remainder))
    print("\t商业贷款额是 {} 元".format(commercial_pay))
    print("\t商业贷款每月还款额是 {} 元".format(business_pay_month))
    print("\t公积金每月还款额是 {} 元".format(pro_fund_pay_month))
    print("\t每月共需还款额是 {} 元".format(pro_fund_pay_month + business_pay_month))


if __name__ == '__main__':
    loan_details()
