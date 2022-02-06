# Required modules
import numpy as np
import random

last_1 = 0 # Last input
last_2 = 0 # Second to last input
inputs = np.zeros(shape=(2, 2, 2), dtype=int)
# 3-D array to keep track of player data

def update_inputs(current):
  global last_2, last_1, inputs
  if inputs[last_2][last_1][0] == current: # If it was played last time
    inputs[last_2][last_1][1] = 1 # Say it is repeating
    inputs[last_2][last_1][0] = current # Set to current
  else:
    inputs[last_2][last_1][1] = 0 # Otherwise, it has not repeated
    inputs[last_2][last_1][0] = current
 
  last_2 = last_1 
  last_1 = current 

def prediction():
  global inputs # Get 3-D array
  if inputs[last_2][last_1][1] == 1: # If the input has been repeated before
    predict = inputs[last_2][last_1][0] # Guess that number
  else:
    predict = random.randint(0, 1) # Guess random number
  return predict

scores = [0,0] #[computer, human]

def update_score(predicted, player_input):
  global scores # Get scores
  if predicted == player_input: 
    scores[0] += 1
  else:
    scores[1] += 1
  print("Computer Score",scores[0],"Player Score",scores[1])

def reset():
  global inputs
  # Reset 3-D array to 0
  for block in range(2):
    for row in range(2):
      for ind in range(2):
        inputs[block][row][ind] = 0

def gameplay():
  reset()
  valid = [0,1] # Valid entries

  while True:
    predicted = prediction()
    playerInput = int(input("Enter a number, 0 or 1 "))
    while(playerInput not in valid):
      playerInput = int(input("Enter a number, 0 or 1 "))
    
    update_inputs(playerInput)
    update_score(predicted, playerInput)

    if scores[0] == 20:
      print("Computer wins!")
      break
    elif scores[1] == 20:
      print("Player wins!")
      break

gameplay()