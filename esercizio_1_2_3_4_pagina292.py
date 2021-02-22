#Crea una classe "Atleta" per rappresentare le informazioni su un giocatore.
#La classe deve anche contenere un attributo booleano chiamato "Visita Medica".
#Aggiungi alla classe "Atleta" un metodo per assegnare all'atleta il nome della squadra dove gioca.
#Aggiungi alla classe "Atleta" un metodo chiamato "effettua_visita" che ponga l'attributo "visitaMedica" uguale a True.
#Aggiungi alla classe "Atleta" un metodo per visualizzare i dati del giocatore

class Atleta:
    def __init__(self, name, surname, age, weight, height): #variabili come argomenti della funzione
        self.name = name # definizione dell'argomento specifico della classe
        self.surname = surname
        self.age = age
        self.weight = weight
        self.height = height
        self.visitaMedica = False
    def dati(self):
        print("L'atleta, ", self.name, self.surname, " di età ", self.age, ", pesa ", self.weight,"kg, ed è alto ", self.height, " cm")
        if self.visitaMedica == False:
            print("L'atleta ", self.name, self.surname, " non si è sottoposto alla visita medica ")
        else:
            print("L'atleta ", self.name, self.surname, " si è sottoposto alla visita medica")
    def effettua_visita(self):
        self.visitaMedica = True
    def squadra(self, team):
        self.team = team
        print("L'atleta gioca nella squadra ", self.team)

def main():
    name = input("Inserisci il nome dell'atleta ")
    surname = input("Inserisci il cognome dell'atleta ")
    age = input("Inserisci l'età dell'atleta ")
    weight = int(input("Inserisci il peso dell'atleta "))
    height = int(input("Inserisci l'altezza dell'atleta "))
    team = input("Inserisci la squadra in cui gioca l'atleta ")
    atleta = Atleta(name, surname, age, weight, height)
    visita = str(input("L'atleta si è sottoposto alla visita medica? "))
    if visita == "sì" or  visita == "SI" or visita == "si":
        atleta.effettua_visita()
    atleta.dati()
    atleta.squadra(team)
main()
