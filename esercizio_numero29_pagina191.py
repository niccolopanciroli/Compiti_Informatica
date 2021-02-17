
reddito = int(input("Inserisci il tuo reddito per conoscere l'importo della imposta sul reddito e la tassazione media "))

if reddito <= 15000:
    imposta = 0.23 * reddito
    tassazione_media = imposta/reddito * 100
    print("L'importo dell'imposta sul reddito è ",imposta, " € ")
    print("La tassazione media è ", tassazione_media, " %")

elif 15000 < reddito <= 28000:
    imposta = 0.23*15000+0.27*(reddito-15000)
    tassazione_media = imposta/reddito * 100
    print("L'importo dell'imposta sul reddito è ",imposta, " € ")
    print("La tassazione media è ", tassazione_media, " %")

elif 28000 < reddito <= 55000:
    imposta = 0.23*15000 + 0.27*13000 + 0.38*(reddito-28000)
    tassazione_media = imposta/reddito * 100
    print("L'importo dell'imposta sul reddito è ",imposta, " € ")
    print("La tassazione media è ", tassazione_media, " %")

elif 55000 < reddito <= 75000:
    imposta = 0.23 * 15000 + 0.27 * 13000 + 0.38 * 27000 + 0.41 *(reddito - 55000)
    tassazione_media = imposta/reddito *100
    print("L'importo dell'imposta sul reddito è ",imposta, " € ")
    print("La tassazione media è ", tassazione_media, " %")

else:
    imposta = 0.23 * 15000 + 0.27 * 13000 + 0.38 * 27000 + 0.41 * 20000 + 0.43*(reddito-75000)
    tassazione_media = imposta/reddito *100
    print("L'importo dell'imposta sul reddito è ",imposta, " € ")
    print("La tassazione media è ", tassazione_media, " %")
