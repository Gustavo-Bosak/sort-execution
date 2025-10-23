import os
import time
import random
import matplotlib.pyplot as plt

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
    print('Para gerar uma nova lista, escolha o tamanho entre as opções:')
    print('1. 1.000 elementos\n2. 5.000 elementos\n3. 10.000 elementos\n4. 25.000 elementos\n5. 50.000 elementos\n')

    escolha = validarInteiroLimite(1, 5)
    match escolha:
        case 1:
            n = 1000
        case 2:
            n = 5000
        case 3:
            n = 10000
        case 4:
            n = 25000
        case 5:
            n = 50000

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

def gerarGrafico(sorts):
    nomes = [(sort["nome"].capitalize()+' Sort') for sort in sorts]
    tempos = [sort["tempo"] for sort in sorts]

    plt.style.use('seaborn-v0_8')
    plt.figure(figsize=(10, 6))
    barras = plt.bar(nomes, tempos)

    plt.title('Comparação de Tempo de Execução dos Sorts', fontsize=14)
    plt.xlabel('Algoritmos de Ordenação', fontsize=12)
    plt.ylabel('Tempo (segundos)', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    for barra in barras:
        altura = barra.get_height()
        plt.text(barra.get_x() + barra.get_width()/2, altura + 0.01, f'{altura:.2f}', ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig('relatorio-sorts.png')
    plt.close()

def imprimirRelatorio(lista, sort):
    print('------------------------------------------------')
    print('\nRESULTADOS DO SORT')
    print('------------------------------------------------')
    
    limpar()
    start = time.time()
    sortLista = sort(lista)
    stop = time.time()

    if len(lista)> 20:
        print('- Lista original: ', str(lista[:10]).replace(']', ''), '...', str(lista[-10:]).replace('[', ''))
        print('- Lista ordenada: ', str(sortLista[:10]).replace(']', ''), '...', str(sortLista[-10:]).replace('[', ''))

    else:
        print('- Lista original: ', lista)
        print('- Lista ordenada: ', sortLista)

    print(f'- Tempo de ordenação: {(stop - start):.3f} segundos')

    with open(f'lista-{(sort.__name__).replace('Sort', '-sorted')}.txt', 'w') as file:
        file.write(','.join(map(str, sortLista)))

    print('------------------------------------------------')
    print('\nUm arquivo com a lista ordenada completa foi gerado.')
    voltar()

def imprimirRelCompleto(lista):
    limpar()
    print('------------------------------------------------')
    print('RELATÓRIO DE SORTS')
    print('------------------------------------------------')

    sorts = [
        {
            "nome": "bubble",
            "metodo": bubbleSort,
            "tempo": 0
        },
        {
            "nome": "selection",
            "metodo": selectionSort,
            "tempo": 0
        },
        {
            "nome": "insertion",
            "metodo": insertionSort,
            "tempo": 0
        },
        {
            "nome": "merge",
            "metodo": mergeSort,
            "tempo": 0
        }
    ]

    for sort in sorts:
        start = time.time()
        sort['metodo'](lista)
        stop = time.time()
        sort['tempo'] = stop - start

        print(f'Tempo de ordenação do {sort["nome"]}: {sort["tempo"]:.3f} segundos')

    gerarGrafico(sorts)

    print('------------------------------------------------')
    print('\nUm arquivo de imagem foi gerado com comparação gráfica do tempo de ordenação dos sorts.')

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
            limpar()
            lista = criarlista()
            voltar()

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
    print('Precisamos definir uma lista para testagem.', end=' ')
    
    listaArquivo = carregarLista()
    if listaArquivo:
        print('Já existe uma lista para ser ordenada Deseja:')
        print('1. Gerar uma nova lista \n2. Continuar com a lista anterior\n3. Encerrar programa')
        escolha = validarInteiroLimite(1, 3)
        
        match escolha:
            case 1:
                criarlista()
            
            case 2:
                pass
            
            case 3:
                print('------------------------------------------------')
                print('PROGRAMA FINALIZADO')
                print('------------------------------------------------')
                return

    else:
        print('Será necessário gerar uma lista.')
        criarlista()

    menu()

main()