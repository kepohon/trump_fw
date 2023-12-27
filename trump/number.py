'''
    number.py
    
    ・カードナンバークラス
    
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
    
    2023/12/27    by kepohon
'''

class CardNumber:
    NUMBER_MIN = 1
    NUMBER_MAX = 13
    JOKER = 0
    ARRAY_NUMBER = ["o","A","2","3","4","5","6","7","8","9","T","J","Q","K"]
    
    _number = 0
    _cardNumberString = ""
    
    def __init__(self, number):
        # スートとナンバーの範囲チェック
        if (number < self.JOKER) or (self.NUMBER_MAX < number):
            print(f"カード番号エラー：：{number}")
            return
        self._number = number
        self._createCardNumberString()
    
    # カード文字列を返す  呼び出し例 print( card )
    def __str__(self):
        return self._cardNumberString
    
    # カード文字列を作る
    def _createCardNumberString(self):
        self._cardNumberString = self.ARRAY_NUMBER[self._number]
        return self._cardNumberString
    
    def _isJoker(self):
        return (self._number == 0)
    
    # カードの数字を見る
    def getNumber(self):
        return self._number
    
    def numberMax(self):
        return self.NUMBER_MAX
