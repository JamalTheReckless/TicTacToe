def chooseplayer():
  p1 = input("Which character will Player 1 use? (X/O):")
  if(p1=="X"):
    print("Player 1 is X and Player 2 is O")
    p2 = "O"
  elif(p1=="O"):
    print("Player 1 is O and Player 2 is X")
    p2 = "X"
  else:
    print("Incorrect input! Please enter 'X' or 'O'")
    return chooseplayer()
  return [p1,p2]

def printboard(board):
  i = 0
  j = 0
  print("    0   1   2  ")
  while(i<3):
    print("   --- --- --- ")
    print(i,end="")
    while(j<3):
      print(" | ",end="")
      print(board[i][j],end="")
      j+=1
    print(" |")
    j=0
    i+=1
  print("   --- --- --- ")
  return

def inputmove(board):
  move = [0,0]
  movestr = ""
  movestr = input("")
  if((movestr[0]=="[") and (movestr[2]==",") and (movestr[4]=="]") and
      isinstance(int(movestr[1]),int) and isinstance(int(movestr[3]),int) and
      (int(movestr[1])<3) and (int(movestr[3])<3) and (movestr[1] or movestr[3])!="-"):
    move[0]=int(movestr[1])
    move[1]=int(movestr[3])
  else:
    print("Incorrect input! Please enter in the form [x,y]")
    return inputmove(board)
  if(checkspot(board,move)==False):
    return inputmove(board)
  return move
  
def checkspot(board,move):
  if(board[move[0]][move[1]] != " "):
    print("There is already a character in that spot! Try again")
    return False
  else:
    return True
    
def checkforwin(Xs,Os,p):
  if((Xs==3 and p[0]=="X") or (Os==3 and p[0]=="O")):
    print("Player 1 wins!")
    return True
  if((Xs==3 and p[1]=="X") or (Os==3 and p[1]=="O")):
    print("Player 2 wins!")
    return True
  return False
    
def countforwin(board,p):
  Xs = 0
  Os = 0
  for i in range(0,3):
    for j in range(0,3):
      if(board[i][j]=="X"):
        Xs += 1
      if(board[i][j]=="O"):
        Os += 1
    if(checkforwin(Xs,Os,p)==True):
      return True
    Xs = Os = 0
  for i in range(0,3) :
    for j in range(0,3) :
      if(board[j][i]=="X"):
        Xs += 1
      if(board[j][i]=="O"):
        Os += 1
    if(checkforwin(Xs,Os,p)==True):
      return True
    Xs = Os = 0
  if(board[0][0]==board[1][1]==board[2][2]=="X"):
      Xs = 3
  elif(board[0][0]==board[1][1]==board[2][2]=="O"):
      Os = 3
  return checkforwin(Xs,Os,p)

def play(board,p):
  move = [0,0]
  print("it's Player 1's turn. What move do they play? ", end="")
  move = inputmove(board)
  board[move[0]][move[1]]=p[0]
  printboard(board)
  if(countforwin(board,p) == True):
    return
  print("it's Player 2's turn. What move do they play? ", end="")
  move = inputmove(board)
  board[move[0]][move[1]]=p[1]  
  printboard(board)
  if(countforwin(board,p) == True):
    return
  return play(board,p)

def tictactoe():
  newboard = [[" "," "," "],[" "," "," "],[" "," "," "]]
  printboard(newboard)
  p = chooseplayer()
  play(newboard,p)
  
tictactoe()
