# come perdere sempre al gioco

print("Giochiamo a carta, forbici, sasso?")
risposta = input()

# con risposta "si", viene eseguito questo codice:
if risposta == "si":
    print("Giochiamo!")
    print("Mi dici il tuo nome da giocatore?")
    nome = input() # giocatore inserisce il proprio nome
    print(nome + ", allora giochiamo")
    print("\nCosa scegli?")
    scelta_giocatore = ["carta", "forbici", "sasso"]
    for scelta in scelta_giocatore:
        print(scelta)
    print("Scegli 0 per carta, 1 per forbici o 2 per sasso")
    lettera_scelta = int(input()) # il giocatore inserisce la sua scelta
    scelta_2 = scelta_giocatore[lettera_scelta]
    print("Bene, hai scelto: " + scelta_2)

    scelta_giocatore_b = "" # il giocatore B sceglierà in base alla scelta del giocatore A e vincerà sempre
    if scelta_2 == "carta":
        scelta_giocatore_b = "forbici"
    elif scelta_2 == "forbici":
        scelta_giocatore_b = "sasso"
    elif scelta_2 == "sasso":
        scelta_giocatore_b = "carta"
    print("Anch'io ho fatto la mia scelta!")
    print("\nPremi invio per vedere chi ha vinto")
    input()
    print("Io ho scelto: " + scelta_giocatore_b)
    print(nome + ", hai perso!!!")

# con risposta "np" o altro, viene eseguita questa riga:
else:
    print("Ok, magari un'altra volta!")
