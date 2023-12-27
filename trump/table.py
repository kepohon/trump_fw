'''
    table.py
    
    ・テーブルクラス（抽象クラス）
        一次元配列を二次元配列のように使う
    
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
    #_table = [None] * ((Card.NUMBER_MAX+1) * (Card.SUIT_MAX+1))
    #_tableCardString = ""
    
    def __init__(self):
        self._card = Card(0, 0)
        self._table = [None] * (self._card.numberMax()+1) * (self._card.suitMax()+1)
        self._tableCardString = ""
        self._createString()
    
    def __str__(self):
        return self._tableCardString
    
    def putCard(self, card):
        suit = card.getSuit()
        number = card.getNumber()
        self._table[suit*self._card.numberMax()+number] = card
        self._createString()
    
    def getCards(self):
        return self._table
    
    #def __str__(self):
    #    return self._tableCardString
    
    # テーブルを文字列として表現する
    def _createString(self):
        self._tableCardString = ""
        numberIndex = 1
        suitIndex = 1
        numberOfCards = (self._card.suitMax()+1) * (self._card.numberMax()+1) 
        for index in range(numberOfCards):
            currentCard = self._table[index]
            if currentCard == None:
                self._tableCardString += ".. "
                if (index % self._card.numberMax()) == 0:
                    self._tableCardString += "\n"
                continue
            else:
                self._tableCardString += str(currentCard)
                self._tableCardString += " "
            
            if currentCard.getNumber() == self._card.numberMax():
                self._tableCardString += "\n"
        return

