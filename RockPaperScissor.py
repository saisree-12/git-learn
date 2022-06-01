import random

print("		--- ROCK PAPER SCISSOR GAME ---		")
def f2():
	c = input("		  ENTER P TO PLAY AGAIN OR Q TO QUIT   ")
	if c=='P':
		f1()
	else:
		quit()
def f1():
	print("			ITS YOUR TURN   ")
	a = input("	ENTER -- R FOR ROCK -- P FOR PAPER -- S FOR SCISSOR ::  ")
	l = ['R','P','S']
	b = random.choice(l)
	if ((a=='P' and b=='R') or (a=='S' and b=='P') or (a=='R' and b=='S')):
		print("			  YOUR CHOICE IS : %c "%(a))
		print("	  		OPPONENT CHOICE IS : %c "%(b))
		print("			    ...YOU WON...    ")
		print("				   *			 ")
		print("				   *			 ")
		print("				   *			 ")
		f2()
	elif ((a=='R' and b=='P') or (a=='P' and b=='S') or (a=='S' and b=='R')):
		print("			  YOUR CHOICE IS : %c "%(a))
		print("	  		OPPONENT CHOICE IS : %c "%(b))
		print("			   ...OPPOENET WON...    ")
		print("				   *			 ")
		print("				   *			 ")
		print("				   *			 ")
		f2()
	elif ((a=='R' and b=='R') or (a=='P' and b=='P') or (a=='S' and b=='S')):
		print("			  YOUR CHOICE IS : %c "%(a))
		print("	  		OPPONENT CHOICE IS : %c "%(b))
		print("			   ...GAME TIE ...    ")
		print("				   *			 ")
		print("				   *			 ")
		print("				   *			 ")
		f2()
	else:
		print("			  YOUR CHOICE IS : %c "%(a))
		print("	  		OPPONENT CHOICE IS : %c "%(b))
		print("			 ...YOU LOST..TRY AGAIN...    ")
		print("				   *			 ")
		print("				   *			 ")
		print("				   *			 ")
		f2()
f1()