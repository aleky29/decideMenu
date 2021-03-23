import csv
import pandas
import random
import itertools
import numpy as np
from random import randint

def main():
    platosIngredientes = pandas.read_csv('platos_ingredientes.csv')
    #print(platosIngredientes)
    semanaDecidida,lista = createWeek(platosIngredientes) # 2 x nPlatos array

def createWeek(DishList):
    #escoge almuerzo y cena para una semana natural (7 dias)
    diasSemana = ['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo']
    availableDishes = DishList
    alreadyUsed = []
    listaCompra = []
    comida_dia  = ''
    cena_dia  = ''
    for dia in diasSemana:
        for i in range(0,2):
            if i==0:
                comida_dia = availableDishes.sample(n = 1)
                availableDishes.drop(comida_dia.index,inplace=True)
                alreadyUsed.append(comida_dia.values[0][0])
                listaCompra.append(comida_dia.values[0][2])

            if i==1:
                while True:
                    cena_dia = availableDishes.sample(n = 1)

                    if cena_dia.values[0][1] == 'Proteina':
                        availableDishes.drop(cena_dia.index,inplace=True)
                        break
                alreadyUsed.append(cena_dia.values[0][0])
                listaCompra.append(cena_dia.values[0][2])
        print('Comida',dia,':',comida_dia.values[0][0])
        print('Cena',dia,':',cena_dia.values[0][0])
    # print('Lista de INGREDIENTES:',listaCompra)
    t = [l.split(',') for l in ','.join(listaCompra).split(';')]
    flat = [item for sublist in t for item in sublist]
    # print('postSplit y flatten: ',flat)
    listaCompra = checkIfDuplicate(flat)
    print('----------------------------------------------------')
    print('INGREDIENTES:',listaCompra)
    return (alreadyUsed,listaCompra)


def checkIfDuplicate(listofElems):
    #Tratamos los elementos repetidos, los contamos y luego lo reflejaremos

    for i in listofElems:
        if listofElems.count(i) > 1:
            #El elemento i está repetido n veces, lo sustituimos por un string de la forma:
            # n x ingrediente
            #por las características de esta aplicación simplemente se puede append
            nveces = listofElems.count(i)
            toIntroduce = str(nveces)+'x'+i
            listofElems.append(toIntroduce)
            #ahora que esta introducido, eliminamos todas las apariciones individuales
            for j in range(0,listofElems.count(i)):
                listofElems.remove(i)

    return listofElems
if __name__ == '__main__':
    main()
