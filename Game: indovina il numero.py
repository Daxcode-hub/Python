import random  # utilizzato per generare numeri casuali
player = int(input("What is the right number between 1 and 100? "))  # Viene chiesto all'utente di inserire un numero tra 1 e 100
winning_number = random.randint(1, 100)  # iene generato un numero casuale tra 1 e 100 che l'utente deve indovinare
player_attempts = 0 # contatore dei tentativi

while player != winning_number:  # Questo ciclo continua finché l'utente non indovina il numero vincente.
    player_attempts += 1
    if player < winning_number:
        print("The number is too small")  # suggerimento all'utente se il numero inserito è troppo piccolo.
    elif player > winning_number:
        print("The number is too big")  # suggerimento all'utente se il numero inserito è troppo grande
    player = int(input("What is the right number? "))
print(f"Well done, you guessed the hidden number which was {winning_number}! It took you {player_attempts} attempts to find it!")  

"""
Quando l'utente indovina il numero, viene stampato un messaggio di congratulazioni che include il numero vincente e il numero di tentativi necessari.
"""
