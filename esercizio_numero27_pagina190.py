'''
Organizza con un dizionario la rubrica con i nomi delle persone e i rispettivi numeri telefonici. Fornito poi il nome della persona,
il programma visualizza il suo numero di telefono oppure un messaggio nel caso la persona non sia presente nella rubrica.
'''
pagine_bianche = {"Mario":123,
                "Luigi":456,
                "Lorenzo":789,
                "Giovanni":987,
                "Giulio":654,
                "Enrico":321}
nome = input("Inserisci il nome della persona di cui cercare il numero di telefono nelle rubrica ")

if nome in pagine_bianche:
    print("Il numero di telefono del seguente dell'utente ", nome," è ", pagine_bianche[nome])
else:
    print("Il numero di telefono dell'utente richiesto non è presente nella rubrica")