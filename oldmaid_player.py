'''
    oldmaid_player.py
    
    ・プレイヤークラス
    
		属性
            ・名前
			・手札(カード配列)
            
		操作
            ・配られたカードを手札に加える
            ・手札に同じ数字のカードがあれば、テーブルへ捨てる
            ・次のプレイヤーからカードを引き、同じ数字のカードがあれば、テーブルへ捨てる
            ・手札カードが無くなれば、マスターに上がりを宣言する
    
    2023/11/17 by kepohon
    2023/11/13 by kepohon
'''

import random
from random import randint, randrange, random, uniform
import trump

from oldmaid_master import OldmaidMaster
from oldmaid_rule import OldmaidRule


class OldmaidPlayer(trump.Player):
    pass_ = 0
    
    def __init__(self, name, master, table, rule):
        super().__init__(name, master, table, rule)
    
    # ・配られたカードを手札に加える
    #   手札に加えるカードの数字と同じ数のカードが手札にあれば捨てる
    def recieveCard(self, card):
        
        if self.hand_.getNumberOfCard() >= 1:
            number = card.getNumber()
            cardCount = self.hand_.getNumberOfCard()
            for index in range(cardCount):
                if number == self.hand_.lookCard(index).getNumber():
                    sameCard = self.hand_.pickCard(index)
                    print("%s %sを捨てました" % (card, sameCard) )
                    self.table_.putCard(card)
                    self.table_.putCard(sameCard)
                    return
        
        super().recieveCard(card)
    
    # プレイ
    #   次のプレイヤーの手札からカードを引く
    #   次のプレイヤーの手札が無くなったら、次のプレイヤーが上がりを宣言する
    #   引いたカードを手札に加える。同じ数字のカードがあれば、テーブルへ捨てる。
    def play(self, nextPlayer):
        index = randrange(nextPlayer.hand_.getNumberOfCard())
        pickCard = nextPlayer.hand_.pickCard(index)
        print("%sさんから%sを引きました" % (nextPlayer, pickCard) )
        if nextPlayer.hand_.getNumberOfCard() == 0:
            self.master_.declareWin(nextPlayer)
        #self.recieveCard(pickCard)
        super().recieveCard(pickCard)
        cards = self.rule_.findCandidate(self.hand_, self.table_)
        if cards != None:
            self.table_.putCard(cards[0])
            self.table_.putCard(cards[1])
            print("%s %sを捨てました" % (cards[0], cards[1]) )
        if self.hand_.getNumberOfCard() == 0:
            self.master_.declareWin(self)
    
    def getPass(self):
        return self.pass_


