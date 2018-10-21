## random number generating library
import random ## imports python's inbuilt random module
import aiaiai ## imports the AI module

          ##############################
          ## Rock Paper Scissors game ##
          ##############################
          ##  Artifical Intelligence  ##
          ##############################
  
moves = {1:'rock', 2:'paper', 3:'scissors'} ## dictionary to help convert numerals into moves

data = [] ## data defined as a list
Round = 1 ## round starts at 1
HumanScore = 0
ComputerScore = 0
DrawScore = 0

def Human(HUchoice): ## function to receieve and convert move into a numeral
  while True:
    if HUchoice.lower() == 'rock':
      Choice = 1
      return Choice
    elif HUchoice.lower() == 'paper':
      Choice = 2
      return Choice
    elif HUchoice.lower() == 'scissors':
      Choice = 3
      return Choice
    elif HUchoice == 'quit' or HUchoice == 'exit':
      return HUchoice
    else: ## error checking, loops the function to the beginning if either 'rock', 'paper' or 'scissors' is not inputted
      print ("Please enter a valid move")
      print('\n')
      HUchoice = input("Please enter rock, paper or scissors:")
      print('\n')

def Computer(Choice, Round, data): ## function to compare and produce a decisive ouput on winner
  if Round < 5:
    AIchoice = random.randint(1,3) ## generates computer's move randomly
  else:
    AIchoice = aiaiai.WinningChoice(data) ## this triggers the machine learning algorithm
  if Choice == 1  and AIchoice == 3: ## anonomlous comparison
    return ('Human', AIchoice)
  elif Choice == 3 and AIchoice == 1: ## anonomlous comparison
    return ('Computer', AIchoice)
  elif Choice > AIchoice:
    return ('Human', AIchoice)
  elif Choice < AIchoice: ## returns who won and the AI's move
    return ('Computer', AIchoice)
  elif Choice == AIchoice:
    return ('Draw', AIchoice)

## main program
print ("Welcome to the Rock Paper Scissors! If you would like to quit please enter 'quit'")
while True:
  HUchoice = input("Please enter 'rock', 'paper' or 'scissors':")
  print ("\n")
  if HUchoice == 'quit' or HUchoice == 'exit':
    print("Exiting program")
    break
  else:
    Choice = Human(HUchoice) ## function returned human choice and sets as variable outside function
    if Choice == 'quit' or Choice == 'exit':
      print("Exiting program")
      break
    CompOutput = Computer(Choice, Round, data) ## variables returned as tuples from fucntion Computer()
    data.append(Choice)
    print("Round:",Round)
    print ("You threw", moves[Choice]) ## using dictionary 'moves' to convert choice into appropriate move 
    print ("Computer threw", moves[CompOutput[1]]) ## Tuple in CompOutput has 2 variables, CompOutput[1] ouputs the second variable AIchoice
    if (CompOutput[0] == 'Human') or (CompOutput[0] == 'Computer'):
      print ("%s won" % (CompOutput[0]))
    else:
      print ("The outcome was a",CompOutput[0]) ## CompOutput[0] returns the first variable from the tuple
  if CompOutput[0] == 'Human': ## score system
    HumanScore += 1 ## adds 1 to the initial value
  elif CompOutput[0] == 'Computer':
    ComputerScore += 1
  else:
    DrawScore += 1
  print("Player Score: %s\nComputer Score: %s\nDraw: %s\n"  % (HumanScore, ComputerScore, DrawScore)) ## outputs the score
  Round += 1
