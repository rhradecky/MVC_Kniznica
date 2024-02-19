from controller import Kniznica

class Sklad(Kniznica):
    def zobraz_dostupne_knihy(self):
        dostupne_knihy = [kniha for kniha in self.zoznam_knih if kniha.dostupna]
        if dostupne_knihy:
            print("Dostupné knihy:")
            for kniha in dostupne_knihy:
                print(kniha.nazov)
        else:
            print("Ziadne knihy nie su dostupne.")
