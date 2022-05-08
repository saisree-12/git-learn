#  TIC TAC TOE

def hii(i,s1,s2):
    if(i%2==0):
        print("PLAYER 1 HAS TO PLAY")
        print("1 | 2 | 3 ")
        print("4 | 5 | 6 ")
        print("7 | 8 | 9 ")
        ia = int(input("enter the number in which u want to insert :: "))
        return ia,s1
    else:
        print("PLAYER 2 HAS TO PLAY")
        print("1 | 2 | 3 ")
        print("4 | 5 | 6 ")
        print("7 | 8 | 9 ")
        ia = int(input("enter the number in which u want to insert :: "))
        return ia,s2
def helo():
    a = ['-','-','-','-','-','-','-','-','-']
    i=0
    s1 = str(input("enter the character of a first player :: "))
    s2 = str(input("enter the character of a second player :: "))
    def restrt():
            print("IF WANTS TO CONTINUE ENTER C ELSE ENTER Q TO QUIT")
            ab=input()
            if ab=='C':
                helo()
            elif ab=='Q':
                exit()
    while True:
        inte,c=hii(i,s1,s2)
        if(inte==1):
            a[0] = c
        elif(inte==2):
            a[1] = c
        elif(inte==3):
            a[2] = c
        elif(inte==4):
            a[3] = c
        elif(inte==5):
            a[4] = c
        elif(inte==6):
            a[5] = c
        elif(inte==7):
            a[6] = c
        elif(inte==8):
            a[7] = c
        elif(inte==9):
            a[8] = c
        i+=1    
        print(a[0],"|",a[1],"|",a[2])
        print(a[3],"|",a[4],"|",a[5])
        print(a[6],"|",a[7],"|",a[8])
        if inte==1:
            if((a[0]==a[1] and a[1]==a[2]) or (a[0]==a[3] and a[3]==a[6]) or (a[0]==a[4] and a[4]==a[8])):
                if i%2==1:
                    print("PLAYER 1 WINS ")
                    restrt()
                else :
                    print("PLAYER 2 WINS ")
                    restrt()
        elif inte==2:
            if((a[1]==a[4] and a[4]==a[7]) or (a[1]==a[0] and a[0]==a[2])):
                if i%2==1:
                    print("PLAYER 1 WINS ")
                    restrt()
                else :
                    print("PLAYER 2 WINS ")
                    restrt()
        elif inte==3:
            if((a[2]==a[5] and a[5]==a[8]) or (a[2]==a[1] and a[1]==a[0]) or (a[2]==a[4] and a[4]==a[6])):
                if i%2==1 :
                    print("PLAYER 1 WINS ")
                    restrt()
                else :
                    print("PLAYER 2 WINS ")
                    restrt()
        elif inte==4:
            if((a[3]==a[4] and a[4]==a[5]) or (a[3]==a[0] and a[0]==a[6])):
                if i%2==1 :
                    print("PLAYER 1 WINS ")
                    restrt()
                else :
                    print("PLAYER 2 WINS ")
                    de()
        elif inte==5:
            if((a[4]==a[1] and a[1]==a[7]) or (a[4]==a[3] and a[3]==a[5]) or (a[4]==a[0] and a[0]==a[8]) or (a[4]==a[2] and a[2]==a[6])):
                if i%2==1 :
                    print("PLAYER 1 WINS ")
                    restrt()
                else:
                    print("PLAYER 2 WINS ")
                    restrt()
        elif inte==6:
            if((a[5]==a[2] and a[2]==a[8]) or (a[5]==a[4] and a[4]==a[3])):
                if i%2==1:
                    print("PLAYER 1 WINS ")
                    restrt()
                else :
                    print("PLAYER 2 WINS ")
                    restrt()
        elif inte==7:
            if((a[6]==a[3] and a[3]==a[0]) or (a[6]==a[7] and a[7]==a[8]) or (a[6]==a[4] and a[4]==a[2])):
                if i%2==1 :
                    print("PLAYER 1 WINS ")
                    restrt()
                else :
                    print("PLAYER 2 WINS ")
                    restrt()
        elif inte==8:
            if((a[7]==a[4] and a[4]==a[1]) or (a[7]==a[6] and a[6]==a[8])):
                if i%2==1 :
                    print("PLAYER 1 WINS ")
                    restrt()
                else :
                    print("PLAYER 2 WINS ")
                    restrt()
        elif inte==9:
            if((a[8]==a[5] and a[5]==a[2]) or (a[8]==a[7] and a[7]==a[6]) or (a[8]==a[4] and a[4]==a[0])):
                if i%2==1 :
                    print("PLAYER 1 WINS ")
                    restrt()
                else :
                    print("PLAYER 2 WINS ")
                    restrt()
        if i==9:
            print("NO ONE WINS")
            print()
            restrt()
helo()