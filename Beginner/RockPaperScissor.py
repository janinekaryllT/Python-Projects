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

choose_rps = (int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n")))

if choose_rps >= 0 and choose_rps <= 2:
    if choose_rps == 0:
        print(rock)
    elif choose_rps == 1:
        print(paper)
    else:
        print(scissors)
    
    computer_choice = random.randint(0, 2)
    print("Computer chose:\n")
    if computer_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    else:
        print(scissors)

    print(computer_choice)

    if choose_rps == 0 and computer_choice == 1  or choose_rps == 1 and computer_choice == 2 or choose_rps == 2 and computer_choice == 0:
        print("You lose!")
    elif choose_rps == 0 and computer_choice == 2  or choose_rps == 1 and computer_choice == 0 or choose_rps == 2 and computer_choice == 1:
        print("You win!")
    else: 
        print("It's a draw!")
else:
    print("You typed invalid number!")
