import random

patterns = [] ## sets the list
matches = 0 ## sets variable matches to 0
PatNum = 0 ## sets patnum to 0
i = None ## changes data withim variable i to none
j = None ## changes data withim variable j to none

def MaxMatches(patterns): ## this function finds the most frequent pattern
  position = 0
  Max = 0
  MaxM = 0
  TheList = [] ## list of checked patterns
  for i in range(3,-1,-1): ## decending order from 
    if not TheList:
      if patterns[i][1] > Max: ## max matches found
        MaxM = patterns[i][1] ## update matches
        position = i ## update position
        TheList.append(patterns[i]) ## append pattern to list of checked patterns
  return patterns[position][0], MaxM ## once all patterns have been checked

def MultiplePattern(data, NewMatch, UserPointer):
  counter = 0 ## counter 
  for i in NewMatch: ## loop desgined to find the next value within the pattern
    if i == UserPointer and NewMatch[len(NewMatch)-1] != UserPointer: ## as long as the loop has not reached the last value in pattern
      guess = NewMatch[counter+1] ## the predicted move will be the value before the last thrown move
      exit ## exit loop
    else:
      guess = NewMatch[0] ## if last thrown move is last in the pattern, next move is first in the pattern
      exit
    counter += 1
  return guess

def DoublePattern(data, NewMatch, UserPointer):
  guess = NewMatch[0] ## since values are reversed, last thrown move is second and next move is first
  return guess ## returns first value as prediction

def SinglePattern(data, UserPointer):
  guess = random.choice(data) ## weighted probability simulation
  return guess

def SearchMatching(data, NewMatch, PatNum):
  UserPointer = (data[(len(data))-1]) ## finds last thrown move
  if PatNum > 2: ## patterns of varying lengths follow different functions
    NextMove = MultiplePattern(data, NewMatch, UserPointer)
  elif PatNum  == 2:
    NextMove = DoublePattern(data, NewMatch, UserPointer)
  else:
    NextMove = SinglePattern(data, UserPointer)
  return NextMove
  
def NextChoice(patterns, data):
  Maximum = MaxMatches(patterns) ## receives pattern of highest frequency
  if patterns[0] == Maximum: ## finds the pattern matching with the highest frequency
    PatNum = 1 
    NewMatch = (patterns[0][0]) ## selects pattern instead of pattern and matches (tuple value)
    Move = SearchMatching(data, NewMatch, PatNum) ## move calculated
  elif patterns[1] == Maximum:
    PatNum = 2
    NewMatch = (patterns[1][0][::-1]) ## reverses the order of numbers in the pattern
    Move = SearchMatching(data, NewMatch, PatNum)
  elif patterns[2] == Maximum:
    PatNum = 3
    NewMatch = (patterns[2][0][::-1])
    Move = SearchMatching(data, NewMatch, PatNum)
  elif patterns[3] == Maximum:
    PatNum = 4
    NewMatch = (patterns[3][0][::-1])
    Move = SearchMatching(data, NewMatch, PatNum)
  return Move

def SelectingPointer(data,PatNum, i): ## function that selects pointer depending on pattern number
  if PatNum == 4:
    UsePointer = data[len(data)-1],data[len(data)-2],data[len(data)-3],data[len(data)-4]
  elif PatNum == 3:
    UsePointer = data[len(data)-1],data[len(data)-2],data[len(data)-3]
  elif PatNum == 2:
    UsePointer = data[len(data)-1],data[len(data)-2]
  elif PatNum == 1:
    UsePointer = data[len(data)-1] ## different scales so -1 needed to match scales accordingly
  if i == None:
    Comparison = None
  else:
    if PatNum == 4:
      Comparison = data[i],data[i-1],data[i-2],data[i-3] ## comparison pointer changes depending on loop number
    elif PatNum == 3:
      Comparison = data[i],data[i-1],data[i-2]
    elif PatNum == 2:
      Comparison = data[i],data[i-1]
    elif PatNum == 1:
      Comparison = data[i]
  return UsePointer,Comparison

def GetPatterns(data, matches, PatNum):
  pair = 0,0 ## defines pair as a tuple
  for i in range((len(data)-2),(PatNum)-2,-1): ## loops from decending order from max length of data to zero
    UsePointer = SelectingPointer(data, PatNum, i) ## userpointer corresponding to the correct pattern selected
    pair = UsePointer[0],matches ## pair redefined
    if UsePointer[0] == UsePointer[1]: ## if match found
      matches += 1 ## adds one to matches
      pair = UsePointer[0],matches ## pair updated
  patterns.append(pair) ## once loop finishes (all data searched), pair is appended to list of patterns
  matches = 0 ## matches reset to zero

def LearnChoice(PatNum, data): ## variables PatNum and data are passed on from previous function
  for PatNum in range(1,5): ## finds patterns of 1,2,3, and 4
    GetPatterns(data,matches,PatNum) ## function finds patterns 
  AIMove = NextChoice(patterns, data) ## function finds prediction from patterns found
  del patterns[:] ## deletes the list of patterns - this is done at the end of each round
  return AIMove

def WinningChoice(datalocal): ## the data is sent form the main module to machine learning module
  data = datalocal ## defines list of moves from the received data
  Move = LearnChoice(PatNum, data) ## LearnChoice triggers all the other functions
  if Move == 3: ## these are the predictions
    Choice = 1 ## beating the predictions
  elif Move == 1:
    Choice = 2
  elif Move == 2:
    Choice = 3
  return Choice ## returns the move to be played by the AI

