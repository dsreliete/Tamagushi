import time
from tamagushi import *

def estatisticas():
    print("")
    print("Estatísticas de {0}:".format(tg.nome))
    print("Fome: {0}%".format(tg.fome))
    print("Saúde: {0}%".format(tg.saude))

def menu():
    print("")
    print("Selecione uma opção:")
    print("1 - Alimentar")
    print("2 - Cuidar")
    print("3 - Mudar nome")
    print("4 - Ver humor")
    print("0 - Sair")

tg = Tamagushi()
op = 1
print("{0}".format(bichinho))

while (op != 0):
    estatisticas()
    menu()
    op = int(input("\n"))
    if op == 1:
        tg.alimentar()
    elif op == 2:
        tg.cuidar()
    elif op == 3:
        nome = input("Qual será meu novo nome? ")
        tg.alterar_nome(nome)
    elif op == 4:
        tg.calcula_humor()
        time.sleep(2)

print("Até mais! :3")
