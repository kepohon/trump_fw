'''
    fantan.py v1.1
    
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
'''

import trump

from fantan_master import FantanMaster
from fantan_rule import FantanRule
from fantan_player import FantanPlayer
from fantan_table import FantanTable


if __name__ == "__main__":
    #       ・トランプの山札を準備する
    #hand = trump.hand.Hand()
    #createTrump(hand)
    
    table = FantanTable()
    
    #        ・進行役を作り、山札を渡す
    master = FantanMaster("斎藤", table, False)
    
    rule = FantanRule()
    
    #        ・プレイヤーを進行役に登録する
    kebon = FantanPlayer("１ケボン", master, table, rule)
    pippi = FantanPlayer("２ピッピ", master, table, rule)
    yamada = FantanPlayer("３山田", master, table, rule)
    murata = FantanPlayer("４村田", master, table, rule)
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
