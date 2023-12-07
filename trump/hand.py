'''
    hand.py
    
    ・手札クラス
    
		属性
            ・カード文字配列
			・手札(カード配列)
            
		操作
            ・カードを手札に加える
            ・カードを見る
            ・手札からカードを引く
            #   手札の残りのカードを引く
            ・手札をシャッフルする
            ・手札の枚数を数える
            ・手札にあるカードを文字列にする
            
            ・カードを手札に加え、同じ数字のカードはテーブルへ捨てる
            ・同じ数のカードを探す
    
    2023/11/17 by kepohon
    2023/11/15 by kepohon
    2023/11/10 by kepohon
    2023/10/03 by kepohon
'''
import random
#from .card import Card

class Hand:
    handString_ = ""
    hand_ = []
    
    def __init__(self):
        self.hand_ = []
    
    def __str__(self):
        return self.handString_
    
    #        ・カードを手札に加える
    def addCard(self, card):
        self.hand_.append(card)
        self.createHandString_()
    
    #       ・カードを見る
    def lookCard(self, position):
        lookingCard = None
        if (position >= 0) and (position < len(self.hand_)):
            lookingCard = self.hand_[position]
        return lookingCard
    
    #        ・手札からカードを引く
    def pickCard(self, index):
        card = self.hand_.pop(index)
        self.createHandString_()
        return card
    
    #   手札の残りのカードを引く
    def pickRemainingCard(self):
        card = self.hand_.pop(0)
        return card
    
    #        ・手札をシャッフルする
    def shuffle(self):
        numberOfCard = self.getNumberOfCard()
        for i in range(numberOfCard*2): #カード枚数の2倍シャッフルする
            card = self.hand_.pop(random.randint(0, numberOfCard-1))
            self.hand_.append(card)
        self.createHandString_()
    
    #        ・手札の枚数を数える
    def getNumberOfCard(self):
        return len(self.hand_)
    
    #        ・手札にあるカードを文字列にする
    def createHandString_(self):
        self.handString_ = ""
        for card in self.hand_:
            self.handString_ += str(card)
            self.handString_ += " "
        return self.handString_
    
    #        ・同じ数のカードを探す
    def searchCard(self, card):
        searchNumber = card.getNumber()
        cardCount = len(self.hand_)
        sameCard = None
        for index in range(cardCount):
            if searchNumber == self.hand_[index].getNumber():
                sameCard = self.hand_.pop(index)
                break
        return sameCard

