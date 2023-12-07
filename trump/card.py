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
    SUIT_MIN = 0
    SUIT_MAX = 4
    NUMBER_MIN = 0
    NUMBER_MAX = 13
    JOKER = 0
    ARRAY_SUIT = ["S","D","C","H"]
    ARRAY_NUMBER = ["A","2","3","4","5","6","7","8","9","T","J","Q","K"]
    
    number_ = 0
    suit_ = 0
    cardNameString_ = ""
    
    def __init__(self, suit, number):
        # スートとナンバーの範囲チェック
        self.suit_ = suit
        self.number_ = number
        self.createCardString_()
    
    # カード文字列を返す  呼び出し例 print( card )
    def __str__(self):
        return self.cardNameString_
    
    # カード文字列を作る
    def createCardString_(self):
        if (self.suit_ == 99) and (self.number_ == 99):
            self.cardNameString_ = "Jo"
        else:
            self.cardNameString_ = self.ARRAY_SUIT[self.suit_] + self.ARRAY_NUMBER[self.number_]
        return self.cardNameString_
    
    # カードの数字を見る
    def getNumber(self):
        return self.number_
    
    # カードのスートを見る
    def getSuit(self):
        return self.suit_





