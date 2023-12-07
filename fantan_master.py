'''
    master.py
    
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
    # パスを宣言する
    #   パス回数が制限を超えた場合
    #       プレイヤーの負けを表示する
    #       プレイヤーを検索し、ローテーションから削除する
    
    2023/11/15 by kepohon
    2023/10/03 by kepohon
'''

import trump

class FantanMaster(trump.Master):
    PASS_LIMIT = 3
    
    def __init__(self, name, hand, table):
        super().__init__(name, hand, table)
    
    # パスを宣言する
    #   パス回数が制限を超えた場合
    #       プレイヤーの負けを表示する
    #       プレイヤーを検索し、ローテーションから削除する
    def pass_(self, player):
        print(" %s さんは %d 回目のパスしました！" % (player, player.getPass()) )
        if player.getPass() > self.PASS_LIMIT:
            print("  %sさんは負けです！" % (player))
            index = self.players_.searchPlayerIndex( player )
            self.players_.deletePlayer(index)
    



