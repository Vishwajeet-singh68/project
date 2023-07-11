def ConstBoard(board):
    print("Current State of the Board: \n\n")
    for i in range(9):
        if i>0 and i%3==0:
            print("\n")
        if(board[i]==0):
            print('_',end=' ')
        if(board[i]==-1):
            print('X',end=' ')
        if(board[i]==1):
            print('O',end=' ')
    print("\n\n")                    

def User1Turn(board):
    pos = int(input("Enter the O's position form [1,2,3,.....,4]:"))
    if(board[pos-1]!=0):
        print("Dude! this is wrong.")
        exit(0)
    board[pos-1]=1


def User2Turn(board):
    pos = int(input("Enter the X's position form [1,2,3,.....,4]:"))
    if(board[pos-1]!=0):
        print("Dude! this is wrong.")
        exit(0)
    board[pos-1]=-1


def analyseboard(board):
    cb=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in range(8):
        if(board[cb[i][0]]!=0 and cb[i][0]==cb[i][1] and cb[i][2]):
            return board[cb[i][0]]

    return 0


def minmax(board,player):
    x = analyseboard(board) 
    if(x!=0):
        return (x*player)
    pos=-1
    value = -2
    for i in range(9):
        if board[i]==0:
            board[i]=player
            score =  -minmax(board, player*-1)
            board[i] = 0
            if score>value:
                value = score
                pos=i
    if(pos==-1):
        return 0
    return value

        
def CompFunc(board):
    pos=-1
    value = -2
    for i in range(9):
        if board[i]==0:
            board[i]=1
            score =  -minmax(board,-1)
            board[i] = 0
            if score>value:
                value = score
                pos=i
    board[pos]=-1


def main():
    choice = int(input("Enter 1 for single player, 2 for multiplayer:"))
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    if(choice == 1):
        print("Computer: 0 Vs. You: X")
        player = int(input("Enter to play first(1) or second(2):"))
        for i in range(9):
            if(analyseboard(board)!=0):
                break
            if((i+player)%2==0):
                CompFunc(board)
            else:
                ConstBoard(board)
                User1Turn(board)
    else:
        for i in range(9):
            if(analyseboard(board)!=0):
                break
            if(i%2==0):
                CompFunc(board)
                User1Turn(board)
            else:
                ConstBoard(board)
                User2Turn(board)

    x = analyseboard(board)
    if x==0:
        ConstBoard(board)
        print("DRAW!")
    if x==-1:
        ConstBoard(board)
        print("player x wins!!! 0 looses")
    if x==1:
        ConstBoard(board)
        print("Player 0 wins!!! x looses")    


main()