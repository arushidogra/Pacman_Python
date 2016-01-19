from game import *
from Person import *
from random import *
from Pacman import *
class Ghost(Person):
	def __init__(self):
		pass # :
	def updatevalue(self,a,b,c,d):	
		a=b
		c=d
		return c,d
	def ghostPosition(self,Board,ghostx,ghosty):

		i=randint(0,14)
		j=randint(0,34)
		q=self.checkWall(i,j,Board)
			
		if q==1:
			if Board[i][j]=='C':
				if Board[ghostx][ghosty]=='CG':
					Board[ghostx][ghosty]='C'
					ghostx=i
					ghosty=j
					'''
					print "haha"
					qwerty=Ghost()
					ghostx,ghosty=qwerty.updatevalue(ghostx,ghosty,i,j)
					'''
					# print hahah1"	
					Board[ghostx][ghosty]='CG'
				
				else:
					
					Board[ghostx][ghosty]='.'
					ghostx=i
					ghosty=j
					'''
					qwerty=Ghost()
					ghostx,ghosty=qwerty.updatevalue(ghostx,ghosty,i,j)
					'''
					Board[ghostx][ghosty]='CG'
			else:
				
				Board[ghostx][ghosty]='.'
				ghostx=i
				ghosty=j
				Board[ghostx][ghosty]='G'
		return Board,ghostx,ghosty

