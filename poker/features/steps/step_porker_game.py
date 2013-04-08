#!/usr/bin/env python
# -*- coding: utf-8 -*-
from behave import step_matcher, given, when, then
from porker_game import PokerGame
from card import Card
from pat import Pat, OnePair


step_matcher('re')


@given(u'手札に(?P<suit1>[SHDC])(?P<no1>\\d+),(?P<suit2>[SHDC])(?P<no2>\\d+),(?P<suit3>[SHDC])(?P<no3>\\d+),(?P<suit4>[SHDC])(?P<no4>\\d+),(?P<suit5>[SHDC])(?P<no5>\\d+)が配られた')
def step_given(
        context,
        suit1, no1,
        suit2, no2,
        suit3, no3,
        suit4, no4,
        suit5, no5
        ):
    sut = PokerGame()
    sut.setUp(
            Card.get(suit1, int(no1)),
            Card.get(suit2, int(no2)),
            Card.get(suit3, int(no3)),
            Card.get(suit4, int(no4)),
            Card.get(suit5, int(no5))
            )
    context.sut = sut


@when(u'チェンジしない')
def step_when(context):
    context.sut.no_change()


@then(u'ノーペアであるべき')
def step_then_nopair(context):
    expected = Pat.NO_PAIR
    actual = context.sut.pat()
    assert actual == expected


@then(u'^(?P<no>\\d)のワンペアであるべき')
def step_then_onepair(context, no):
    expected = OnePair(no)
    actual = context.sut.pat()
    assert actual == expected
