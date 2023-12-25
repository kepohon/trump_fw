'''
    fantan_table.py
    
    ・テーブルクラス
    
		属性
			・手札(カード配列)
            
		操作
            ・捨てられたカードを手札に加える
            ・捨てられたカードを見る
    
    2023/11/15 by kepohon
    2023/11/12 by kepohon
'''

import trump
#from .card import Card

class FantanTable(trump.Table):
    def __init__(self):
        super().__init__()
    
    def putCard(self, card):
        super().putCard(card)
    
    def getCards(self):
        return self._table
    
