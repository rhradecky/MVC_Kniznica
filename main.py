from controller import Kniznica
from model import Kniha
#from view import ShoesView





kniha1 = Kniha("Harry Potter","Rowlingova",  1001, 2010)
kniha2 = Kniha("Pan Prstenov", "Tolkien", 1002, 2003)
kniha3 = Kniha("Vkladna Knizka", "Slovenska Sporitelna", 1103, 2000)



kniznica = Kniznica()
kniznica.pridaj_knihu(kniha1)
kniznica.pridaj_knihu(kniha2)
kniznica.pridaj_knihu(kniha3)
print("******************")
kniznica.vypozicaj_knihu(1001)
kniznica.zobraz_dostupne_knihy()
print("******************")
kniznica.vratit_knihu(1001)
kniznica.zobraz_dostupne_knihy()