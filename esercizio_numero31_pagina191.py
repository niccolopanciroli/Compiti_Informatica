zone = ["nord", "centro", "sud", "isole"]
tot_fatturato = []

for z in range(len(zone)):
    fatturato = int(input("Inserisci il fatturato della zona " + zone[z] + " "))
    tot_fatturato.append(fatturato)
print("Il totale del fatturato dell'azienda è: ", sum(tot_fatturato))
for z in range(len(zone)):
    print("Il valore percentuale delle vendite rispetto al totale della zona", zone[z]," è: ", tot_fatturato[z]* 100/sum(tot_fatturato))