#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: Mxyzptlk
# Date: 2018/8/13

import random


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.suit}{self.value}"


class Deck:
    def __init__(self, quantity=1):
        # '\u2660', '\u2663', '\u2665', '\u2666' ♠ ♣ ♥ ♦
        suits = ['\u2660', '\u2663', '\u2665', '\u2666']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(value, suit) for suit in suits for value in values]
        self.cards.append(Card('Black', 'Joker'))
        self.cards.append(Card('Colored', 'Joker'))
        self.cards *= quantity
        print(self.cards)
        print(len(self.cards))


class Player:
    def __init__(self, player, team, hand, score):
        self.player = player
        self.team = team
        self.hand = hand
        self.score = score


Deck(2)

print(random.randint(1, 4))
