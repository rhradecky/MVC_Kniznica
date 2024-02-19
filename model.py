class Kniha:
    def __init__(self, nazov, autor, isbn, rok):
        self.nazov = nazov
        self.autor = autor
        self.isbn = isbn
        self.rok = rok
        self.dostupna = True

    def vypozicaj(self):
            self.dostupna = False
            print("Kniha ", self.nazov, " nie je dostupna")

    def vratit(self):
            self.dostupna = True
            print("Kniha ", self.nazov, " je dostupna")