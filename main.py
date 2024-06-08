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

game_images = [rock, paper, scissors]

user_choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw")

# choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

# computer_choice = random.randint(0,2)

# if choice == "0":
#     print(rock)
#     if str(computer_choice) == "0":
#         print("Computer Chose: \n")
#         print(rock)
#         print("It's a draw")
#     elif str(computer_choice) =="1":
#         print("Computer Chose: \n")
#         print(paper)
#         print("Computer wins")
#     elif str(computer_choice) =="2":
#         print("Computer Chose: \n")
#         print(scissors)
#         print("You win")

# if choice == "1":
#     print(paper)
#     if str(computer_choice) =="0":
#         print("Computer Chose: \n")
#         print(rock)
#         print("You win")
#     elif str(computer_choice) =="1":
#         print("Computer Chose: \n")
#         print(paper)
#         print("It's a draw")
#     elif str(computer_choice) =="2":
#         print("Computer Chose: \n")
#         print(scissors)
#         print("Computer Wins")

# if choice == "2":
#     print(scissors)
#     if str(computer_choice) =="0":
#         print("Computer Chose: \n")
#         print(rock)
#         print("Computer Wins")
#     elif str(computer_choice) =="1":
#         print("Computer Chose: \n")
#         print(paper)
#         print("You Win")
#     elif str(computer_choice) =="2":
#         print("Computer Chose: \n")
#         print(scissors)
#         print("It's a draw")
