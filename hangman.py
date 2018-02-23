# -*- coding: utf-8 -*-


import random


wisielec= (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")

MAX_WRONG = len(wisielec) - 1 # ilość maksymalna prob (do 7 prób)
WORDS = ("komputer", "gra", "wisielec", "samochod", "kalkulator", "telefon", "programista","python",)

#inicjalizacja zmiennych
word = random.choice(WORDS) # wygnerenoway losowo wyraz
so_far = "*" * len(word)    # litery nieodganiete
wrong = 0                   # ilosc prob
used = []                   # lista

print("##################################################WITAJ DROGI UŻYTKOWNIKU W GRZE!##################################################")

print("GRASZ NA WŁASNE RYZYKO :) POWODZENIA!")
print("ZGADNIJ MÓJ WYRAZ ZANIM ZAWIŚNIESZ ----->", WORDS)      

while wrong < MAX_WRONG and so_far != word: # petla wykonuje sie tak dlugo az nie przekroczy limitu prob lub nie odgadnie wyrazu
    print(wisielec
          [wrong])                  
    print("\nUŻYTE LITERY: \n", used) 
    print("\nSŁOWO ZGADAYWANE \n", so_far) 

    guess = input("\nPODAJ LITERE: ")
    guess = guess.lower()            

    while guess in used: 
        print("LITERA, KTÓRĄ PODEŁEŚ ZOSTAŁA POWTÓRZONA!")
        guess = input("PODAJ NOWĄ LITERĘ:")
        guess = guess.lower()

    used.append(guess) # dodajemy litere do naszej zmiennej w szukanym wyrazie

    if guess in word:
        print("\nTWOJA LITERA", guess, " WYSTĘPUJE W SZUKANYM WYRAZIE :)")

        new = "" # dodatkowa zmienna to wyswietlania odgadnietych juz liter
        for i in range(len(word)): # petla do wyswietlania liter w zgadywanym wyrazie
            if guess == word[i]:   # sprawdzanie czy litera jest w wyrazie literujac go
                new += guess       
            else:                  # nastepnie zapisuje odgadniete juz litery
                new += so_far[i]    
        so_far = new
    else:    
        print("\nNIESTETY, PODANA LITERA NIE WYSTĘPUJE W WYRAZIE: ",guess)
        wrong += 1

if wrong == MAX_WRONG:  # jesli ilosc prob jest rowna 8 zatrzymuje program/petle
    print(wisielec[wrong])
    print("\nZOSTAŁEŚ POWIESZONY!")
    print("\nSZUKANY WYRAZ: ",word)
else:                   
    print("GRATULUJE!!! UDAŁO SIĘ TOBIE ZGADNĄĆ WYRAZ!!!")



input("ABY ZAKOŃCZYĆ PROGRAM WCIŚNIJ ENTER")