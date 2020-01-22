def jogar():
    print("***************************")
    print("Bem Vindo ao jogo de Forca!")
    print("***************************")

    palavra_secreta = "Banana"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("Qual a letra?")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Econtrei a letra {} na posição {}".format(letra, index))
            index = index + 1

        print("Jogando...")

    print("Fim de Jogo!")

if(__name__ == "__main__"):
    jogar()