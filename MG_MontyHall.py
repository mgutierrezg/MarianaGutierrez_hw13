import numpy as np
import random as rd
from random import shuffle
#Funcion que crea la lista y la desordena de manera aleatoria. Retorna la lista desordenada 
def sort_doors():
    lista = ["goat", "goat", "car"]
    shuffle(lista)
    return lista

#Funcion para escoger la puerta 
def choose_door():
    x = np.random.choice(3,1)
    return x
#Funcion que revela donde hay una cabra

def reveal_door(lista, choice):
    for i in range(len(lista)):
        if (i != choice) and (lista[i] == "goat"):
            lista[i] = "GOAT_MONTY"
            return lista
    
#Revela todas la puertas si se cambia imprime la que no es chpoice ni GOAT_MONTYsi no imprime choice
def finish_game(lista,choice,change):
    if (change == False):
        x = choice[0]
        return lista[x]
    else:
        for i in range(len(lista)):
            if(i != choice) and (lista[i] != "GOAT_MONTY"):
                return lista[i]

t = 0
for i in range(100):
    lista_es = sort_doors()
    ch = choose_door()
    lista2 = reveal_door(lista_es, ch)
    con_true = finish_game(lista2,ch,True)
    if (con_true == "car"):
        t +=1

        
f  = 0
for i in range(100):
    lista_es = sort_doors()
    ch = choose_door()
    lista2 = reveal_door(lista_es, ch)
    con_true = finish_game(lista2,ch,False)
    if (con_true == "car"):
        f +=1

print "La probabilidad de ganar con hubo cambio de puerta es de: ", t , "%"
print  "La probabilidad de ganar con no hubo cambio de puerta es de: ", f , "%"
