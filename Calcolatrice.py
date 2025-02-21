# permette di effettuare calcoli e ricominciare con opzione di uscita

def addizione(x, y):
    return x + y    # addizione

def sottrazione(x, y):
    return x - y    # sottrazione

def moltiplicazione(x, y):
    return x * y   # moltiplicazione

def divisione(x, y):
    if y != 0:    # controlla se il valore di y è diverso da zero per poter effettuare la divisione
        return x / y
    else:
        return "Errore: divisione per zero" # se viene inserito 0 si riceve questa risposta

def calcolatrice():  # vengono offerte delle opzioni all'utente
    while True:
        print("Seleziona l'operazione:")
        print("1. Addizione")
        print("2. Sottrazione")
        print("3. Moltiplicazione")
        print("4. Divisione")
        print("5. Esci")

        scelta = input("Inserisci il numero dell'operazione (1/2/3/4/5): ") # si chiede una scelta

        if scelta == '5':  # nel caso l'utente volesse uscire
            print("Grazie per aver usato la calcolatrice! Arrivederci!")
            break

        num1 = float(input("Inserisci il primo numero: "))  # richiesta all'utente
        num2 = float(input("Inserisci il secondo numero: "))  # richiesta all'utente
      
# in base alla scelta effettuata si ricevono questi output:
        if scelta == '1':
            print(f"Il risultato è: {addizione(num1, num2)}")
        elif scelta == '2':
            print(f"Il risultato è: {sottrazione(num1, num2)}")
        elif scelta == '3':
            print(f"Il risultato è: {moltiplicazione(num1, num2)}")
        elif scelta == '4':
            print(f"Il risultato è: {divisione(num1, num2)}")
        else:
            print("Operazione non valida")

if __name__ == "__main__":  # assicura che la funzione --->calcolatrice() venga eseguita solo se viene eseguito direttamente e non importato come modulo.
    calcolatrice()
