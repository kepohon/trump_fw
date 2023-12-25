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
    _handString = ""
    _hand = []
    
    def __init__(self):
        self._hand = []
    
    def __str__(self):
        return self._handString
    
    #        ・カードを手札に加える
    def addCard(self, card):
        self._hand.append(card)
        self.createHandString_()
    
    #       ・カードを見る
    def lookCard(self, position):
        lookingCard = None
        if (position >= 0) and (position < len(self._hand)):
            lookingCard = self._hand[position]
        return lookingCard
    
    #        ・手札からカードを引く
    def pickCard(self, index):
        card = self._hand.pop(index)
        self.createHandString_()
        return card
    
    #   手札の残りのカードを引く
    def pickRemainingCard(self):
        card = self._hand.pop(0)
        return card
    
    #        ・手札をシャッフルする
    def shuffle(self):
        numberOfCard = self.getNumberOfCard()
        for i in range(numberOfCard*2): #カード枚数の2倍シャッフルする
            card = self._hand.pop(random.randint(0, numberOfCard-1))
            self._hand.append(card)
        self.createHandString_()
    
    #        ・手札の枚数を数える
    def getNumberOfCard(self):
        return len(self._hand)
    
    #        ・手札にあるカードを文字列にする
    def createHandString_(self):
        self._handString = ""
        for card in self._hand:
            self._handString += str(card)
            self._handString += " "
        return self._handString
    
    #        ・同じ数のカードを探す
    def searchCard(self, card):
        searchNumber = card.getNumber()
        cardCount = len(self._hand)
        sameCard = None
        for index in range(cardCount):
            if searchNumber == self._hand[index].getNumber():
                sameCard = self._hand.pop(index)
                break
        return sameCard

