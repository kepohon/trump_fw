'''
    joker.py 
    
		属性
            ・プレイヤー配列
			・手札(山カード)
            ・名前
            
		操作
            ・数値をセットする
            ・模様をセットする
            ・カードの文字列を返す
        
    2023/11/10 by kepohon
'''

#import trump
from .card import Card

class Joker(Card):
    def __init__(self):
        super().__init__(99, 99)
    
    def setNumber(self, number):
        this._number = number
    
    def setSuit(self, suit):
        this._suit = suit



if __name__ == "__main__":
    pass
