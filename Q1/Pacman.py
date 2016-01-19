from game import *
from Person import *
from random import *
from Ghost import *	
class Pacman(Person):
	def __init__(self):
		pass
	def updatevalue(self,a,b,c,d):
		a=b
		c=d
		return c,d
	def checkmove(self,move,initialx,initialy,Board,flag,score):
		if move=='w' :
			if initialx==0:
				return 0,initialx,initialy ,Board,flag,score
			else:
				q=self.checkWall(initialx-1,initialy,Board)
				if q==0:
					return 0,initialx,initialy,Board,flag,score
				else:
					Board[initialx][initialy]='.'
					initialx=initialx-1
					if Board[initialx][initialy]!='C' and Board[initialx][initialy]!='CG':
						Board[initialx][initialy]='P'
						flag=0
						return 1,initialx,initialy,Board,flag,score
					else:	
						flag=1
						return 1,initialx,initialy,Board,flag,score
		if move=='a':			
			if initialy==0:
				return 0,initialx,initialy,Board,flag,score
			else: 
				q=self.checkWall(initialx,initialy-1,Board)
				if q==0:
					return 0,initialx,initialy,Board,flag,score
				else:
					Board[initialx][initialy]='.'
					initialy=initialy-1
			
					if Board[initialx][initialy]!='C' and  Board[initialx][initialy]!='CG':
						flag=0
						Board[initialx][initialy]='P'
						return 1,initialx,initialy,Board,flag,score
					else:	
						flag=1
						return 1,initialx,initialy,Board,flag,score


		if move=='s':
			if initialx==14:
				return 0,initialx,initialy,Board,flag,score
			else:
				q=self.checkWall(initialx+1,initialy,Board)
				if q==0:
					return 0,initialx,initialy,Board,flag,score
				else:
					Board[initialx][initialy]='.'
						flag=0
						Board[initialx][initialy]='P'
						return 1,initialx,initialy,Board,flag,score
					else:
						flag=1
						return 1,initialx,initialy,Board,flag,score
		if move=='d':
			if initialy==34:
				return 0,initialx,initialy,Board,flag,score
			else:
				q=self.checkWall(initialx,initialy+1,Board)
				if q==0:
					return 0,initialx,initialy,Board,flag,score
				else:
					Board[initialx][initialy]='.'
					initialy=initialy+1	
					if Board[initialx][initialy]!='C' and Board[initialx][initialy]!='CG':
						Board[initialx][initialy]='P'
						flag=0
						return 1,initialx,initialy,Board,flag,score
					else:
						flag=1
						return 1,initialx,initialy,Board,flag,score
				
	def collectCoin(self,initialx,initialy,Board,flag,score):

		if Board[initialx][initialy]=='C':
			if flag==1:
				flag=0
				score=score+1
				Board[initialx][initialy]='P'
		return Board,flag,score
