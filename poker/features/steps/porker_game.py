#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pat import Pat


class Hands(object):
    _SIZE = 5

    def __init__(self, cards):
        if len(cards) != Hands._SIZE:
            raise AssertionError("len(cards) != Hands._SIZE")
        self.cards = []
        for card in cards:
            self.cards.append(card)

    def __iter__(self):
        for card in self.cards:
            yield card


class PokerGame(object):
    class Status(object):
        INIT, READY, CHANGED = range(3)

    def __init__(self):
        self.status = PokerGame.Status.INIT
        self.hands = None

    def setUp(self, *cards):
        if self.status != PokerGame.Status.INIT:
            raise AssertionError("self.status != PokerGame.Status.INIT:")
        self.hands = Hands(cards)
        self.status = PokerGame.Status.READY

    def no_change(self):
        if self.status != PokerGame.Status.READY:
            raise AssertionError("if self.status != PokerGame.Status.READY")
        self.status = PokerGame.Status.CHANGED

    def pat(self):
        if self.status != PokerGame.Status.CHANGED:
            raise AssertionError("self.status != PokerGame.Status.CHANGED")
        return Pat.make(self.hands)
