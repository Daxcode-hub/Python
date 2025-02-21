# La to-do list è composta da quattro funzioni principali e un blocco di codice che avvia il programma. 

#funzione
def mostra_todo(todo_list):                          # Questa funzione prende una lista di task (todo_list) e stampa ciascun task con un indice numerico                 
    for idx, task in enumerate(todo_list, start=1):  # Ciclo for con enumerate per itera la lista dei task. enumerate restituisce sia l'indice che il valore,
                                                     # permettendo di stampare un indice numerico per ciascun task.
        print(f"{idx}. {task}")

def aggiungi_todo(todo_list, task):                  # aggiungere task
    todo_list.append(task)
    print(f"'{task}' è stato aggiunto alla lista.")

def rimuovi_todo(todo_list, task_idx):              # rimuovere task
    if 1 <= task_idx <= len(todo_list):
        removed_task = todo_list.pop(task_idx - 1)
        print(f"'{removed_task}' è stato rimosso dalla lista.")
    else:
        print("Indice non valido.")

def todo_list():   # funzione che gestisce il programma
    tasks = []  # lista vuota per memorizzare i task
    while True:  # in esecuzione fino a quando l'utente non sceglie di uscire.
        print("\nSeleziona un'azione:")
        print("1. Mostra lista")
        print("2. Aggiungi task")
        print("3. Rimuovi task")
        print("4. Esci")

        scelta = input("Inserisci il numero dell'azione (1/2/3/4): ")  # scelta utente
# opzioni in base alla scelta
        if scelta == '1':
            mostra_todo(tasks)
        elif scelta == '2':
            task = input("Inserisci il nuovo task: ")
            aggiungi_todo(tasks, task)
        elif scelta == '3':
            task_idx = int(input("Inserisci il numero del task da rimuovere: "))
            rimuovi_todo(tasks, task_idx)
        elif scelta == '4':
            print("Arrivederci!")
            break
        else:
            print("Azione non valida")

if __name__ == "__main__":  # Verifica se il file è stato eseguito direttamente (non importato come modulo) e, in tal caso, chiama todo_list() per avviare il programma.
    todo_list()
