#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Card(object):
    def __init__(self, suit, no):
        self.suit = suit
        self.no = no

    class Suit(object):
        DIAMONDS, SPADES, HEARTS, CLUBS = range(4)

    @classmethod
    def get(cls, suit, no):
        if not(1 <= no <= 13):
            raise AssertionError("not(1 <= no <= 13)")
        if suit == 'D':
            return Card(Card.Suit.DIAMONDS, no)
        elif suit == 'S':
            return Card(Card.Suit.SPADES, no)
        elif suit == 'H':
            return Card(Card.Suit.HEARTS, no)
        elif suit == 'C':
            return Card(Card.Suit.CLUBS, no)
        else:
            raise AssertionError("Invalid suit")

    def __hash__(self):
        prime = 31
        result = 1
        result = prime * result + self.no
        result = prime * result + 0 if self.suit is None else hash(self.suit)
        return result

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.no == other.no
