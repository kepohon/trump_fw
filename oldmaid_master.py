'''
    oldmaid_master.py
    
    ・進行役クラス
    
		属性
            ・プレイヤー配列
			・手札(山カード)
            ・名前
            
		操作
            ・コンストラクタ
                ・名前の初期化
                ・カードを受け取る
                ・テーブルの作成
                ・プレイヤー配列の準備
            ・ゲームの準備をする
                ・各プレイヤーにカードを配る
            ・プレイヤーを追加する
            ・プレイヤーと次のプレイヤーを指定する
            ・上がりを宣言する
            ・敗者を宣言する
    
    2023/11/13 by kepohon
'''

import trump
'''
from .player import Player
from .players import Players
from .hand import Hand
from .table import Table
from .card import Card
'''

class OldmaidMaster(trump.Master):
    PASS_LIMIT = 3
    
    def __init__(self, name, hand, table):
        super().__init__(name, hand, table)
    
    def pass_(self, player):
        print(" %s さんは %d 回目のパスしました！" % (player, player.getPass()) )
        if player.getPass() > self.PASS_LIMIT:
            print("  %sさんは負けです！" % (player))
            #deregisterPlayer(player)
            index = self.players_.searchPlayerIndex( player )
            #self.players_.deletePlayer(index)

