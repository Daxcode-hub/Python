import random
player = int(input("What is the right number between 1 and 100? "))
winning_number = random.randint(1, 100)
player_attempts = 0

while player != winning_number:
    player_attempts += 1
    if player < winning_number:
        print("The number is too small")
    elif player > winning_number:
        print("The number is too big")
    player = int(input("What is the right number? "))
print(f"Well done, you guessed the hidden number which was {winning_number}! It took you {player_attempts} attempts to find it!")
