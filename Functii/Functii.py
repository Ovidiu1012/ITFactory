print('1. Functie care sa calculeze si sa returneze suma a 2 numere')
def suma_2_numere(a,b):
    suma = a + b
    return suma

functie_suma = suma_2_numere(int(input('Completati un numar: ')), int(input('Completati inca un numar: ')))
print (f'\nSuma numerelor introduse este: {functie_suma}')
print('--------------------------------------------------------------')

print('2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar')
def func_par(x):
    if x%2 == 0:
        return 'TRUE'
    else:
        return 'FALSE'

numar_par = func_par(int(input('Completati un numar: ')))
print(f'\nNumarul introdus este par? {numar_par}')
print('--------------------------------------------------------------')

print('3. Functie care returneaza numarul total de caractere din numele tau complet.\
(nume, prenume, nume_mijlociu)')
def numar_caractere(nume, prenume, nume_mijlociu):
    caractere = len(nume)+len(prenume)+len(nume_mijlociu)
    return caractere
numar_caractere_nume = numar_caractere(input('Completati numele dvs.: '), input('Completati prenumele dvs.: '), input('Completati numele mijlociu.: '))
print(f'\nNumele dvs. contine {numar_caractere_nume}')
print('--------------------------------------------------------------')

print('4. Functie care returneaza aria dreptunghiului')
def aria_dreptunghi(x,y):
    arie = x*y
    return arie
arie_dreptunghi = aria_dreptunghi(int(input('Completati lungimea dreptunghiului: ')),int(input('Completati latimea dreptunghiului: ')))
print(f'\nAria dreptunghiului este: {arie_dreptunghi}')
print('--------------------------------------------------------------')

print('5. Functie care returneaza aria cercului')
import math
def aria_cerc(r):
    arie = math.pi*r**2
    return arie
arie_cerc = aria_cerc(int(input('Completati raza cercului: ')))
print(f'\nAria cercului este: {arie_cerc}')
print('--------------------------------------------------------------')

print('6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. False daca nu')
cuvant = input('Completati un cuvant: ')
def exista_caracter(i):
    if i in cuvant:
        return 'True'
    else:
        return 'False'
rezultat = exista_caracter(input('Completati un caracter: '))
print(f'\nCaracterul exista in cuvantul dat?: {rezultat}')
print('--------------------------------------------------------------')

print('7. Functie fara return, primeste un string si printeaza pe ecran: \
\nNr de caractere lower case este x \
\nNr de caractere upper case exte y \
')

cuvant = input('Completati un string: ')
def lower_upper(s):
    x = 0
    y = 0
    for i in range(len(s)):
        if s[i].isupper():
            x +=1
        else:
            y +=1
    print(f'\nNr de caractere upper case este {x}')
    print(f'Nr de caractere lower case este {y}')
lower_upper(cuvant)
print('--------------------------------------------------------------')

print('8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive')

lista = [1,2,3,-1,-4,-5,0]
print(f'Lista contine {lista}')
def numere_pozitive(x):
    lista_pozitiva=[]
    for i in x:
        if i >= 0:
            lista_pozitiva.append(i)
    return lista_pozitiva
lista_noua = numere_pozitive(lista)
print(f'\nLista noua cu numere pozitive este {lista_noua}')
print('--------------------------------------------------------------')

print('9. Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA\
\nPrimul numar x este mai mare decat al doilea nr y\
\nAl doilea nr y este mai mare decat primul nr x\
\nNumerele sunt egale. \
')

def func_info(x,y):
    if x>y:
        print(f'\nPrimul numar {x} este mai mare decat al doilea nr {y}')
    elif x<y:
        print(f'\nAl doilea nr {y} este mai mare decat primul nr {x}')
    else:
        print(f'\nNumerele sunt egale')

func_info(int(input('\nCompletati valoarea lui x: ')),int(input('Completati valoarea lui y: ')))
print('--------------------------------------------------------------')

print('10. Functie care primeste un numar si un set de numere.\
\nPrinteaza ‘am adaugat numarul nou in set’ + returneaza True\
\nSau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False\
')
set = {1,2,3,4,5,6}
print(set)
def func_10(x):
    if x in set:
        print('Nu am adaugat numarul in set. Acesta exista deja')
        return 'False'
    else:
        set.add(x)
        print('Am adaugat numarul nou in set')
        return 'True'

valoare_func = func_10(int(input('\nCompletati un numar: ')))
print(valoare_func)
print('--------------------------------------------------------------')

print('11. Functie care primeste o luna din an si returneaza cate zile are acea luna')
from calendar import monthrange
an = int(input('Completati anul: '))
luna = int(input('Completati numarul lunii: '))
def numar_zile_luna(an, luna):
    return monthrange(an, luna)[1]

rezultat = numar_zile_luna(an, luna)
print(f'\nNumarul de zile din luna {luna} si din anul {an} este: {rezultat} zile')
print('--------------------------------------------------------------')

print('12. Functie calculator care sa returneze 4 valori \
\nSuma, diferenta, inmultirea, impartirea a 2 numere\
\
\nIn final vei putea face:\
\na, b, c, d = calculator(10, 2)\
\nprint("Suma: ", a)\
\nprint("Diferenta: ", b)\
\nprint("Inmultirea: ", c)\
\nprint("Impartirea: ", d)\
')
def calculator(x,y):
    o1 = x+y
    o2 = x-y
    o3 = x*y
    o4 = x/y
    return o1,o2,o3,o4
