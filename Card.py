#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import math


class Card(object):
    def __init__(self, people_num, per_people_card_number):
        self.Card_Pair = math.ceil(people_num * per_people_card_number / 52)  # 多少副牌
        self.Original_Cards = ('A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K')  # 原始牌
        self.Original_Cards_Numbers = (0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0)  # 原始牌对应的牌的大小
        self.Card_Types = ('♠', '♥', '❀', '♦')  # 牌的类型
        self.Remaining_Cards = self.__all_cards()  # 目前剩余牌

    # 洗牌
    def shuffle_cards(self):
        """洗牌，重新获取所有牌"""
        self.Remaining_Cards = self.__all_cards()

    def __iter__(self):
        return self

    # 获取下一张牌
    def __next__(self):
        card_len = len(self.Remaining_Cards)
        if card_len == 0:  # 如果没有牌，则洗牌
            self.shuffle_cards()
            card_len = len(self.Remaining_Cards)
        random_num = random.randint(0, card_len - 1)
        x = self.Remaining_Cards[random_num]
        self.Remaining_Cards.remove(x)
        return x

    # 获取所有牌
    def __all_cards(self):
        card_types = self.Card_Types
        cards = []
        for i in range(len(card_types)):
            cards += self.__type_all_cards(card_types[i])
        cards *= self.Card_Pair
        return cards

        # 获取单个类型的所有牌

    # 获取某个类型的所有牌
    def __type_all_cards(self, card_type):
        ori_cards = self.Original_Cards
        cards = [''] * len(ori_cards)
        for i in range(len(cards)):
            if isinstance(ori_cards[i], int):
                cards[i] = str(ori_cards[i]) + card_type
            else:
                cards[i] = ori_cards[i] + card_type
        return cards


if __name__ == '__main__':
    card_class = Card(1)
    card_iter = iter(card_class)
    all_card_len = 52
    for i in range(all_card_len):
        print(next(card_iter))
