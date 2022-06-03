
import random

input("Welcome to Rock, Paper, Scissors! Press Enter to start.")
print()
user_wins = 0
computer_wins = 0

choices = [
    "R", "P", "S"]

while True:
  random_index = random.randint(0,2)
  cpu_choice = choices[random_index]

  user_choice = input("R, P, or S? ").lower()
  while user_choice not in choices:
    user_choice = input("That is not a valid choice. Please try again: ").lower()
  
  print()
  print("Your choice:", user_choice)
  print("Computer's choice:", cpu_choice)
  print()

  if user_choice == 'rock':
      
    if cpu_choice == 'R':
      print("It's a tie!")
    elif cpu_choice == 'S':
      print("You win!")
      user_wins+=1
    elif cpu_choice == 'P':
      print("You lose!")
      computer_wins+=1
  elif user_choice == 'P':
    if cpu_choice == 'P':
      print("It's a tie!")
    elif cpu_choice == 'R':
      print("You win!")
      user_wins+=1
    elif cpu_choice == 'S':
      print("You lose!")
      computer_wins+=1
  elif user_choice == 'S':
    if cpu_choice == 'S':
      print("It's a tie!")
    elif cpu_choice == 'P':
      print("You win!")
      user_wins+=1
    elif cpu_choice == 'R':
      print("You lose!")
      computer_wins+=1

  print()
  print("You have "+str(user_wins)+" wins")
  print("The computer has "+str(computer_wins)+" wins")
  print()

  repeat = input("Play again? (Y/N) ").lower()
  while repeat not in ['y', 'n']:
    repeat = input("That is not a valid choice. Please try again: ").lower()
  
  if repeat == 'n':
    break

  print("\n----------------------------\n")

