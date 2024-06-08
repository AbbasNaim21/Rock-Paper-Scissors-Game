import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")


computer_choice = random.randint(0,2)

if choice == "0":
    print(rock)
    if str(computer_choice) == "0":
        print("Computer Chose: \n")
        print(rock)
        print("It's a draw")
    elif str(computer_choice) =="1":
        print("Computer Chose: \n")
        print(paper)
        print("Computer wins")
    elif str(computer_choice) =="2":
        print("Computer Chose: \n")
        print(scissors)
        print("You win")

if choice == "1":
    print(paper)
    if str(computer_choice) =="0":
        print("Computer Chose: \n")
        print(rock)
        print("You win")
    elif str(computer_choice) =="1":
        print("Computer Chose: \n")
        print(paper)
        print("It's a draw")
    elif str(computer_choice) =="2":
        print("Computer Chose: \n")
        print(scissors)
        print("Computer Wins")

if choice == "2":
    print(scissors)
    if str(computer_choice) =="0":
        print("Computer Chose: \n")
        print(rock)
        print("Computer Wins")
    elif str(computer_choice) =="1":
        print("Computer Chose: \n")
        print(paper)
        print("You Win")
    elif str(computer_choice) =="2":
        print("Computer Chose: \n")
        print(scissors)
        print("It's a draw")
    
