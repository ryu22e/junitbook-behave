#!/usr/bin/env python
# -*- coding: utf-8 -*-


class NoPair(object):
    def __hash__(self):
        return 17

    def __eq__(self, other):
        return isinstance(other, self.__class__)


class OnePair(object):
    def __init__(self, no):
        self.no = no

    def __hash__(self):
        prime = 31
        result = 1
        result = prime * result + self.no
        return result

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.no == other.no


class Pat(object):
    @classmethod
    def make(cls, hands):
        nums = {}
        for card in hands:
            count = nums.get(str(card.no), 0)
            count += 1
            nums[str(card.no)] = count
        for k, v in nums.items():
            if v == 2:
                return OnePair(k)
        return NoPair()


Pat.NO_PAIR = NoPair()
