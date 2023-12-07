'''
    players.py
    
    ・プレイヤー配列を持つクラス（フレームワーク内で使われる）
    
		属性
            ・プレイヤー配列
            
		操作
            ・プレイヤーを登録する
            ・プレイヤーの人数を返す
            ・全プレイヤーの名前と手札を表示する
            ・現在のプレイヤーオブジェクトを返す
            ・次のプレイヤーオブジェクトを返す
            ・現在のプレイヤーを進める
            ・プレイヤーの添え字をリセットする
            ・指定されたプレイヤーの添え字を返す
            ・プレイヤーを削除する
            ・現在のプレイヤーがずれたか？
    
    2023/10/03 by kepohon
'''

from .player import Player
from .hand import Hand
from .table import Table
from .card import Card

class Players:
    def __init__(self):
        self.players = []
        self.currentIndex = 0
        self.numberOfPlayer = 0
        self.currentPlayerOBJ = None
        self.nextPlayerOBJ = None

    # プレイヤーを登録する
    def register(self, player):
        self.players.append(player)
        self.numberOfPlayer += 1
    
    # プレイヤーの人数を返す
    def numberOfPlayers(self):
        return self.numberOfPlayer  #len(self.players)
    
    # 全プレイヤーの名前と手札を表示する
    def displayHand(self):
        print("")
        for player in self.players:         #参加プレイヤーと手札を表示する
            print( "%s さん : %s" % (player, player.hand_) )
            #print( player , end='')
            #print( "さん:", end=' ')
            #print( player.hand_ )
        print("")
        print("")
    
    # 現在のプレイヤーオブジェクトを返す
    def currentPlayer(self):
        self.currentIndex = self.currentIndex % self.numberOfPlayers()
        self.currentPlayerOBJ = self.players[self.currentIndex]
        return self.currentPlayerOBJ
    
    # 次のプレイヤーオブジェクトを返す
    def nextPlayer(self):
        self.nextPlayerOBJ = self.players[(self.currentIndex + 1) % self.numberOfPlayers()]
        return self.nextPlayerOBJ
    
    # 現在のプレイヤーを進める
    def advancePlayer(self):
        self.currentIndex += 1
        if self.currentIndex >= self.numberOfPlayers():
            self.currentIndex = 0
    
    # プレイヤーの添え字をリセットする
    def resetPlayerIndex(self):
        self.currentIndex = 0
    
    # 指定されたプレイヤーの添え字を返す
    def searchPlayerIndex(self, player):
        return self.players.index( player )
    
    # プレイヤーを削除する
    def deletePlayer(self, index):
        self.players.pop(index)
        self.numberOfPlayer -= 1
    
    # 現在のプレイヤーがずれたか？
    def isChangeCurrentPlayer(self):
        if self.currentIndex >= len(self.players):  # 現在のプレイヤーがいなくなった場合
            return True
        if self.currentPlayerOBJ != self.players[self.currentIndex]:
            return True
        return False
