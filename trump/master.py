'''
    master.py
    
    ・進行役クラス（抽象クラス）
    
		属性
            ・プレイヤー配列
			・手札(山カード)
            ・名前
            
		操作
            ・コンストラクタ
                ・名前の初期化
                ・テーブルを受け取る
                ・Jokerの要・不要を受け取る
                ・プレイヤー配列の準備
            ・カードを準備する
            ・ゲームの準備をする
                ・各プレイヤーにカードを配る
            ・プレイヤーを追加する
            ・プレイヤーと次のプレイヤーを指定する
            ・上がりを宣言する
            ・敗者を宣言する
    
    2023/11/17 by kepohon
    2023/10/03 by kepohon
'''

from .player import Player
from .players import Players
from .hand import Hand
from .table import Table
from .card import Card
from .joker import Joker

class Master:
    def __init__(self, name, table, withJoker):
        self.name_ = name
        self._table = table
        self.withJoker_ = withJoker
        self.hand_ = Hand()
        self._players = Players()
    
    def __str__(self):
        return "進行役（" + self.name_ + "）"
    
    # プレイヤーを登録する
    def registerPlayer(self, player):
        self._players.register(player)
    
    #ゲームを準備する
    def prepareGame(self):
        self._createTrump()         # カードを準備する
        self._handOutCard()         # カードを配る
        
        print("テーブルのカード：")
        print( self._table )
        
        print( self )
        self._players.displayHand()      #参加プレイヤーと手札を表示する
        print("エンターキーを押してください")
        input()
    
    #カードを準備する
    def _createTrump(self):
        print("カードの準備")
        
        if self.withJoker_:         # Jokerが必要な場合
            card = Joker()
            self.hand_.addCard(card)
        
        for suit in range(4):
            for number in range(13):
                card = Card(suit+1, number+1)
                self.hand_.addCard(card)
        
        #作ったカードを表示する
        print( self.hand_ )
        
        print("カードをシャッフルする")
        self.hand_.shuffle()
        print( self.hand_ )
    
    # カードをプレイヤーに配る
    def _handOutCard(self):
        print("カードを配ります")
        cardCount = self.hand_.getNumberOfCard()
        playerCount = self._players.numberOfPlayers()
        print("カード枚数:%d" % cardCount)
        for i in range(cardCount):
            card = self.hand_.pickCard(0)
            self._players.currentPlayer().recieveCard(card)
            self._players.advancePlayer()
    
    # ゲームを開始する
    #   ・プレイヤーが1人の場合、何もしない
    #   ・プレイヤーの順番をリセットする
    #   ・プレイヤーを指名する
    #       ・現在のプレイヤーと次のプレイヤーの手札を表示する
    #       ・プレイヤーを指名する
    #       ・プレイヤーが1人になったら負けを宣言する
    def startGame(self):
        if self._players.numberOfPlayers() < 2:
            return
            
        self._players.resetPlayerIndex()
        playing = True
        index = 0
        
        while playing:
            print("==============================================")
            print("%sさんの番です" % (self._players.currentPlayer()))
            print("%sさんの手札: %s" % (self._players.currentPlayer(), self._players.currentPlayer()._hand) )
            print("%sさんの手札: %s" % (self._players.nextPlayer(), self._players.nextPlayer()._hand) )
            
            self._players.currentPlayer().play(self._players.nextPlayer())
            
            if self._players.numberOfPlayers() < 2:
                playing = False
                print( "%sさんの負けです" % (self._players.currentPlayer()) )
                print("%s: %s" % (self._players.currentPlayer(), self._players.currentPlayer()._hand))
                break
                
            if self._players.isChangeCurrentPlayer() == False:
                self._players.advancePlayer()
                
            self._players.displayHand()
            print("テーブルのカード：")
            print( self._table )
            print("")
        print("テーブルのカード：")
        print( self._table )
    
    def declareWin(self, winner):
        print( "%sさんが上がりました！！！！！！！！！！！！" % winner )
        index = self._players.searchPlayerIndex( winner )
        self._players.deletePlayer(index)



