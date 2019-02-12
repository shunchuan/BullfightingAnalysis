#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""计分规则"""
Scoring_Rule = {8: 2, 9: 2, 0: 3}


class CalculatePoints(object):
    # 数张牌进行冒泡排序
    def card_bubble_sort(self, objs):
        """数张牌进行冒泡排序"""
        obj_len = len(objs)
        for i in range(obj_len):
            for j in range(obj_len - i - 1):
                first_card, sec_card = objs[j], objs[j + 1]
                if self.card_compare(first_card, sec_card) > 0:
                    objs[j], objs[j + 1] = sec_card, first_card
        return objs

    # 获取点数对应的积分数
    def card_score(self, num):
        """获取点数对应的积分数"""
        if num > 20:
            num %= 10
            return Scoring_Rule.get(num, 1)
        return 1

    # 两张牌比较
    def card_compare(self, first_card, sec_card):
        """两张牌比较，如果first>second 返回正数，相等返回0，否则返回负数"""
        if first_card == sec_card:
            return 0
        prefix1 = self.card_prefix(first_card)
        prefix2 = self.card_prefix(sec_card)

        if prefix1 == prefix2:
            suffix1 = first_card[len(first_card) - 1]
            suffix2 = sec_card[len(sec_card) - 1]
            if self.card_type_compare(suffix1, suffix2):
                return 1
        elif self.card_num_transform(prefix1) > self.card_num_transform(prefix2):
            return 1
        return -1

    # 获取牌前缀
    def card_prefix(self, card):
        """获取牌的前缀(数字,10♠即10)"""
        if len(card) > 2:
            return card[0:2]
        else:
            return card[0]

    # 判断花形大小
    def card_type_compare(self, obj1, obj2):
        """判断obj1花形是否大于obj2"""
        if obj1 == "♠":
            return True
        if obj1 == "♥" and obj2 != "♠":
            return True
        if obj1 == "❀" and obj2 != "♠" and obj1 != "♥":
            return True
        return False

    # 将牌数转为数字
    def card_num_transform(self, obj):
        """将牌数转为数字"""
        if obj == 'A':
            return 1
        if obj == 'J':
            return 11
        if obj == 'Q':
            return 12
        if obj == 'K':
            return 13
        return int(obj)

    # 获取除给定索引的牌外，其他牌的总和
    def card_other_sum(self, cards, first_index, sec_index, three_index):
        """获取除给定索引的牌外，其他牌的总和"""
        result = 0
        for i in range(len(cards)):
            if i != first_index and i != sec_index and i != three_index:
                num = self.card_prefix(cards[i])
                num = self.card_num_transform(num)
                if num >= 10:
                    num = 0
                result += num
        result %= 10
        if result == 0:
            return 10
        return result

    # 计算是否为牛
    def calculate_points(self, cards, first_index=1, sec_index=2, three_index=3):
        """递归遍历计算三张牌的点数是否为10的倍数,如果为10倍数，则结果为20+其他两张牌%10(牛牛则返回30)，否则为0"""
        first_card_num = self.card_prefix(cards[first_index])
        sec_card_num = self.card_prefix(cards[sec_index])
        three_card_num = self.card_prefix(cards[three_index])
        first_card_num = self.card_num_transform(first_card_num)
        sec_card_num = self.card_num_transform(sec_card_num)
        three_card_num = self.card_num_transform(three_card_num)
        if first_card_num >= 10:
            first_card_num = 0
        if sec_card_num >= 10:
            sec_card_num = 0
        if three_card_num >= 10:
            three_card_num = 0
        if (first_card_num + sec_card_num + three_card_num) % 10 == 0:
            return 20 + self.card_other_sum(cards, first_index, sec_index, three_index)
        else:
            cards_len = len(cards)
            if three_index < cards_len - 1:  # 第三个非最后一张牌
                three_index += 1
            elif sec_index < cards_len - 2:  # 第三个为最后一张牌，但第二个非倒数第二张牌
                sec_index += 1
                three_index = sec_index + 1
            elif first_index < cards_len - 3:  # 第三个为最后一张牌，第二个为倒数第二张牌，但第一个不为倒数第三张牌
                first_index += 1
                sec_index = first_index + 1
                three_index = sec_index + 1
            else:
                return 0
            return self.calculate_points(cards, first_index, sec_index, three_index)

    # 两手牌比较
    def cards_compare(self, first_cards, sec_cards):
        """两手牌比较，并返回对应得分，牌相同则first_cards赢"""
        first_score = self.calculate_points(first_cards)
        sec_score = self.calculate_points(sec_cards)
        if first_score == sec_score:
            first_cards = self.card_bubble_sort(first_cards)
            sec_cards = self.card_bubble_sort(sec_cards)
            cards_len = len(first_cards)
            for i in range(cards_len):
                compare_result = self.card_compare(first_cards[cards_len - 1 - i], sec_cards[cards_len - 1 - i])
                if compare_result == 0:
                    continue
                elif compare_result == 1:
                    return self.card_score(first_score)
                else:
                    return 0 - self.card_score(sec_score)
            return self.card_score(first_score)  # 均相同则取第一个
        elif first_score > sec_score:
            return self.card_score(first_score)
        else:
            return 0 - self.card_score(sec_score)


if __name__ == '__main__':
    data = ['J♠', '8❀', '10♥', 'J♥', 'J♦']
    print(data[0])
    data1 = '10♥'
    print(data[2][0:2])
    method = CalculatePoints()
    print(method.card_bubble_sort(data))
    print(method.calculate_points(data, 0, 1, 2))
