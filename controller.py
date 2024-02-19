class Kniznica:
    def __init__(self):
        self.zoznam_knih = []

    def pridaj_knihu(self, kniha):
        self.zoznam_knih.append(kniha)
        print("Kniha ", kniha.nazov, "bola pridana do kniznice.")


    def vyhladat_podla_nazvu(self, nazov):
        for kniha in self.zoznam_knih:
            if kniha.nazov == nazov:
                return kniha
        return None


    def vyhliadat_podla_isbn(self, isbn):
        for kniha in self.zoznam_knih:
            if kniha.isbn == isbn:
                return kniha
        return None


    def vypozicaj_knihu(self, isbn):
        for kniha in self.zoznam_knih:
            if (kniha.isbn == isbn):
                kniha.vypozicaj()


    def vratit_knihu(self, isbn):
        kniha = self.vyhliadat_podla_isbn(isbn)
        if kniha:
            kniha.vratit()
        else:
            print("Kniha s daným ISBN neexistuje.")


    def zobraz_dostupne_knihy(self):
        dostupne_knihy = [kniha for kniha in self.zoznam_knih if kniha.dostupna]
        if dostupne_knihy:
            print("Dostupné knihy:")
            for kniha in dostupne_knihy:
                print(kniha.nazov)
        else:
            print("Ziadne knihy nie su dostupne.")


