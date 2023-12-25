'''
    oldmaid_rule.py
    
    ・ルールクラス
    
		属性
            ・プレイヤーの手札
			・テーブル
            
		操作
            ・テーブルに置けるカードを探す
    
    2023/11/17 by kepohon
    2023/11/13 by kepohon
'''

import trump
'''
from .player import Player
from .hand import Hand
from .table import Table
from .card import Card
'''

class OldmaidRule(trump.Rule):
    _candidate = None
    def __init__(self):
        pass

    #            ・テーブルに置けるカードを探す
    #               ・同じ数字のカードがあれば、テーブルに捨てる
    def findCandidate(self, hand, table):
        sameCards = [0,0]
        cardCount = hand.getNumberOfCard()
        if cardCount >= 2:
            orgIndex = 0
            sameIndex = 1
            orgCard = hand._hand[0]
            while True:
                if hand._hand[orgIndex].getNumber() == hand._hand[sameIndex].getNumber():
                    sameCards[1] = hand.pickCard(sameIndex)
                    sameCards[0] = hand.pickCard(orgIndex)
                    return sameCards
                if sameIndex == (cardCount-1):
                    if orgIndex == (cardCount-2):
                        return None
                    else:
                        orgIndex += 1
                        sameIndex = orgIndex + 1
                else:
                    sameIndex += 1
    
    def isThereCard(self, table, suit, number):
        cards = table.getCards()
        if cards[suit][number] != None:
            return True
        return False
    
    
