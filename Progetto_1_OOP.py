
#In una biblioteca digitale si vuole realizzare un piccolo sistema software per gestire libri,
#  utenti e prestiti.

#Parte 1 - Dichiarare e stampare alcune variabili di esempio:

titolo = "Lord of The Rings"
copie = 5
prezzo = float(15.25)
disponibile = True

print(
    f"--- Parte 1 ---\n"
    f"Titolo: {titolo}\n"
    f"Copie disponibili: {copie}\n"
    f"Price: {prezzo} $\n"
    f"Disponibile: {disponibile}"
)

#Parte 2 - Creare una lista con almeno 5 titoli, 
#un dizionario per titoli e num copie, un Set utenti registrati.

titoli = [
    "Il nome della rosa",
    "Cent'anni di solitudine",
    "I fratelli Karamazov",
    "Orgoglio e pregiudizio",
    "Il signore degli anelli"
]

copie_disp = {
    "Il nome della rosa": 3,
    "Cent'anni di solitudine": 5,
    "I fratelli Karamazov": 2,
    "Orgoglio e pregiudizio": 4,
    "Il signore degli anelli": 6
}

utenti = {"alice", "bob", "carla", "daniele", "elena", "franz"}

#Parte 3 - Creare una classe Libro con attributi titolo, autore, anno, copie disponibili.
#Aggiungere un metodo info() che restituisca una stringa descrittiva del libro.

class Libro:
    def __init__(self, titolo, autore, anno, copie_disponibili):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili

    def info_libro(self):
        return f"Libro: {self.titolo} - Autore: {self.autore} - Anno: {self.anno} - copie disponibili: {self.copie_disponibili}"

#Creare una classe Utente con attributi, e metodo scheda per stampare dati utente.

class Utente:
    def __init__(self, nome, eta, id_utente):
        self.nome = nome
        self.eta = eta
        self.id_utente = id_utente

    def scheda(self):
        print(f"Utente: {self.nome} - Età: {self.eta} - ID: {self.id_utente}")

#Eccezione personalizzata - numero copie
class Copie_Non_Disponibili(Exception):
    pass

#Classe Prestito che colleghi un Utente a un Libro e contenga: utente, libro, giorni. 
class Prestito:
    def __init__(self, utente, libro, giorni):
        self.utente = utente       
        self.libro = libro       
        self.giorni = giorni

#metodo 'dettagli()' che stampa tutte le info sul prestito

    def dettagli(self):
        print(f"{self.utente.nome} - ID: {self.utente.id_utente} - ha preso in prestito "
                f"'{self.libro.titolo}' "
                f"per {self.giorni} giorni. "
                f"Copie disponibili ora: {self.libro.copie_disponibili}")

#Parte 4 – Funzionalità -
#Creare una funzione presta_libro

    @classmethod
    def presta_libro(cls, utente, libro, giorni):
        if libro.copie_disponibili > 0:
            libro.copie_disponibili -= 1
            return cls(utente, libro, giorni)
        else:
            # sollevo eccezione personalizzata
            raise Copie_Non_Disponibili(f"Nessuna copia disponibile di: '{libro.titolo}' - richiesta da utente:'{utente.id_utente}'")

#-------Esecuzione-------#
#Simulare almeno 3 prestiti con utenti e libri diversi.
# Stampare:
#-L’elenco aggiornato delle copie disponibili per ciascun libro.
#-I dettagli di ogni prestito effettuato.

print("--- Libri in Prestito ---")

libro1 = Libro("Il nome della rosa", "Umberto Eco", 1980, 3)
libro2 = Libro("I Fratelli Karamazov", "Fedor Dostoevskij", 1880, 0)
libro3 = Libro("Cent'anni di solitudine", "Gabriel García Márquez", 1967, 4)
libro4 = Libro("Orgoglio e pregiudizio", "Jane Austen", 1813, 5)

utente1 = Utente("Davide", 22, "B3456")
utente2 = Utente("Elena", 29, "B1234")
utente3 = Utente("Daniele", 35, "B6789")

prestito1 = Prestito.presta_libro(utente1, libro1, 12)
prestito3 = Prestito.presta_libro(utente3, libro4, 7)  

prestito1.dettagli()
prestito3.dettagli()

try:
    prestito2 = Prestito.presta_libro(utente2, libro2, 5)  
    prestito2.dettagli()
except Copie_Non_Disponibili as e:
    print(e)