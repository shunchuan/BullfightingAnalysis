# BullfightingAnalysis
过年娱乐纸牌《斗牛》分析
## 当前版本
- V1.0.0
- Python Version 3.6.5
## 目的
- 使用Python实现《斗牛》玩法，进行Python的初步学习。
- 初始想法是为了观察庄家在参与人数不同的情况下，胜率是否改变
## 待实现
- 发牌筛子
- 记录每局的结果，以便生成计分趋势
- 洗牌现实化，而非随机生成，模拟人工洗牌过程
## 实现
### [Card.py](https://github.com/shunchuan/BullfightingAnalysis/blob/master/Card.py)
  - 根据参与人数确认使用多少副牌
  - 随机发牌迭代器，发牌开始如果剩余牌数不足，则重新洗牌
### [CalculatePoints.py](https://github.com/shunchuan/BullfightingAnalysis/blob/master/CalculatePoints.py)
  - 自定义计分规则
  - 手牌比较，实现两个花色、两张牌、两手牌的比较
  - 点数计算，计算每手牌的总点数，如果没牛则为0，否则>20,牛牛为30
### [BullFighting.py](https://github.com/shunchuan/BullfightingAnalysis/blob/master/BullFighting.py)
  - 发牌
  - 两手牌比较并计分
## 观察结果
```
people_number= 3 times= 1000
Score Result :  {0: 24, 1: 59, 2: -83}
```
```
people_number= 4 times= 1000
Score Result :  {0: 204, 1: 10, 2: -96, 3: -118}
```
```
people_number= 8 times= 1000
Score Result :  {0: 1351, 1: -93, 2: -175, 3: -192, 4: -246, 5: -187, 6: -251, 7: -207}
```
```
people_number= 3 times= 100000
Score Result :  {0: 13403, 1: -685, 2: -12718}
```
```
people_number= 4 times= 100000
Score Result :  {0: 26889, 1: -880, 2: -11054, 3: -14955}
```
```
people_number= 8 times= 100000
Score Result :  {0: 92562, 1: -1371, 2: -12049, 3: -15967, 4: -16138, 5: -16085, 6: -15712, 7: -15240}
```
## 问题
- 第一位为庄家，发现不管参与人数为多少，庄家一直为正
