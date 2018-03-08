def inputmove(player):
  print(player + " : What move will you choose?")
  move = input()
  move = checkinput(move,player)
  return move

def checkinput(move, player):
  if(move == "S" or move == "P" or move == "R"):
    return move
  else:
    print("Incorrect input! Try again! Please enter 'P' for paper, 'S' for scissors and 'R' for Rock")
    return inputmove(player)
    
def rps():
  p1 = inputmove("Player 1")
  p2 = inputmove("Player 2")
  if(p1 == p2):
   print("Both players did the same move!\n")
   return rps()
  else:
    if((p1 == "S" and p2 == "P") or
       (p1 == "P" and p2 == "R") or
       (p1 == "R" and p2 == "S")):
      print("Player 1 wins!\n")
    else:
      print("Player 2 wins!\n")

rps()