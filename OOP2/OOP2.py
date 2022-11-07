'''ABSTRACTION
Clasa abstracta FormaGeometrica
Contine un field PI=3.14
Contine o metoda abstracta aria (optional)
Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’
'''

class FormaGeometrica():
    PI = 3.14
    raza = None
    def aria(self):
        aria = self.PI * self.raza ** 2
        return aria
    def descrie(self):
        print('Cel mai probabil am colturi')

'''INHERITANCE
Clasa Patrat - mosteneste FormaGeometrica
constructor pt latura
ENCAPSULATION
latura este proprietate privata
Implementati getter, setter, deleter pt latura
Implementati metoda ceruta de interfata (optional, doar daca ati ales sa implementati metoda abstracta aria)
'''
class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        return self.__latura

    @latura.setter
    def latura(self, latura):
        self.__latura = latura

    @latura.deleter
    def latura(self):
        self.__latura = None

'''Clasa Cerc - mosteneste FormaGeometrica
constructor pt raza
raza este proprietate privata
Implementati getter, setter, deleter pt raza
Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte (optional, doar daca ati ales sa implementati metoda abstracta aria)
'''

class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza
    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, raza):
        self.__raza = raza

    @raza.deleter
    def raza(self):
        self.__raza = None

    '''POLYMORPHISM 
    Definiti o noua metoda descrie - printati ‘Eu nu am colturi’
    Creati un obiect de tip Patrat si jucati-va cu metodele lui
    Creati un obiect de tip Cerc si jucati-va cu metodele lui
    '''

    def descrie(self):
        print('Eu nu am colturi')

patrat1 = Patrat(2)
patrat1.latura = 3
patrat1.latura
del patrat1.latura
patrat1.latura
patrat1.descrie()

cerc1 = Cerc(2)
cerc1.raza = 3
cerc1.raza
del cerc1.raza
cerc1.raza
cerc1.descrie()