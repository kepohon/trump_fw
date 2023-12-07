'''
    oldmaid.py v1.1
    
		属性
            ・プレイヤー配列
			・手札(山カード)
            ・名前
            
		操作
            ・トランプの山札を準備する
            ・進行役を作り、山札を渡す
            ・プレイヤーを進行役に登録する
            ・進行役がゲームの準備をする
            ・進行役がゲームを開始する
        
    2023/10/11 by kepohon
    2023/10/10 by kepohon
    2023/10/04 by kepohon
'''

import trump

from oldmaid_rule import OldmaidRule
from oldmaid_master import OldmaidMaster
from oldmaid_table import OldmaidTable
from oldmaid_player import OldmaidPlayer


if __name__ == "__main__":
    #       ・トランプの山札を準備する
    #hand = trump.hand.Hand()
    #createTrump(hand)
    
    rule = OldmaidRule()
    table = OldmaidTable()
    
    #        ・進行役を作り、山札を渡す
    master = OldmaidMaster("斎藤", table, True)
    
    #        ・プレイヤーを進行役に登録する
    kebon = OldmaidPlayer("１ケボン", master, table, rule)
    pippi = OldmaidPlayer("２ピッピ", master, table, rule)
    yamada = OldmaidPlayer("３山田", master, table, rule)
    murata = OldmaidPlayer("４村田", master, table, rule)
    #donguri = trump.player.Player("５ドングリ", master, master.table)
    #ookita = trump.player.Player("６大北", master, master.table)
    
    #       ・プレイヤーの登録
    master.registerPlayer(kebon)
    master.registerPlayer(pippi)
    master.registerPlayer(yamada)
    master.registerPlayer(murata)
    #master.registerPlayer(donguri)
    #master.registerPlayer(ookita)
    
    #        ・進行役がゲームの準備をする
    master.prepareGame()   # ゲームを準備する
    
    #        ・進行役がゲームを開始する
    master.startGame()          # ゲームを開始する
