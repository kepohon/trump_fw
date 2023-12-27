'''
    card.py
    
    ・カードクラス
    
		属性
            ・定数
                ・ジョーカー "J"
                ・スペード "S"
                ・ダイヤ "D"
                ・クラブ "C"
                ・ハート "H"
            ・スート(J,S,D,C,H)
            ・ナンバー(o,A,2,3,4,5,6,7,8,9,T,J,Q,K)
            
		操作
            ・カード文字列を返す
            ・カードの文字列を作る
            ・カードのスートを見る
            ・カードの数字を見る
    
    2023/12/27 by kepohon
    2023/11/15 by kepohon
    2023/10/25 by kepohon
    2023/10/03 by kepohon
'''

from .number import CardNumber
from .suit import CardSuit

class Card:
    _number = 0
    _suit = 0
    _cardNameString = ""
    
    def __init__(self, suit, number):
        # スートとナンバーの範囲チェック
        self._suit = CardSuit(suit)
        self._number = CardNumber(number)
        self._createCardString()
    
    # カード文字列を返す  呼び出し例 print( card )
    def __str__(self):
        return self._cardNameString
    
    # カード文字列を作る
    def _createCardString(self):
        #if (self._suit == 0) and (self._number == 0):
        #    self._cardNameString = "Jo"
        #else:
        #self._cardNameString = self.ARRAY_SUIT[self._suit.getSuit()] + #self.ARRAY_NUMBER[self._number.getNumber()]
        self._cardNameString = str(self._suit) + str(self._number)
        return self._cardNameString
    
    def _isJoker(self):
        return (self._suit.getSuit() == 0) and (self._number.getNumber() == 0)
    
    # カードの数字を見る
    def getNumber(self):
        return self._number.getNumber()
    
    # カードのスートを見る
    def getSuit(self):
        return self._suit.getSuit()
    
    def numberMax(self):
        return self._number.numberMax()
    
    def suitMax(self):
        return self._suit.suitMax()
    





