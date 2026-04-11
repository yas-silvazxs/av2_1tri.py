import random

def jogar():
    # menu de opções usando o terminal
    while(True):
        print("menu de dificuldades")

        print("1 - facil")
        print("2 - medio")
        print("3 - dificil")
        print("4 - voltar/sair")
        opcao = int(input("Digite a opção desejada (1 a 4)"))

        if opcao == 1:
            print( " voce seleciono o Fácil")
            sorteio_max = 10
            tentativas_max = 5
        elif opcao == 2:
            print( " voce selecionado o Médio"  )
            sorteio_max = 50
            tentativas_max = 10
        elif opcao == 3:
            print("voce selecionado o Difícil")
            sorteio_max = 100
            tentativas_max = 12
        elif opcao == 4:
            break
        else:
            print("Opção inválida, sselecionado o modo facil ")
            sorteio_max = 10
            tentativas_max = 5

        # Configurações do jogo
        tentativas = 1
        errou = True
        
        numero = random.randint(0,sorteio_max)


        while (tentativas <= tentativas_max):
            print("Tentativa:", tentativas)
            chute = int(input(f"Digite o seu chute (0 a {sorteio_max}):"))
            if chute == numero:
                print("Parabéns, você é o bonzão mesmo")
                errou = False
                break
            else:
                print("Errou :c")
                if numero > chute:
                    print("o numero sorteado e maior que o chute")
                else:
                    print("o numero sorteado e menor que o chute")

            tentativas = tentativas + 1
            
        if errou == True:
            print("O número sorteado era:", numero) # mostra p quem errou
        print("### FIM DO JOGO ###")

if(__name__ == "__main__"):
    jogar()
       
