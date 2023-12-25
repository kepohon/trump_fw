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
    
    2023/11/15 by kepohon
    2023/10/25 by kepohon
    2023/10/03 by kepohon
'''

class Card:
    SUIT_MIN = 1
    SUIT_MAX = 4
    NUMBER_MIN = 1
    NUMBER_MAX = 13
    JOKER = 0
    ARRAY_SUIT = ["J","S","D","C","H"]
    ARRAY_NUMBER = ["o","A","2","3","4","5","6","7","8","9","T","J","Q","K"]
    
    _number = 0
    _suit = 0
    _cardNameString = ""
    
    def __init__(self, suit, number):
        # スートとナンバーの範囲チェック
        self._suit = suit
        self._number = number
        self._createCardString()
    
    # カード文字列を返す  呼び出し例 print( card )
    def __str__(self):
        return self._cardNameString
    
    # カード文字列を作る
    def _createCardString(self):
        #if (self._suit == 0) and (self._number == 0):
        #    self._cardNameString = "Jo"
        #else:
        self._cardNameString = self.ARRAY_SUIT[self._suit] + self.ARRAY_NUMBER[self._number]
        return self._cardNameString
    
    def _isJoker(self):
        return (self._suit == 0) and (self._number == 0)
    
    # カードの数字を見る
    def getNumber(self):
        return self._number
    
    # カードのスートを見る
    def getSuit(self):
        return self._suit





