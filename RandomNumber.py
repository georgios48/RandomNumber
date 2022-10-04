import random

computer_number = random.randint(1, 101)

user_number = int(input("Guess the number: "))

while user_number != computer_number:
    if computer_number > user_number:
        print("the number is higher than yours.. ")
    elif computer_number < user_number:
        print("the number is lower than yours.. ")
    user_number = int(input("Guess the number: "))

print(f"Congratz, you guessed right!")
print(f"The number is: {computer_number}")