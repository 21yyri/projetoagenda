import os
# AGENDA DE TAREFAS LOCAL
# Introdução a Programação
# Informática - 1° ano - manhã
# CAIO WESLEY, PEDRO LUCAS, DIEGO VINICIUS E YURI TEIXEIRA

def exibir(lista):
    if len(lista) > 0:
        for indice, item in enumerate(lista):
            print(f'{indice + 1}. {item}')
            if descricoes[indice] != None:
                print(f'  ┗ {descricoes[indice]}')
    else:
        print('Agenda de tarefas vazia.')

def substituir(lista, indice, desc):
    atualizacao = input(f'O que deseja por no índice {indice + 1}? ').strip().lower().capitalize()
    lista[indice] = atualizacao
    opcao = input('Deseja atualizar a descrição? ').upper().strip()[0]
    if opcao == 'S':
        desc[indice - 1] = input('Digite a nova descrição: \n')
    else:
        desc[indice - 1] = None


def deletar(lista, indice, desc):
    try:
        del lista[indice - 1]
        del desc[indice - 1]
    except:
        print('Índice inválido.')


atividades = []
descricoes = []
while True:
    print('Esta é uma agenda virtual.')
    opcao = input('Selecione entre (C)riar, (L)er, (S)ubstituir e (D)eletar.').upper().strip()[0]
    if opcao not in 'CLSD':
        print('Opção inválida.')
        os.system('cls' if os.name == 'nt' else 'clear')
        continue

    match opcao:
        case 'C':
            os.system('cls' if os.name == 'nt' else 'clear')
            tarefa = input('Insira a tarefa que deseja adicionar: ').strip().capitalize()
            atividades.append(tarefa)
            escolha = input('Deseja escrever uma breve descrição da atividade? (S/N) ').upper().strip()
            if escolha == 'S':
                descricao = input('Digite aqui a descrição da tarefa: \n')
                descricoes.append(descricao)
            elif escolha == 'N':
                descricoes.append(None)
            else:
                print('Operação falha.')
                atividades.pop()
        case 'L':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Exibindo as tarefas registradas:')
            exibir(atividades)
        case 'S':
            os.system('cls' if os.name == 'nt' else 'clear')
            exibir(atividades)
            if len(atividades) == 0:
                continue
            print('Qual o índice da lista quer substituir? (Começando do 1.)')
            indice = int(input())
            try:
                substituir(atividades, indice - 1, descricoes)
            except:
                print('Índice inválido.')
                continue
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'Atualizando o item {indice}. {atividades[indice - 1]}.')
        case 'D':
            os.system('cls' if os.name == 'nt' else 'clear')
            exibir(atividades)
            print('Insira o índice do item que deseja deletar: ')
            indice = int(input())
            try:
                deletar(atividades, indice, descricoes)
                print(f'Deletando o item {indice}. {atividades[indice - 1]}.')
            except:
                continue
