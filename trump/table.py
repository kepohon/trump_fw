'''
    table.py
    
    ・テーブルクラス（抽象クラス）
    
		属性
			・手札(カード配列)
            
		操作
            ・捨てられたカードを手札に加える
            ・捨てられたカードを見る
    
    2023/11/15 by kepohon
    2023/10/03 by kepohon
'''

from .card import Card

class Table:
    table_ = [None] * (Card.NUMBER_MAX * Card.SUIT_MAX)
    tableCardString_ = ""
    
    def __init__(self):
        self._createString()
    
    def __str__(self):
        return self.tableCardString_
    
    def putCard(self, card):
        suit = card.getSuit()
        number = card.getNumber()
        self.table_[suit*Card.NUMBER_MAX+number] = card
        self._createString()
    
    def getCards(self):
        return self.table_
    
    #def __str__(self):
    #    return self.tableCardString_
    
    # テーブルを文字列として表現する
    def _createString(self):
        self.tableCardString_ = ""
        numberIndex = 0
        suitIndex = 0
        for card in self.table_:
            if card == None:
                self.tableCardString_ += ".. "
            else:
                self.tableCardString_ += str(card)
                self.tableCardString_ += " "
            numberIndex += 1
            if numberIndex >= Card.NUMBER_MAX:
                suitIndex += 1
                numberIndex = 0
                self.tableCardString_ += "\n"
        return

