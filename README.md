# buy-a-house
快速计算购买北京一套房子需要首付、还款的金额，方便想要购房的朋友快速决策

# 代码使用方法
1. git clone https://github.com/xujinzh/buy-a-house.git
2. python main.py --area 89 --price 44800 --firstRate 0.3 --providentFund 1200000 --providentFundRate 3.25 --lpr 4.65 --years 25 --floatingRate 0.5

其中，area 指房屋面积，price 指房屋单价，firstRate 指首付比例，providentFund 指公积金贷款额，providentFundRate 指公积金贷款利率，lpr 指商业贷款利率，years 指贷款年限，floatingRate 是根据朝向、楼层价格调整率。

运行结果显示如下：
```python
89.0 平米(area)的房子，当单价(price)是 44800.0 元，销售价格调整比例(floatingRate)是 0.5%，首付比例(firstRate)是 30.0%，公积金最高贷款额度(providentFund)是 1200000.0 元，公积金贷款利率(providentFundRate)是 3.25%，当期 LPR(lpr) 是 4.65%，贷款年限是 25 年时：
        总价是 4007135.9999999995 元
        首付是 1202140.7999999998 元
        总剩余还款额是 2804995.1999999997 元
        商业贷款应贷款额是 1604995.1999999997 元
        商业贷款每月还款额是 9058.283441665406 元
        公积金每月还款额是 5847.794704080007 元
        每月共需还款额是 14906.078145745414 元
```

# 依赖包
- python3