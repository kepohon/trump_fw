'''
    rule.py
    
    ・ルールクラス（抽象クラス）
    
		属性
            ・プレイヤーの手札
			・テーブル
            
		操作
            ・テーブルに置けるカードを探す
    
    2023/10/03 by kepohon
'''

from .player import Player
from .hand import Hand
from .table import Table
from .card import Card

class Rule:
    
    def __init__(self):
        pass
        #self.hand = hand
        #self.table = table

    #def __str__(self):
    #    return "進行役（" + self.name + "）"
    
    #            ・テーブルに置けるカードを探す
    def findCandidate(self, hand, table):
        pass
