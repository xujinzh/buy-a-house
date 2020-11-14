# buy-a-house
快速计算购买北京一套房子需要首付、还款的金额，方便想要购房的朋友快速决策

# 代码使用方法
1. git clone https://github.com/xujinzh/buy-a-house.git
2. python main.py --area 88 --price 44800 --floatingRate 5.0 --firstRate 30 --providentFund 1200000 --providentFundRate 3.25 --lpr 5.4 --years 25

其中，area 指房屋面积，price 指房屋单价，firstRate 指首付比例，providentFund 指公积金贷款额，providentFundRate 指公积金贷款利率，lpr 指商业贷款利率，years 指贷款年限，floatingRate 是根据朝向、楼层价格调整率。

运行结果显示如下：
```python
88.0 平米(area)的房子，当单价(price)是 44800.0 元，销售价格调整比例(floatingRate)是 5.0%，首付比例(firstRate)是 30.0%，公积金最高贷款额度(provident
Fund)是 1200000.0 元，公积金贷款利率(providentFundRate)是 3.25%，当期 LPR(lpr) 是 5.4%，贷款年限是 25 年(years)时：
        真实单价是 47040.0 元/平米
        总价是 4139520.0 元
        首付是 1241856.0 元
        总剩余还款额是 2897664.0 元
        商业贷款额是 1697664.0 元
        商业贷款每月还款额是 10324.002681068872 元
        公积金每月还款额是 5847.794704080007 元
        每月共需还款额是 16171.797385148879 元
```

# 依赖包
- python3