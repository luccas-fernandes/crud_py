import json
import os
from time import sleep


class cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'


arquivo = os.path.join(os.path.dirname(__file__), 'restaurantes.json')
arquivoReservas = os.path.join(os.path.dirname(__file__), 'reservas.json')


def adicionar_reserva(nome, data, horario, restaurante):
    with open(arquivoReservas, 'r') as f:
        reservas = json.load(f)

    reservas.append({'nome': nome, 'data': data, 'horario':horario, 'restaurante': restaurante})

    with open(arquivoReservas, 'w') as f:
        json.dump(reservas, f, indent=4)
    print("😎 RESERVA ADICIONADA COM SUCESSO!")

def listar_restaurantes():
    with open(arquivo, 'r') as f:
        restaurantes = json.load(f)

    if restaurantes:
        print("=" *50)
        print("LISTA DE RESTAURANTES:")
        print("-" *50)
        for restaurante in restaurantes:
            print("*" *50)
            print(f"NOME: {restaurante['nome']}, COZINHA: {restaurante['cozinha']}, HORARIO: {restaurante['horario']}, AVALIACAO: {restaurante['avaliacao']}")
            print("*" *50)
            print("=" *50)
    else:
        print("😒 NENHUM RESTAURANTE ENCONTRADO.")

def atualizar_reserva(nome_antigo, novo_nome, nova_data, novo_horario, novo_restaurante):
    with open(arquivoReservas, 'r') as f:
        reservas = json.load(f)

    for reserva in reservas:
        if reserva['nome'] == nome_antigo:
            reserva['nome'] = novo_nome
            reserva['data'] = nova_data
            reserva['horario'] = novo_horario
            reserva['restaurante'] = novo_restaurante
            break

    with open(arquivoReservas, 'w') as f:
        json.dump(reservas, f, indent=4)
    print("😙 RESERVA ATUALIZADA COM SUCESSO!")

def excluir_reserva(nome, data, horario, restaurante):
    with open(arquivoReservas, 'r') as f:
        reservas = json.load(f)

    for reserva in reservas:  
        if reserva['nome'] == nome:
           reserva['data'] == data
           reserva['horario'] == horario
           reserva['restaurante'] == restaurante
            
        reservas.remove(reserva)

    with open(arquivoReservas, 'w') as f:
        json.dump(reservas, f, indent=4)
        print("😡 RESERVA EXCLUÍDA COM SUCESSO!")

def buscar_reserva (nome, data, horario, restaurante):
    with open(arquivoReservas, 'r') as f:
        reservas = json.load(f)
    
    encontrado = False

    for reserva in reservas:
        if reserva['nome'] == nome:
            reserva['data'] = data  # Correção: usar '=' para atribuir valor
            reserva['horario'] = horario
            reserva['restaurante'] = restaurante
        print(f"NOME: {reserva['nome']}, DATA: {reserva['data']}, HORÁRIO: {reserva['horario']}, RESTAURANTE: {reserva['restaurante']}")
        encontrado = True

    if not encontrado:  # Verificação fora do loop
        print("😒 NENHUMA RESERVA CADASTRADA.")
    
def listar_reservas():
    with open(arquivoReservas, 'r') as f:
        reservas = json.load(f)

    if reservas:
        print("=" *50)
        print("LISTA DE RESERVAS:")
        print("-" *50)
        for reserva in reservas:
            print("*" *50)
            print(f"NOME: {reserva['nome']}, DATA: {reserva['data']}, HORARIO: {reserva['horario']}, RESTAURANTE: {reserva['restaurante']}")
            print("*" *50)
            print("=" *50)
    else:
        print("😒 NENHUMA RESERVA ENCONTRADO.")


def linha_horizontal(cor):
    return cor + "=" * 50 + cor['RESET']

def menu_inicial ():
    print (cor.CIANO + "=" *55 + cor.RESET)
    print (cor.VERMELHO + " ---->>> BEM VINDO AO RESERVA JÁ <<<---- ")
    print ("          1 - MÓDULO RESERVAS ")
    print ("          2 - MÓDULO RESTAURANTES ")
    print ("          3 - SAIR ")
    print (cor.CIANO + "=" *55 + cor.RESET)
    
def exibir_menu():
    print("\nMENU:")
    print("1. ADICIONAR RESERVA")
    print("2. LISTAR RESTAURANTES")
    print("3. ATUALIZAR RESERVA")
    print("4. EXCLUIR RESERVA")
    print("5. LISTAR UMA RESERVA")
    print("6. LISTAR TODAS AS RESERVAS")
    print("7. VOLTAR AO MENU ANTERIOR")



def main():
    
    while True:
        menu_inicial()
        opcao_inicial = int(input("INFORME UMA OPÇÃO"))

        match (opcao_inicial):
            case 2:
                print("MÓDULO EM DESENVOLVIMENTO")

            case 1:
                while True: 
                    exibir_menu()
                    opcao = input("ESCOLHA UMA OPÇÃO:\n>>>")

                    if opcao == "1":
                        nome = input(" DIGITE O NOME:\n>>>")
                        data = input(" DIGITE A DATA:\n>>>")
                        horario = input(" DIGITE O HORÁRIO:\n>>>")
                        restaurante = input(" DIGITE O RESTAURANTE ESCOLHIDO:\n>>>")
                        adicionar_reserva(nome, data, horario, restaurante)
                    elif opcao == "2":
                        listar_restaurantes()
                    elif opcao == "3":
                        nome_antigo = input("DIGITE O NOME A SER ATUALIZADO:\n>>>")
                        novo_nome = input("DIGITE O NOVO NOME:\n>>>")
                        nova_data = input("DIGITE A NOVA DATA:\n>>>")
                        novo_horario = input("DIGITE O NOVO HORÁRIO:\n>>>")
                        novo_restaurante = input("DIGITE O NOVO RESTAURANTE:\n>>>")
                        atualizar_reserva(nome_antigo, novo_nome, nova_data, novo_horario, novo_restaurante)
                    elif opcao == "4":
                        nome = input("DIGITE O NOME QUE CONSTA NA RESERVA A SER EXCLUÍDA:\n>>>")
                        data = input("DIGITE A DATA QUE CONSTA NA RESERVA A SER EXCLUÍDA:\n>>>")
                        horario = input("DIGITE O HORARIO QUE CONSTA NA RESERVA A SER EXCLUÍDA:\n>>>")
                        restaurante = input("DIGITE O NOME DO RESTAURANTE QUE CONSTA NA RESERVA A SER EXCLUÍDA:\n>>>")
                        excluir_reserva(nome, data, horario, restaurante)
                    elif opcao == "5":
                        nome = input("DIGITE O NOME QUE CONSTA NA RESERVA:\n>>>")
                        data = input("DIGITE A DATA QUE CONSTA NA RESERVA:\n>>>")
                        horario = input("DIGITE O HORARIO QUE CONSTA NA RESERVA::\n>>>")
                        restaurante = input("DIGITE O RESTAURANTE QUE CONSTA NA RESERVA:\n>>>")
                        buscar_reserva(nome, data, horario, restaurante)
                    elif opcao == '6':
                        listar_reservas()
                    elif opcao == "7":
                        print("VOLTAR AO MENU ANTERIOR...")
                        sleep(3)
                        break
                    else:
                        print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
            case 3:
                print("🚀 SAINDO...")
                sleep(3)
                break
            case __:
                print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")

if __name__ == "__main__":
    main()