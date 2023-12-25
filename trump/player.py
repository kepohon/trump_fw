'''
    player.py
    
    ・プレイヤークラス（抽象クラス）
    
		属性
            ・名前
			・手札(カード配列)
            
		操作
            ・配られたカードを手札に加える
            ・自分の回のプレイを行う（仮想関数）
            ここから下は継承したクラスで処理する
                ・手札に同じ数字のカードがあれば、テーブルへ捨てる
                ・次のプレイヤーからカードを引き、同じ数字のカードがあれば、テーブルへ捨てる
                ・手札カードが無くなれば、マスターに上がりを宣言する
    
    2023/11/15 by kepohon
    2023/10/03 by kepohon
'''

from .hand import Hand
from .table import Table

class Player:
    _name = ""
    _hand = None
    _master = None
    _table = None
    _rule = None
    
    def __init__(self, name, master, table, rule):
        self._name = name
        self._master = master
        self._table = table
        self._hand = Hand()
        self._rule = rule
    
    def __str__(self):
        return self._name
    
    #        ・配られたカードを手札に加える
    def recieveCard(self, card):
        self._hand.addCard(card)
    
    def play(self, nextPlayer):
        pass
    
    def showHand(self):
        return self._hand
    
    def printHand(self):
        print(self._hand)



