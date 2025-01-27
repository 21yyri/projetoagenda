import os
# AGENDA DE TAREFAS LOCAL
# CAIO WESLEY, PEDRO LUCAS E YURI TEIXEIRA



def exibir(lista):
    for indice, item in enumerate(lista):
        print(f'{indice + 1}. {item}')

def substituir(lista, indice):
    atualizacao = input('').strip().capitalize()
    lista[indice - 1] = atualizacao

def deletar(lista, indice):
    del lista[indice - 1]


atividades = []
while True:
    print('Esta é uma agenda virtual.')
    opcao = input('Selecione entre (C)riar, (L)er, (S)ubstituir e (D)eletar.').upper().strip()[0]
    if opcao not in 'CLSD':
        print('Opção inválida.')
        os.system('cls')
        continue
    elif opcao == 'C':
        os.system('cls')
        tarefa = input('Insira a tarefa que deseja adicionar: ').strip().capitalize()
        atividades.append(tarefa)
    elif opcao == 'L':
        os.system('cls')
        print('Exibindo as tarefas registradas:')
        exibir(atividades)
    elif opcao == 'S':
        os.system('cls')
        print('Qual o índice da lista quer substituir? (Começando do 1.)')
        indice = int(input())
        try:
            substituir(atividades, indice)
        except:
            print('Índice inválido.')
            continue
        print(f'Atualizando o item {indice}. {atividades[indice]}.')
    elif opcao == 'D':
        os.system('cls')
        print('Insira o índice do item que deseja deletar: ')
        indice = int(input())
        print(f'Deletando o item {indice}. {atividades[indice - 1]}.')
        try:
            deletar(atividades, indice)
        except:
            print('Índice inválido.')
            os.system('cls')
            continue
