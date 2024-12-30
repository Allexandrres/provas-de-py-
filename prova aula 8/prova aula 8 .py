import os

def listar_diretorio_atual():
    itens = os.listdir()
    
    print("Arquivos e pastas no diretório atual:")
    for item in itens:
        print(item)

listar_diretorio_atual()
