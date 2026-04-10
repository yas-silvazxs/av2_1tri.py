import advinhacao
import forca

while True:
    print("=== MENU PRINCIPAL ===")
    print("1 - Adivinhação")
    print("2 - Força")
    print("3 - Sair")
    
    opcao = int(input("Escolha uma opção (1-3): "))
    
    if opcao == 1:
        advinhacao.jogar()
    elif opcao == 2:
        forca.jogar()
    elif opcao == 3:
        print(" Até logo!")
        break
    else:
        print(" Opção inválida!")
    
    input("\nPressione Enter para continuar...")
