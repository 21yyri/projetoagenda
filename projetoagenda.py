import os
# AGENDA DE TAREFAS LOCAL
# Introdução a Programação
# Informática - 1° ano - manhã
# CAIO WESLEY, PEDRO LUCAS, DIEGO VINICIUS E YURI TEIXEIRA

def exibir(lista):
    if len(lista) > 0:
        for indice, item in enumerate(lista):
            print(f'{indice + 1}. {item}')
    else:
        print('Agenda de tarefas vazia.')

def substituir(lista, indice):
    atualizacao = input(f'O que deseja por no índice {indice}? ').strip().lower().capitalize()
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

    match opcao:
        case 'C':
            os.system('cls')
            tarefa = input('Insira a tarefa que deseja adicionar: ').strip().capitalize()
            atividades.append(tarefa)
        case 'L':
            os.system('cls')
            print('Exibindo as tarefas registradas:')
            exibir(atividades)
        case 'S':
            os.system('cls')
            exibir(atividades)
            if len(atividades) == 0:
                continue
            print('Qual o índice da lista quer substituir? (Começando do 1.)')
            indice = int(input())
            try:
                substituir(atividades, indice)
            except:
                print('Índice inválido.')
                continue
            os.system('cls')
            print(f'Atualizando o item {indice}. {atividades[indice]}.')
        case 'D':
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
