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

#Write your code below this line 👇
User_Choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if User_Choice == 0:
  print("You chose rock")
  print(rock)
elif User_Choice == 1:
  print("You chose paper")
  print(paper)
else:
  print("You chose scissors")
  print(scissors)

Computer_Choice = random.randint(0,2)
if Computer_Choice == 0:
  print("Computer chose rock")
  print(rock)
elif Computer_Choice == 1:
  print("Computer chose paper")
  print(paper)
else:
  print("Computer chose scissors")
  print(scissors)

if User_Choice == Computer_Choice:
  print("It's a tie!")
elif User_Choice == 0 and Computer_Choice == 2:
  print("You win!")
elif User_Choice == 1 and Computer_Choice == 0:
  print("You win!")
elif User_Choice == 2 and Computer_Choice == 1:
  print("You win!")
else:
  print("You lose!")
