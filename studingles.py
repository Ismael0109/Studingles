import time, random
from rich import print

def buscarPalavraIng(listaIngles):
    num = random.randint(651, len(listaIngles) - 1)
    return (listaIngles[num])

def buscarPalavraPort(listaPortugues):
    num = random.randint(651, len(listaPortugues) - 1)
    return (listaPortugues[num])

def traduzirParaIng(listaIngles,listaPortugues, palavraPort):
    indice = listaPortugues.index(palavraPort)
    return listaIngles[indice]

def traduzirParaPort(listaIngles,listaPortugues, palavraIng):
    indice = listaIngles.index(palavraIng)
    return listaPortugues[indice]

def realizarAcoes(idioma, listaIngles, listaPortugues, palavra):
    if(idioma == 1):
        palavra = buscarPalavraIng(listaIngles)
        traducao = traduzirParaPort(listaIngles, listaPortugues, palavra)
    else:
        palavra = buscarPalavraPort(listaPortugues)
        traducao = traduzirParaIng(listaIngles, listaPortugues, palavra)
    print(f"[bold blue]{palavra}[/bold blue]")
    print()
    prosseguir = input("Prosseguir: ")
    if(prosseguir == ""):
        print(f"[bold]{palavra}[/bold] -> [bold blue]{traducao}[/bold blue]")
    else:
        print(f"[bold]{palavra}[/bold] -> [bold blue]{traducao}[/bold blue]")
            
            
listaIngles = []
with open("words.txt", "r", encoding="utf-8") as wordsTxt:
    linhasIng = []
    for linhaIng in wordsTxt:
        linhaIng_Formatada = linhaIng.strip()
        listaIngles.append(linhaIng_Formatada)

listaPortugues = []
with open("palavras.txt", "r", encoding="utf-8") as palavrasTxt:
    linhasPort = []
    for linhaPort in palavrasTxt:
        linhaPort_Formatada = linhaPort.strip()
        listaPortugues.append(linhaPort_Formatada)

palavra = ""
opcao = 0
while(opcao != 3):
    print("[bold blue]=========== Studingles ===========[/bold blue]")
    time.sleep(0.5)
    print("1 - INGLÊS")
    time.sleep(0.2)
    print("2 - PORTUGUÊS")
    time.sleep(0.2)
    print("3 - SAIR")
    print()
    time.sleep(0.5)
    
    opcao = int(input("Escolha uma Opção: "))
    time.sleep(0.5)
    
    if(opcao == 1):
        realizarAcoes(1, listaIngles, listaPortugues, palavra)
        continue
    elif(opcao == 2):
        realizarAcoes(2, listaIngles, listaPortugues, palavra)
        continue
    elif(opcao == 3):
        print()
        print("VOCÊ SAIU DO PROGRAMA!!!!")
        break
    else:
        print()
        print("Valor Inválido")
        continue