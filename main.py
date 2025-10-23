import os
import time
import random

def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def voltar():
    print('\n------------------------------------------------')
    print('Voltando ao menu. Aperte qualquer tecla para continuar')
    input('')
    menu()

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

    with open('lista.txt', 'w') as file:
        file.write(','.join(map(str, lista)))
    
    return lista

def carregarLista():
    if not os.path.exists('lista.txt'):
        return []
    
    with open('lista.txt', 'r') as file:
        conteudo = file.read().strip()
        
        if not conteudo:
            return []
        
        return list(map(int, conteudo.split(',')))

def imprimirRelatorio(lista, sort):
    limpar()
    start = time.time()
    sortLista = sort(lista)
    stop = time.time()

    print('\nRESULTADOS DO SORT')
    print('------------------------------------------------')
    if len(lista)> 20:
        print('- Lista original: ', str(lista[:10]).replace(']', ''), '...', str(lista[-10:]).replace('[', ''))
        print('- Lista ordenada: ', str(sortLista[:10]).replace(']', ''), '...', str(sortLista[-10:]).replace('[', ''))

    else:
        print('- Lista original: ', lista)
        print('- Lista ordenada: ', sortLista)

    print(f'- Tempo de ordenação: {(stop - start):.3f} segundos')
    voltar()

def imprimirRelCompleto(lista):
    limpar()
    print('------------------------------------------------')
    print('RELATÓRIO DE SORTS')
    print('------------------------------------------------')

    sorts = [
        ("bubble", bubbleSort ),
        ("selection", selectionSort ),
        ("insertion", insertionSort ),
        ("merge", mergeSort ),
    ]

    for nome, metodo in sorts:
        start = time.time()
        metodo(lista)
        stop = time.time()

        print(f'Tempo de ordenação do {nome} sort: {(stop - start):3f} segundos')

    voltar()

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

def menu():
    limpar()
    print('------------------------------------------------')
    print('ALGORITMOS DE SORTS')
    print('------------------------------------------------')
    print('Agora escolha qual sort deseja realizar:')
    print('1. Bubble Sort\n2. Selection Sort\n3. Insertion Sort\n4. Merge Sort\n5. Gerar relatório completo\n6. Definir nova lista\n7. Encerrar programa')

    escolha = validarInteiroLimite(1, 7)
    lista = carregarLista()

    match escolha:
        case 1:
            imprimirRelatorio(lista, bubbleSort)

        case 2:
            imprimirRelatorio(lista, selectionSort)

        case 3:
            imprimirRelatorio(lista, insertionSort)

        case 4:
            imprimirRelatorio(lista, mergeSort)

        case 5:
            imprimirRelCompleto(lista)

        case 6:
            main()

        case 7:
            print('------------------------------------------------')
            print('PROGRAMA FINALIZADO')
            print('------------------------------------------------')
            return

def main():
    limpar()
    print('------------------------------------------------')
    print('PROGRAMA DE TESTE DE SORTS')
    print('------------------------------------------------')
    print('Precisamos definir uma lista para testagem.')
    
    listaArquivo = carregarLista()
    if listaArquivo:
        print('Foi encontrado um arquivo lista.txt com dados.')
        print('1. Usar a lista existente\n2. Gerar uma nova lista\n3. Encerrar programa')
        escolha = validarInteiroLimite(1, 3)
        if escolha == 1:
            pass
        elif escolha == 2:
            criarlista()
        elif escolha == 3:
            print('------------------------------------------------')
            print('PROGRAMA FINALIZADO')
            print('------------------------------------------------')
            return

    else:
        print('Nenhum arquivo lista.txt válido encontrado. Criando nova lista...')
        criarlista()

    menu()

main()