import random

print("*****************************************************")
print("Welcome to Janken")
print("rock beats scissors")
print("paper beats rock")
print("scissors beats paper")
print("sames draw")
print("*****************************************************")


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

possible_choices = [rock, paper, scissors]

# receive choice from user
input_choice = int(input("choose: rock(0), paper(1) or scissors(2)? "))
user_choice = possible_choices[input_choice]

# generate random choice for bot
computer_choice = random.choice(possible_choices)

if user_choice == computer_choice:
    print("You chose:")
    print(user_choice)
    print("\ncomputer chose:")
    print(computer_choice)
    print("It is a Draw")

elif user_choice == possible_choices[0] and computer_choice == possible_choices[2]:
    print("You chose:")
    print(user_choice)
    print("\ncomputer chose:")
    print(computer_choice)
    print("you win")

elif user_choice == possible_choices[0] and computer_choice == possible_choices[1]:
    print("You chose:")
    print(user_choice)
    print("\ncomputer chose:")
    print(computer_choice)
    print("you lose")

elif user_choice == possible_choices[1] and computer_choice == possible_choices[0]:
    print("You chose:")
    print(user_choice)
    print("\ncomputer chose:")
    print(computer_choice)
    print("you win")

elif user_choice == possible_choices[1] and computer_choice == possible_choices[2]:
    print("You chose:")
    print(user_choice)
    print("\ncomputer chose:")
    print(computer_choice)
    print("you lose")

elif user_choice == possible_choices[2] and computer_choice == possible_choices[0]:
    print("You chose:")
    print(user_choice)
    print("\ncomputer chose:")
    print(computer_choice)
    print("you lose")

elif user_choice == possible_choices[2] and computer_choice == possible_choices[1]:
    print("You chose:")
    print(user_choice)
    print("\ncomputer chose:")
    print(computer_choice)
    print("you win")
