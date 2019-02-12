#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Card
import CalculatePoints
import math


class BullFighting(object):
    def __init__(self, people_number):
        self.People_Number = people_number  # 人数
        self.Per_Card_Num = 5  # 每个人的牌数
        self.Card_Method = Card.Card(self.People_Number, self.Per_Card_Num)
        self.Score = {}
        for i in range(self.People_Number):
            self.Score[i] = 0

    # 发牌
    def deal_cards(self):
        """给每个人发指定张数的牌，返回二维列表"""
        # 会导致返回泪飙内的每一条都相同，结合存在字符串的驻留[string interning])，原理估计相同
        # all_cards = [[''] * self.Per_Card_Num] * self.People_Number
        all_cards = []
        card_iter = iter(self.Card_Method)
        self.whether_shuffle_cards()
        for card_index in range(5):
            for people_index in range(self.People_Number):
                if people_index > len(all_cards) - 1:
                    all_cards.append([''] * self.Per_Card_Num)
                all_cards[people_index][card_index] = next(card_iter)
        return all_cards

    # 判断是否洗牌
    def whether_shuffle_cards(self):
        """判断是否洗牌，如果剩余牌数不够，则洗牌"""
        remaining_cards = self.Card_Method.Remaining_Cards
        if len(remaining_cards) < self.People_Number * 5:
            self.Card_Method.shuffle_cards()

    def compare_cards(self, all_cards):
        """默认索引0的牌为庄家"""
        calculate_points_method = CalculatePoints.CalculatePoints()
        index = 1
        all_cards_len = len(all_cards)
        while index < all_cards_len:
            score = calculate_points_method.cards_compare(all_cards[0], all_cards[index])
            # print(all_cards[0], "与", all_cards[index], '比牌,得分：', score)
            self.Score[0] = self.Score[0] + score
            self.Score[index] = self.Score[index] - score
            index += 1


if __name__ == '__main__':
    people_number = 10
    times = 100000
    bull_fighting = BullFighting(people_number)
    for i in range(times):
        all_cards = bull_fighting.deal_cards()
        bull_fighting.compare_cards(all_cards)
    print(bull_fighting.Score)