a,b,c,d = calculator(int(input('\nCompletati o valoare pentru x: ')), int(input('Completati o valoare pentru y: ')))
print("\nSuma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)
print('--------------------------------------------------------------')

print('13. Functie care primeste o lista de cifre (adica doar 0-9)\
\nEx: [1, 3, 1, 5, 9, 7, 7, 5, 5]\
\nReturneaza un DICT care ne spune de cate ori apare fiecare cifra\
\n=> dict {\
\n0: 0\
\n1 :2\
\n2: 0\
\n3: 1\
\n4: 0\
\n5: 3\
\n6: 0\
\n7: 2\
\n8: 0\
\n9: 1\
\n}\
')

def func_dict(*dict):
    dict_meu = {}
    zero = 0
    unu = 0
    doi = 0
    trei = 0
    patru = 0
    cinci = 0
    sase = 0
    sapte = 0
    opt = 0
    noua = 0
    for i in dict:
        if i>=0 and i<=9:
            if i == 0:
                zero += 1
            elif i == 1:
                unu += 1
            elif i == 2:
                doi += 1
            elif i == 3:
                trei += 1
            elif i == 4:
                patru += 1
            elif i == 5:
                cinci += 1
            elif i == 6:
                sase += 1
            elif i == 7:
                sapte += 1
            elif i == 8:
                opt += 1
            else:
                noua +=1
        else:
            print(f'\nNumarul {i} nu se incadreaza in intervalul 0-9')
    dict_meu[0] = zero
    dict_meu[1] = unu
    dict_meu[2] = doi
    dict_meu[3] = trei
    dict_meu[4] = patru
    dict_meu[5] = cinci
    dict_meu[6] = sase
    dict_meu[7] = sapte
    dict_meu[8] = opt
    dict_meu[9] = noua
    return dict_meu
rezultat = func_dict(2,3,5,5,2,4,2)
print(rezultat)
print('--------------------------------------------------------------')

print('14. Functie care primeste 3 numere. Returneaza valoarea maxima dintre ele')

def maxim(x,y,z):
    maxim = max(x,y,z)
    return maxim
rezultat = maxim(int(input('\nCompletati un numar: ')),int(input('Completati un numar: ')),int(input('Completati un numar: ')))
print(f'Numarul cel mai mare dintre numerele introduse este {rezultat}')
print('--------------------------------------------------------------')

print('15. Functie care sa primeasca un numar si sa returneze suma tuturor numerelor de la 0 la acel numar\
\nEx: daca dam nr 3\
\nSuma va fi 6 (0+1+2+3)\
')

def suma(x):
    sumax = 0
    for i in range(1, x + 1, 1):
        sumax +=i
    return sumax
rezultat = suma(int(input('\nCompletati un numar: ')))
print(f'\nSuma pana la numarul respectiv este {rezultat}')
print('--------------------------------------------------------------')

print('16. Functie care primesete 2 liste de numere (numerele pot fi dublate)\
\nReturnati numerele comune \
\nEx:\
\nlist1 = [1, 1, 2, 3]\
\nlist2 = [2, 2, 3, 4]\
\nRaspuns: {2, 3}\
')

def comune(x,y):
    lista_comuna = set(x).intersection(y)
    return lista_comuna
rezultat = comune([1,2,3,4,5],[4,5,6,7,8,9])
print(f'\nNumerele comune din cele 2 liste sunt {rezultat}')
print('--------------------------------------------------------------')

print('17. Functie care sa aplice o reducere de pret\
\nDaca produsul costa 100 lei si aplicam reducere de 10%\
\nPretul va fi 90\
\nTratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalida\
')

def reducere(x,y):
    if y > 0 and y <= 100:
        redus = x-x*y/100
    else:
        print(f'Reducere invalida: {y}%')
    return redus
rezultat = reducere(int(input('\nCompletati un pret: ')), int(input('Completati un procent de reducere: ')))
print(f'\nPretul redus este {rezultat}')
print('--------------------------------------------------------------')

print('18. Functie care sa afiseze data si ora curenta din ro\
\n(bonus: afisati si data si ora curenta din China)\
')

from datetime import datetime
import pytz
def get_date_timezone(x):
    now = datetime.now(pytz.timezone(x))
    formatat = now.strftime("%d/%m/%Y %H:%M:%S")
    return formatat
x = input('\nCompletati un timezone (pentru China completati Asia/Kolkata): ')
rezultat = get_date_timezone(x)
print(f'\nData si ora curenta in {x} este {rezultat}')
print('--------------------------------------------------------------')
def data_curenta_ro():
    now = datetime.now()
    formatat = now.strftime("%d/%m/%Y %H:%M:%S")
    return formatat
rezultat = data_curenta_ro()
print(f'\nData si ora curenta in Romania este {rezultat}')
print('--------------------------------------------------------------')

print('19. Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la craciun daca nu vrei sa ne zici cand e ziua ta :)')

from datetime import datetime
def zile_pana_la_ziua_ta(x):
    now = datetime.now()
    formatat_zi_nastere = datetime.strptime(x, "%Y/%m/%d")
    diferenta = formatat_zi_nastere - now
    return diferenta.days
rezultat = zile_pana_la_ziua_ta(input('\nCompletati urmatoarea zi de nastere(yyyy/MM/dd): '))
print(f'\nPana la ziua ta de nastere mai sunt {rezultat} zile')
print('--------------------------------------------------------------')