'''
    fantan_player.py
    
    ・プレイヤークラス
    
		属性
            ・名前
			・手札(カード配列)
            
		操作
            ・配られたカードを手札に加える
            ・手札カードが無くなれば、マスターに上がりを宣言する
            # プレイ
            # ・手札を見て、テーブルに置けるカードを探し、
            #   置けるなら、テーブルに置く
            #       手札のカードがなくなったら、上がりを宣言する
            #   置けないなら、進行役にパスを宣言する
            #       ・パス回数がリミットを超えたら、手札をすべてテーブルに置く
            # パス回数を取得する
    
    2023/11/17 by kepohon
    2023/11/16 by kepohon
    2023/11/15 by kepohon
    2023/11/13 by kepohon
'''

import trump

from fantan_master import FantanMaster
from fantan_rule import FantanRule

class FantanPlayer(trump.Player):
    pass_ = 0
    
    def __init__(self, name, master, table, rule):
        super().__init__(name, master, table, rule)
    
    #        ・配られたカードを手札に加える
    #           ・7のカードであればテーブルへ置く
    #           ・それ以外は手札に加える
    def recieveCard(self, card):
        if card.getNumber() == 6:
            print("%s:%sを置きました。" % (self.name_, card) )
            self.table_.putCard(card)
            return
        super().recieveCard(card)
    
    # プレイ
    # ・手札を見て、テーブルに置けるカードを探し、
    #   置けるなら、テーブルに置く
    #       手札のカードがなくなったら、上がりを宣言する
    #   置けないなら、進行役にパスを宣言する
    #       ・パス回数がリミットを超えたら、手札をすべてテーブルに置く
    def play(self, nextPlayer):
        self.showHand()
        candidateCard = self.rule_.findCandidate(self.hand_, self.table_)
        if candidateCard != None:   #置ける場合
            print("  %sを置きました。\n" % (candidateCard))
            self.table_.putCard(candidateCard)
            #print(self.table_)
            if self.hand_.getNumberOfCard() == 0:
                self.master_.declareWin(self)
        else:   #置けない場合
            self.pass_ += 1
            self.master_.pass_(self)    # パスを宣言する
            if self.pass_ > FantanMaster.PASS_LIMIT:
                if self.hand_.getNumberOfCard() > 0:   # 手持ちのカードがあれば、すべてテーブルに置く
                    self.putAllCardsOnTheTable_(self.hand_, self.table_)
    
    # 手持ちのカードをすべてテーブルに置く
    def putAllCardsOnTheTable_(self, hand, table):
        for i in range(hand.getNumberOfCard()):
            card = hand.pickRemainingCard()
            table.putCard(card)
    
    # パス回数を取得する
    def getPass(self):
        return self.pass_


