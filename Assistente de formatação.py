#Assistente de formatação
#versão alpha
#Objetivo: Já pensou em ter um programa que te auxilia a instalar programas da internet de forma mais rápida e facil do que ir em varios sites diferentes para baixar os aplixativos?
#Este projeto tenta resolver este problema alem de ser um jeito de me desenvolver em python :)
Versao ="v0.2.0"

#Aqui eu importo as bibliotecas que vou usar no projeto
import os

#Futuramente modo escuro
Darkmode = 1

#Limpar a tela
os.system(command="cls")

#Aqui eu carrego alguns textos que vou exibir ao longo do progrma.
Linha1 = "Assistente de formatação "+Versao
Linha2 = "by: Yuri1502 https://github.com/Yuri1502"

#Definindo o que é o menu de erro
def ErroMenu():
    os.system(command="cls")
    if Darkmode == 1:
        os.system(command="color 04")
    else:
        os.system(command="color 74")
    print(Linha1)
    print(Linha2)
    print()
    print("Poxa algo deu errado")
    input("Aperte ENTER para voltar ao menu anterior")
    Menu()

#Instalador de programas baseado no Winget do Windows
def instalador():
    os.system(command="cls")
    if Darkmode == 1:
        os.system(command="color 09")
    else:
        os.system(command="color 79")
    print(Linha1)
    print(Linha2)
    print()
    print("Instalador de aplicativos")
    print()
    print("O que deseja instalar?")
    print("--Navegadores--")
    print("1 - Google Chrome")
    print("2 - Mozilla Firefox")
    print("3 - Opera")
    print("4 - Opera GX")
    print("--Ferramentas--")
    print("5 - Discord")
    print("6 - GIMP")
    print("7 - Google Drive")
    print("8 - LibreOffice")
    print("9 - Oracle Virtual Box")
    print("10 - PowerToys")
    print("11 - SpeedTest")
    print("12 - Spotify")
    print("13 - TeamViewer")
    print("--Lojas de Jogos--")
    print("14 - Epic Games")
    print("15 - EA app")
    print("16 - Steam")
    print("17 - Ubisoft Conect")
    print("--Desinvolvimento de programas--")
    print("18 - Node.js")
    print("19 - Python 3.9")
    print("20 - Visual Studio 2022")
    print("21 - Visual Studio Code")
    print()
    print("0 - Voltar")
    print()
    print("Escolha um número referente a opção e aperte ENTER: ")
    print()

    #Escolhendo a opção
    OpcaoInstalador = input("")

    #Depois de definir a opção ira iniciar a instalação via Winget
    if OpcaoInstalador == "0":
        Menu()
    elif OpcaoInstalador == "1":
        print("Você escolheu instalar o aplicativo Google Chrome")
        os.system(command="winget install Google.Chrome")
        instalador()
    elif OpcaoInstalador == "2":
        print("Você escolheu instalar o aplicativo Mozilla Firefox")
        os.system(command="winget install Mozilla.Firefox")
        instalador()
    elif OpcaoInstalador == "3":
        print("Você escolheu instalar o aplicativo Opera")
        os.system(command="winget install Opera.Opera")
        instalador()
    elif OpcaoInstalador == "4":
        print("Você escolheu instalar o aplicativo Opera GX")
        os.system(command="winget install Opera.OperaGX")
        instalador()
    elif OpcaoInstalador == "5":
        print("Você escolheu instalar o aplicativo Discord")
        os.system(command="winget install Discord.Discord")
        instalador()
    elif OpcaoInstalador == "6":
        print("Você escolheu instalar o aplicativo GIMP")
        os.system(command="winget install GIMP.GIMP")
        instalador()
    elif OpcaoInstalador == "7":
        print("Você escolheu instalar o aplicativo Google Drive")
        os.system(command="winget install Google.GoogleDrive")
        instalador()
    elif OpcaoInstalador == "8":
        print("Você escolheu instalar o aplicativo LibreOffice")
        os.system(command="winget install TheDocumentFoundation.LibreOffice")
        instalador()
    elif OpcaoInstalador == "9":
        print("Você escolheu instalar o aplicativo Oracle Virtual Box")
        os.system(command="winget install Oracle.VirtualBox")
        instalador()
    elif OpcaoInstalador == "10":
        print("Você escolheu instalar o aplicativo PowerToys")
        os.system(command="winget install Microsoft.PowerToys")
        instalador()
    elif OpcaoInstalador == "11":
        print("Você escolheu instalar o aplicativo SpeedTest")
        os.system(command="winget install Ookla.Speedtest.Desktop")
        instalador()
    elif OpcaoInstalador == "12":
        print("Você escolheu instalar o aplicativo Spotify")
        os.system(command="winget install Spotify.Spotify")
        instalador()
    elif OpcaoInstalador == "13":
        print("Você escolheu instalar o aplicativo TeamViewer")
        os.system(command="winget install TeamViewer.TeamViewer")
        instalador()
    elif OpcaoInstalador == "14":
        print("Você escolheu instalar o aplicativo Epic Games")
        os.system(command="winget install EpicGames.EpicGamesLauncher")
        instalador()
    elif OpcaoInstalador == "15":
        print("Você escolheu instalar o aplicativo EA app")
        os.system(command="winget install ElectronicArts.EADesktop")
        instalador()
    elif OpcaoInstalador == "16":
        print("Você escolheu instalar o aplicativo Steam")
        os.system(command="winget install Valve.Steam")
        instalador()
    elif OpcaoInstalador == "17":
        print("Você escolheu instalar o aplicativo Ubisoft Conect")
        os.system(command="winget install Ubisoft.Connect")
        instalador()
    elif OpcaoInstalador == "18":
        print("Você escolheu instalar o aplicativo Node.js")
        os.system(command="winget install OpenJS.NodeJS")
        instalador()
    elif OpcaoInstalador == "19":
        print("Você escolheu instalar o aplicativo Python 3.9")
        os.system(command="winget install Python.Python.3.9")
        instalador()
    elif OpcaoInstalador == "20":
        print("Você escolheu instalar o aplicativo Visual Studio 2022")
        os.system(command="winget install Microsoft.VisualStudio.2022.Community")
        instalador()
    elif OpcaoInstalador == "21":
        print("Você escolheu instalar o aplicativo Visual Studio Code")
        os.system(command="winget install Microsoft.VisualStudioCode")
        instalador()
    else:
        ErroMenu()

