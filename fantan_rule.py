'''
    fantan_rule.py
    
    ・ルールクラス
    
		属性
            ・プレイヤーの手札
			・テーブル
            
		操作
            ・テーブルに置けるカードを探す
    
    2023/11/17 by kepohon
    2023/11/15 by kepohon
    2023/10/03 by kepohon
'''

import trump
from trump.card import Card

class FantanRule(trump.Rule):
    #_candidate = None
    
    def __init__(self):
        self._card = Card(0,0)
        self._candidate = None

    #            ・テーブルに置けるカードを探す
    def findCandidate(self, hand, table):
        _candidate = None
        numberOfHand = hand.getNumberOfCard()
        for position in range(numberOfHand):
            lookingCard = hand.lookCard(position)
            number = lookingCard.getNumber()
            suit = lookingCard.getSuit()
            
            if number > 1:
                leftNumber = number - 1
            else:
                leftNumber = self._card.numberMax()
                
            if number < self._card.numberMax():
                rightNumber = number + 1
            else:
                rightNumber = 1
            
            # テーブル上に現在のカードの前後のカードがあれば、その手札のカードを取り出す
            if self.isThereCard_(table, suit, leftNumber) or \
               self.isThereCard_(table, suit, rightNumber):
                _candidate = hand.pickCard(position)
                break
        
        return _candidate
    
    def isThereCard_(self, table, suit, number):
        cards = table.getCards()
        if cards[suit*self._card.numberMax()+number] != None:
            return True
        return False
    
    
