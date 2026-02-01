import json
from colorama import Fore
import chime
import os
import time

def carregar_tarefas(tarefas): #função para carregar os dados do json e colocar em uma lista
    try:
        with open(tarefas, "r", encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    
def salvar_tarefas(tarefas, dados): #função para salvar as alterações da lista no json
    with open(tarefas, "w", encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

def limpar_tela(): #função para limpar a tela após um segundo
    time.sleep(1)
    os.system('cls')

tarefas = carregar_tarefas("tarefas.json")
chime.theme('material')

while True:
    print(Fore.CYAN +"LISTA DE TAREFAS\n")
    print(Fore.GREEN +"[1]" + Fore.BLUE + " - ADICIONAR TAREFA")
    print(Fore.GREEN +"[2]" + Fore.BLUE + " - MARCAR TAREFA COMO CONCLUÍDA")
    print(Fore.GREEN +"[3]" + Fore.BLUE + " - REMOVER TAREFAS")
    print(Fore.GREEN +"[4]" + Fore.BLUE + " - MOSTRAR TODAS AS TAREFAS")
    print(Fore.GREEN +"[5]" + Fore.BLUE + " - SAIR DO SISTEMA\n")
    
    #tenta executar o programa principal
    try:
        opcao_usuario = int(input(Fore.LIGHTGREEN_EX + "Digite a opção: ")) #recebe a opção do usuário
        match opcao_usuario: #semelhante ao switch case para evitar vários IF e ELSE
            case 1:
                os.system('cls') 
                nome_tarefa = input(Fore.LIGHTGREEN_EX +"Digite a tarefa: ")
                status_tarefa = False
                tarefas.append([nome_tarefa, status_tarefa]) #adiciona a tarefa a lista e coloca o status como falso
                try:
                    salvar_tarefas("tarefas.json", tarefas) #chama a função para guarda a lista em um json
                    print("Arquivo salvo com sucesso!")
                    limpar_tela()
                except FileExistsError:
                    print(Fore.RED+"Erro ao salvar o arquivo!")
                    chime.error()
                    limpar_tela()
            
            case 2:
                os.system('cls')
                if not tarefas:
                    chime.error()
                    print(Fore.RED + "A lista está vazia, adicione tarefas com a opção 1")
                    limpar_tela()
                else:
                    for i, tarefa in enumerate(tarefas): 
                        nome_tarefa = tarefa[0]
                        print(Fore.LIGHTBLUE_EX + f"{i} - {nome_tarefa}")
                    try:
                        opcao_usuario = int(input(Fore.LIGHTGREEN_EX + "Digite o número da tarefa que deseja marcar como concluída: ")) #recebe a opção do usuário
                        if tarefas[opcao_usuario][1] == True:
                            print("A tarefa já está como concluída")
                            chime.warning()
                            limpar_tela()
                        else:
                            tarefas[opcao_usuario][1] = True
                            print(Fore.BLUE + f"{tarefas[opcao_usuario][0]} foi concluída")
                            try:
                                salvar_tarefas("tarefas.json", tarefas)
                                print("Arquivo salvo com sucesso!")
                                chime.success()
                                limpar_tela()
                            except FileExistsError:
                                print(Fore.RED + "Erro ao salvar o arquivo!")
                                limpar_tela()
                    except ValueError:
                        print(Fore.RED + "Opção Inválida")

            case 3:
                os.system('cls')
                if not tarefas:
                    chime.error()
                    print(Fore.RED + "A lista está vazia, adicione tarefas com a opção 1")
                    limpar_tela()
                else:
                    for i, tarefa in enumerate(tarefas):
                        nome_tarefa = tarefa[0]
                        print(Fore.LIGHTBLUE_EX + f"{i} - {nome_tarefa}")
                    try:
                        opcao_usuario = int(input(Fore.LIGHTGREEN_EX + "Digite o número da tarefa que deseja remover: "))
                        tarefas.pop(opcao_usuario)
                        salvar_tarefas("tarefas.json", tarefas)
                        print(Fore.YELLOW + "Tarefa removida com sucesso!")
                        chime.success()
                        limpar_tela()
                    except ValueError:
                        chime.error()
                        print(Fore.RED + "Opção Inválida")
            
            case 4:
                os.system('cls')
                if not tarefas:
                    chime.error()
                    print(Fore.RED + "A lista está vazia, adicione tarefas com a opção 1")
                    limpar_tela()
                else:
                    for i, tarefa in enumerate(tarefas): 
                        nome = tarefa[0] 
                        if tarefa[1] == True:
                            status = 'Concluido'
                        else:
                            status = 'Pendente'
                        print(f"{i} - {nome} - [{status}]")
                    print()
            
            case 5:
                os.system("cls")
                print(Fore.GREEN + "Programa finalizado com sucesso!")
                chime.success()
                break

            case _:
                chime.error()
                print(Fore.RED + "Opção inválida")
                limpar_tela()
    except:
        print(Fore.RED + "Digite somente números")
        chime.error()