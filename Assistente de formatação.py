#Assistente de formatação
#versão alpha
#Objetivo: Já pensou em ter um programa que te auxilia a instalar programas da internet de forma mais rápida e facil do que ir em varios sites diferentes para baixar os aplixativos?
#Este projeto tenta resolver este problema alem de ser um jeito de me desenvolver em python :)
Versao ="v0.0.1"

#Aqui eu importo as bibliotecas que vou usar no projeto
import os

#Futuramente modo escuro
Darkmode = 1

#Limpar a tela
os.system(command="cls")

#Aqui eu carrego alguns textos que vou exibir ao longo do progrma.
Linha1 = "Assistente de formatação "+Versao

#Definindo o que é o menu
def ErroMenu():
    os.system(command="cls")
    if Darkmode == 1:
        os.system(command="color 04")
    else:
        os.system(command="color 74")
    print(Linha1)
    print()
    print("Poxa algo deu errado")
    input("Aperte ENTER para voltar ao menu anterior")
    Menu()

def Menu():
    os.system(command="cls")
    if Darkmode == 1:
        os.system(command="color 03")
    else:
        os.system(command="color 73")
    print(Linha1)
    print()
    print("Menu")
    print("O que deseja fazer?")
    print("1 - Instalar um programa")
    print("0 - Sair")
    print("Mais opções em breve")

    OpcaoMenu = input("Escolha um número referente a opção e aperte ENTER: ")

    if OpcaoMenu == 0:
        os.system(command="exit")
    elif OpcaoMenu == 1:
        ErroMenu()
    else:
        ErroMenu()

Menu()