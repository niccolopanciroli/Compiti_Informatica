'''
Un'azienda vende prodotti in tutta Italia e la rete di vendita è suddivisa in quattro zone: Nord, Centro, Sud, Isole.
Dopo aver acquistato in un array il fatturato nelle quattro zone, calcola:
- il totale del fatturato;
- i valori in percentuale delle vendite nelle quattro zone rispetto al totale.
'''
zone = ["nord", "centro", "sud", "isole"]
tot_fatturato = []

for z in range(len(zone)):
    fatturato = int(input("Inserisci il fatturato della zona " + zone[z] + " "))
    tot_fatturato.append(fatturato)
print("Il totale del fatturato dell'azienda è: ", sum(tot_fatturato))
for z in range(len(zone)):
    print("Il valore percentuale delle vendite rispetto al totale della zona", zone[z]," è: ", tot_fatturato[z]* 100/sum(tot_fatturato))