'''
I nomi delle città e i corrispondenti Codici di Avviamento Postali (CAP), vengono inseriti da tastiera e memorizzati in un dizionario,
dove il CAP è la chiave. Fornito poi il nome di una città, costruisci un messaggio che visualizzi il suo CAP oppure un messaggio nel caso la
città non sia compresa nell'elenco. Analagomente, fornendo il CAP restituisce il nome della città oppure un messaggio di errore.
'''
cap_città = {}
città_cap = {}

while True:
    print("Per ogni città dovrai inserire un CAP, se vuoi concludere la compilazione del dato scrivi STOP ")
    input()
    città = input("Inserisci il nome della città ")
    if città == "STOP":
        print("bella")
        break
    else:
        cap = input("Inserisci il cap della città ")
        cap_città[cap]= città
        città_cap[città] = cap
print("Il resoconto finale è ",cap_città)
print(città_cap)
risposta = input("Fai una scelta (DIGITA 1 o 2) \n1) Vuoi sapere il CAP, conoscendo la città \n2) Vuoi sapere la città, conoscendo il CAP \n")
if risposta == "1":
    nome_città = input("Inserisci il nome della città della quale vuoi sapere il CAP ")
    if nome_città in cap_città.values():
        print("Il CAP associato alla città ", nome_città, " è ", città_cap[nome_città])
    else:
        print("Non è presente alcun CAP associato alla città ", nome_città)
else:
    nome_cap = input("Inserisci il cap della città della quale vuoi sapere il nome ")
    if nome_cap in cap_città:
        print("La città associata al CAP ", nome_cap, " è ", cap_città[nome_cap])
    else:
        print("Non è presente nessuna città associata al CAP ", nome_cap)