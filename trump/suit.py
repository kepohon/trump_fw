'''
    suit.py
    
    ・カードスートクラス
    
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
'''

class CardSuit:
    JOKER = 0
    SUIT_MIN = 1
    SUIT_MAX = 4
    ARRAY_SUIT = ["J","S","D","C","H"]
    
    _suit = 0
    _cardSuitString = ""
    
    def __init__(self, suit):
        # スートの範囲チェック
        if (suit < self.JOKER) or (self.SUIT_MAX < suit):
            print(f"スート番号エラー：：{suit}")
            return
        self._suit = suit
        self._createSuitString()
    
    # スート文字列を返す  呼び出し例 print( card )
    def __str__(self):
        return self._cardSuitString
    
    # スート文字列を作る
    def _createSuitString(self):
        self._cardSuitString = self.ARRAY_SUIT[self._suit]
        return self._cardSuitString
    
    def _isJoker(self):
        return (self._suit == 0)
    
    # カードのスートを見る
    def getSuit(self):
        return self._suit
    
    def suitMax(self):
        return self.SUIT_MAX
