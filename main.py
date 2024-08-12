def ConstBoard(board):
  print("\n\nCurrent State Of Board : \n\n")
  for i in range(9):
    if(board[i] == 0):
      print("_ ", end="\t")#ends with a tab space
    if(board[i] == -1):
      print("X ", end="\t")
    if(board[i] == 1):
      print("O ", end="\t")
    if((i+1)%3 == 0):
      print("\n")

def User1Turn(board):#Multiplayer user 2
  while(True):
    pos = int(input("\nEnter X's pos where you want to place it from [1-9]: "))
    print("\n")
    if(board[pos-1] != 0):
      print("Wrong Move")
      print("Try Again below\n")
      continue
    board[pos-1] = -1
    break


def User2Turn(board):#Multiplayer user 2
  while(True):
    pos = int(input("\nEnter O's pos where you want to place it from [1-9]: "))
    print
    if(board[pos-1] != 0):
      print("Wrong Move")
      print("Try Again below\n")
      continue
    board[pos-1] = 1
    break

def UserTurn(board, sym):#When playing with Computer
  while(True):
    print("\nEnter ",sym,"'s pos where you want to place it from [1-9]: ")
    pos = int(input())
    if(board[pos-1] != 0):
      print("Wrong Move")
      print("Try Again below\n")
      continue
    if(sym == 'X'):
      board[pos-1] = -1
    else:
      board[pos-1] = 1
    break


def analyseboard(board):
  cb = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]#Champions board all triplets eligible for winning
  for i in range(8):
    if((board[cb[i][0]] != 0) and (board[cb[i][0]] == board[cb[i][1]]) and (board[cb[i][0]] == board[cb[i][2]])):#To check if triplet conatins same elements and not equal to zero
      return board[cb[i][0]]#Since here we already have stored X's and O's in the form of 1 and -1
  return 0

def minmax(board, player):
  x = analyseboard(board)
  if(x != 0):
    return (x*player)#if analyseboard gives won this means previous turn was winning turn so if now player is -1 and due to this 1 won return would be -1 which using minus in minmax becomes 1. Similarly if player is 1 and x =-1 won return = -1 and prev player=-1 so that return = 1 so in -1's turn -1 won becomes 1 and gets returned to 1's turn(original also) where - makes it -1
  else:#Recursion starts
    pos = -1#Just temporary position
    value = -2#Score cannot be less than -1 so -2 least value just like INT_MIN
    for i in range(9):
      if(board[i] == 0):#If empty
        board[i]= player#Player's turn computer assuming player is also playing optimally
        score = -minmax(board, player*(-1))#X(-1)'s turn after this #Why (-)? Real use of minus is because for 8 scores received by user playing it gets only those as 1 when it is winning similarly when computer wins from below recursions only those scores are one when it is winning
        board[i] = 0
        if(score > value):
          value = score
          pos = i
    if(pos == -1):
      return 0
    return value


def CompTurn(board, sym):
  pos = -1#Just temporary position
  #MaxAlgo starts
  if(sym == 'O'):
    value = -2#Score cannot be less than -1 so -2 least value just like INT_MIN
    for i in range(9):
      if(board[i] == 0):#If empty
        board[i]= 1#Computer's choice
        score = -minmax(board, -1)#X(-1)'s turn after this #Why (-)?: To inverse returned result which is opposite 
        board[i] = 0
        if(score > value):
          value = score
          pos = i
    board[pos] = 1
    #MinAlgo starts
  else:
    value = -2#Score cannot be greater than 1 so 2 greatest value just like INT_MAX while finding min element
    for i in range(9):
      if(board[i] == 0):#If empty
        board[i]= -1#Computer's choice
        score = -minmax(board, 1)#O(1)'s turn
        board[i] = 0
        if(score > value):
          value = score
          pos = i
    board[pos] = -1



def main():
  choice = int(input("Enter 1 for Single-Player game or 2 for Multi-Player Game: \n"))
  board = [0,0,0,0,0,0,0,0,0]#Initial Board
  if (choice == 1):
    symbol = input("\n\nWhat do you want to chose X or O: ")
    if(symbol == 'X'):
      compSymbol = 'O'
    else:
      compSymbol = 'X'
    print("\nComputer: ",compSymbol, " Vs. You: ",symbol,"\n");
    player = int(input("Enter 1 to play 1(st) or 2 to play 2(nd): "))
    for i in range(9):
      if(analyseboard(board) != 0):#Winner found with 1 or -1
        break
      if((i+player)%2 == 0):#Computer's chance because if we choose 1 then our turn is always indexed even but +player odd and similarly for 2 our indexed turn is odd which +2 remains odd
        CompTurn(board, compSymbol)
      else:
        ConstBoard(board)
        UserTurn(board, symbol)
    ConstBoard(board)
    if(analyseboard(board) == 0):
      print("\nDraw!")
    elif(analyseboard(board) == -1):
      if(symbol == 'X'):
        print("\nYou Won!")
      else:
        print("\nYou Lost :( !")
    else:
      if(symbol == 'X'):
        print("\nYou Lost :( !")
      else:
        print("\nYou Won!")
  elif(choice == 2):
    for i in range(9):
      if(analyseboard(board) != 0):#Winner found with 1 or -1
        break
      if(i%2 == 0):
          #Player 1's turn
          ConstBoard(board)
          User1Turn(board)
      else:
          #Player 2's turn
          ConstBoard(board)
          User2Turn(board)
    ConstBoard(board)
    if(analyseboard(board) == 0):
      print("\nDraw!")
    elif(analyseboard(board) == -1):
      print("\nPlayer 1 Won!")
    else:
      print("\nPlayer 2 Won!")

main()
