import os
import time
import random

def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def voltar(lista):
    print('\n------------------------------------------------')
    print('Voltando ao menu. Aperte qualquer tecla para continuar')
    input('')
    menu(lista)

def validarInteiroLimite(min, max):
    while True:
        entry = input('R: ')

        try:
            entry = int(entry)

            if entry < min or entry > max:
                print(f'\nNúmero fora do limite. Escolha entre {min} e {max}.')
                continue

            return entry
        
        except ValueError:
            print('\nInforme apenas números.')

def criarlista():
    print('Para gerar uma nova lista, informe a quantidade de elementos, com máximo de 900.000. (Apenas os números, exemplo: 10000).')

    n = validarInteiroLimite(1, 900000)
    lista = [random.randint(0, 9999) for _ in range(n)]
    
    return lista

def imprimirRelatorio(lista, sort):
    start = time.time()
    sortLista = sort(lista)
    stop = time.time()

    print('\nLISTAS')
    print('------------------------------------------------')
    if len(lista)> 20:
        print('- Lista original: ', lista[:10], '...', lista[-10:])
        print('- Lista ordenada: ', sortLista[:10], '...', sortLista[-10:])
    else:
        print('- Lista original: ', lista)
        print('- Lista ordenada: ', sortLista)

    print(f'- Tempo de ordenação: {(stop - start):.2f} segundos')
    voltar(lista)

def imprimirRelCompleto(lista):
    limpar()

    sorts = [
        {
            "nome": "bubble",
            "metodo": bubbleSort,
            "execucao": 0
        },
        {
            "nome": "selection",
            "metodo": selectionSort,
            "execucao": 0
        },
        {
            "nome": "insertion",
            "metodo": insertionSort,
            "execucao": 0
        },
        {
            "nome": "merge",
            "metodo": mergeSort,
            "execucao": 0
        }
    ]

    for i in range(4):
        start = time.time()
        sorts[i]["metodo"](lista)
        stop = time.time()
        sorts[i]["execucao"] = stop - start

    print('------------------------------------------------')
    print('RELATÓRIO DE SORTS')
    print('------------------------------------------------')
    
    for i in range(4):
        print(f'Tempo de ordenação do {sorts[i]["nome"]} sort: {(sorts[i]["execucao"]):.2f} segundos')
    voltar(lista)

def bubbleSort(lista):
    bubbleLista = lista.copy()
    
    for i in range(len(bubbleLista)):
        for j in range(len(bubbleLista)-i-1):
            if bubbleLista[j] > bubbleLista[j+1]:
                bubbleLista[j], bubbleLista[j+1] = bubbleLista[j+1], bubbleLista[j]

    return bubbleLista

def selectionSort(lista):
    selectionLista = lista.copy()
    # as lógicas aqui, baseadas nessa lista copiada
    return selectionLista

def insertionSort(lista):
    insertionLista = lista.copy()
    # as lógicas aqui, baseadas nessa lista copiada
    return insertionLista

def mergeSort(lista):
    mergeLista = lista.copy()
    # as lógicas aqui, baseadas nessa lista copiada
    return mergeLista

def menu(lista):
    limpar()
    print('------------------------------------------------')
    print('ALGORITMOS DE SORTS')
    print('------------------------------------------------')
    print('Agora escolha qual sort deseja realizar:')
    print('1. Bubble Sort\n2. Selection Sort\n3. Insertion Sort\n4. Merge Sort\n5. Gerar relatório completo\n6. Definir nova lista\n7. Encerrar programa')

    escolha = validarInteiroLimite(1, 7)
    match escolha:
        case 1:
            limpar()
            print('------------------------------------------------')
            print('BUBBLE SORT')
            print('------------------------------------------------')
            imprimirRelatorio(lista, bubbleSort)

        case 2:
            limpar()
            print('------------------------------------------------')
            print('SELECTION SORT')
            print('------------------------------------------------')
            imprimirRelatorio(lista, selectionSort)

        case 3:
            limpar()
            print('------------------------------------------------')
            print('INSERTION SORT')
            print('------------------------------------------------')
            imprimirRelatorio(lista, insertionSort)

        case 4:
            limpar()
            print('------------------------------------------------')
            print('MERGE SORT')
            print('------------------------------------------------')
            imprimirRelatorio(lista, mergeSort)

        case 5:
            imprimirRelCompleto(lista)

        case 6:
            main(lista)

        case 7:
            print('------------------------------------------------')
            print('PROGRAMA FINALIZADO')
            print('------------------------------------------------')
            return

def main(lista = []):
    limpar()
    print('------------------------------------------------')
    print('PROGRAMA DE TESTE DE SORTS')
    print('------------------------------------------------')
    print('Precisamos definir uma lista para testagem.')

    if len(lista) > 0:
        print('1. Gerar uma nova lista \n2. Continuar com a lista anterior\n3. Encerrar programa')
        escolha = validarInteiroLimite(1, 3)
        
        match escolha:
            case 1:
                listaSort = criarlista()
            
            case 2:
                listaSort = lista

            case 3:
                print('------------------------------------------------')
                print('PROGRAMA FINALIZADO')
                print('------------------------------------------------')
                return
    else:
        listaSort = criarlista()

    menu(listaSort)

main()