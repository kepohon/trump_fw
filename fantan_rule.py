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
    candidate = None
    def __init__(self):
        pass

    #            ・テーブルに置けるカードを探す
    def findCandidate(self, hand, table):
        candidate = None
        numberOfHand = hand.getNumberOfCard()
        for position in range(numberOfHand):
            lookingCard = hand.lookCard(position)
            number = lookingCard.getNumber()
            suit = lookingCard.getSuit()
            
            if number != 0:
                leftNumber = number - 1
            else:
                leftNumber = trump.Card.NUMBER_MAX-1
                
            if number != Card.NUMBER_MAX-1:
                rightNumber = number + 1
            else:
                rightNumber = 1
            
            # テーブル上に現在のカードの前後のカードがあれば、そのカードを取り出す
            if self.isThereCard_(table, suit, leftNumber) or \
               self.isThereCard_(table, suit, rightNumber):
                candidate = hand.pickCard(position)
                break
        
        return candidate
    
    def isThereCard_(self, table, suit, number):
        #print("suit=%d, number=%d" % (suit, number))
        cards = table.getCards()
        if cards[suit*Card.NUMBER_MAX+number] != None:
            return True
        return False
    
    
