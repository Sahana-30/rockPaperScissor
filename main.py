import random 
print("Welcome to Rock Paper Scissor!")
while True: 
  userChoice =input("Enter a choice(rock, paper, scissor)")
  actions = ['rock','paper','scissor']
  computerChoice =random.choice (actions)
  print("You chose "+userChoice+", Computer chose "+computerChoice)
  #Determine a winner 
  if userChoice == computerChoice: 
    print("It's a tie!")
  elif userChoice == 'rock': 
    if computerChoice == 'scissor': 
      print("You win!")
    else: 
      print("You lose")
  elif userChoice == "paper":
      if computerChoice == "rock":
          print("Paper covers rock! You win!")
      else:
          print("Scissors cuts paper! You lose.")
  elif userChoice == "scissor":
      if computerChoice == "paper":
          print("Scissors cuts paper! You win!")
      else:
          print("Rock smashes scissor! You lose.")


  playAgain = input("Play again? (y/n): ")
  if playAgain.lower() != "y":
    break