#Ferramenta de desfragmentar a unidade dew disco C:
def desfragmentar():
    os.system(command="cls")
    if Darkmode == 1:
        os.system(command="color 0A")
    else:
        os.system(command="color 7A")
    print(Linha1)
    print(Linha2)
    print()
    print("Desfragmentar unidade C:")
    print("O que deseja fazer?")
    print("1 - Analizar")
    print("2 - Desfragmentar o Boot")
    print("3 - Desfragmentar Normal")
    print("4 - Desfragmentar Avançado")
    print("5 - Abrir defrag")
    print("0 - Voltar")
    print()
    print("Escolha um número referente a opção e aperte ENTER: ")
    print()

    #Escolhendo a opção
    OpcaoDesfrag = input("")

    #Depois de definir a opção ira iniciar a desfragmentaçãop conforme escolhido a opção
    if OpcaoDesfrag == "0":
        Menu()
    elif OpcaoDesfrag == "1":
        print("Você escolheu Analizar a unidade C")
        os.system(command="defrag c: /a")
        desfragmentar()
    elif OpcaoDesfrag == "2":
        print("Você escolheu Desfragmentar o Boot da unidade C")
        os.system(command="defrag c: /b")
        desfragmentar()
    elif OpcaoDesfrag == "3":
        print("Você escolheu Desfragmentar Normal a unidade C")
        os.system(command="defrag c: /d /u")
        desfragmentar()
    elif OpcaoDesfrag == "4":
        print("Você escolheu Desfragmentar Avançado a unidade C")
        os.system(command="defrag c: /h /u")
        desfragmentar()
    elif OpcaoDesfrag == "5":
        print("Você escolheu Abrir defrag da unidade C")
        os.system(command="start dfrgui.exe")
        desfragmentar()
    else:
        ErroMenu()


#Definindo o que é o menu
def Menu():
    os.system(command="cls")
    if Darkmode == 1:
        os.system(command="color 03")
    else:
        os.system(command="color 73")
    print(Linha1)
    print(Linha2)
    print()
    print("Menu")
    print("O que deseja fazer?")
    print("1 - Instalar um programa")
    print("2 - Atualizar os programas instalados")
    print("3 - Desfragmentar")
    print("0 - Sair")
    print()
    print("Escolha um número referente a opção e aperte ENTER:")
    OpcaoMenu = input("")

    if OpcaoMenu == "0":
        os.system(command="exit")
    elif OpcaoMenu == "1":
        instalador()
    elif OpcaoMenu == "2":
        os.system(command="winget upgrade --all")
    elif OpcaoMenu == "3":
        desfragmentar()
    else:
        ErroMenu()

Menu()