from game import *
from Ghost import *
from Person import *
from random import *
from Pacman import *
from sys import *


def checkghost(a,b,c,d):
	if a==c and b==d:
		return 1
	else:
		return 0
def main():
	Board=[]
	p=[]
	flag=0
	for i in range(0,16):
		for j in range(0,36):
			p.append('.')
		Board.append(p)
		p=[]
	
	n=60


#MAKE WALLS#60
	while n:
	
		p=randint(0,15)
		q=randint(0,35)
		while Board[p][q] !='.' :
			p=randint(0,15)
			q=randint(0,35)
		Board[p][q]='X'
		n=n-1
				
#PUT COINS#40
	n=40
	while n:
		p=randint(0,14)
		q=randint(0,34)
		while Board[p][q]!='.' :
			p=randint(0,14)
			q=randint(0,34)
		Board[p][q]='C'
		n=n-1
		
# put Pacman

	p=randint(0,14)
	q=randint(0,34)
	while Board[p][q]!='.' :
		p=randint(0,14)
		q=randint(0,34)
	Board[p][q]='P'
	initialx=p
	initialy=q

	
#put ghost

	p=randint(0,14)
	q=randint(0,34)
	while Board[p][q]!='.':
		p=randint(0,14)
		q=randint(0,34)
	if Board[p][q]!='C':
		Board[p][q]='G'
	ghostx=p
	ghosty=q
	
	for i in range(0,15) :
		for j in range(0,35):
			print Board[i][j],
		print '\n'

	
	
	hello=Pacman()
	hey=Person()
	hola=Ghost()
	score=0
	while True:
		if score==40:
			Board=[]
			p=[]
			flag=0
			for i in range(0,16):
				for j in range(0,36):
					p.append('.')
				Board.append(p)
				p=[]
	
			n=60


		#MAKE WALLS#60
			while n:
	
				p=randint(0,15)
				q=randint(0,35)
				while Board[p][q] !='.' :
					p=randint(0,15)
					q=randint(0,35)
				Board[p][q]='X'
				n=n-1
					
												
		#PUT COINS#40
			n=40
			while n:
				p=randint(0,14)
				q=randint(0,34)
				while Board[p][q]!='.' :
					p=randint(0,14)
					q=randint(0,34)
				Board[p][q]='C'
				n=n-1
		
		# put Pacman

			p=randint(0,14)
			q=randint(0,34)
			while Board[p][q]!='.' :
				p=randint(0,14)
				q=randint(0,34)
			Board[p][q]='P'
			initialx=p
			initialy=q

	
		#put ghost

			p=randint(0,14)
			q=randint(0,34)
			while Board[p][q]!='.':
				p=randint(0,14)
				q=randint(0,34)
			if Board[p][q]!='C':
				Board[p][q]='G'
			ghostx=p
			ghosty=q
			for i in range(0,15) :
					for j in range(0,35):
						print Board[i][j],
					print '\n'
			continue
			print "YOU HAVE COLLECTED ALL COINS , BOARD RELOADED :) "			
		flag=0
		print "ENTER A MOVE",
     		move=raw_input() 
		if move=='q':
			exit(0)
		else:
#q=
		
			q=hello.checkmove(move,initialx,initialy,Board,flag,score)
			initialx=q[1]
			initialy=q[2]
			Board=q[3]
			flag=q[4]
			score=q[5]
			if q[0]==0:
				flag=0
				print "OOPS!!!!A WALL TRY AGAIN!!!"
				for i in range(0,15) :
					for j in range(0,35):
						print Board[i][j],
					print '\n'
				continue
			else:
				le=hola.ghostPosition(Board,ghostx,ghosty)
				Board=le[0]
				ghostx=le[1]
				ghosty=le[2]
				'''
				if ghostx==initialx and ghosty==initialy:
					print "a ghost :O"
					flag=0
				'''
				final=checkghost(initialx,initialy,ghostx,ghosty)
				if final==1:
					print "a ghost :O"
					flag=0
					exit(0)
				else:
					woah=hello.collectCoin(initialx,initialy,Board,flag,score)	
					Board=woah[0]
					flag=1
					score=woah[2]
				
			
		for i in range(0,15) :
			for j in range(0,35):
				print Board[i][j],
			print '\n'

		print "SCORE",score
		flag=0

