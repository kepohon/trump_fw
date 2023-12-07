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
    name_ = ""
    hand_ = None
    master_ = None
    table_ = None
    rule_ = None
    
    def __init__(self, name, master, table, rule):
        self.name_ = name
        self.master_ = master
        self.table_ = table
        self.hand_ = Hand()
        self.rule_ = rule
    
    def __str__(self):
        return self.name_
    
    #        ・配られたカードを手札に加える
    def recieveCard(self, card):
        self.hand_.addCard(card)
    
    def play(self, nextPlayer):
        pass
    
    def showHand(self):
        return self.hand_
    
    def printHand(self):
        print(self.hand_)



