import Forca
import Game

def escolhe_jogo():
    print("**********************")
    print("Qual jogo você deseja?")
    print("**********************")

    print("(1) Forca (2) Advinhação")

    jogo = int(input("Qual jogo você escolhe?"))

    if(jogo ==1):
        print("Jogando Forca!")
        Forca.jogar()
    elif(jogo == 2):
        print("Jogando Advinhação!")
        Game.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
