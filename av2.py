import random

def jogar():
    palavras = []

    print("1 - jogos ")
    print("2 - carros ")
    print("3 - animais 3")
    print("4 - Sair")
    opcao = int(input("Digite a opção desejada (1 a 4): "))

    if opcao == 1:
        print("Selecionado opção 1")
        arquivo = open("jogos.txt", "r")
    elif opcao == 2:
        print("Selecionado opção 2")
        arquivo = open("carros.txt", "r")
    elif opcao == 3:
        print("Selecionado opção 3")
        arquivo = open("animais.txt", "r")
    else:
        arquivo = open("carros.txt", "r")
        print("selecionado carros, bom jogo")
    
    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()
    palavra = random.choice(palavras)

    letras_acertadas = []
    for letra in palavra:
        letras_acertadas.append("_")

    acertou = False
    enforcou = False
    erros = 0 
    MAX_ERROS = 6  
    tentativa = 1

    def mostrar_letras_acertadas():
        for letra in letras_acertadas:
            print(letra, end=" ")
        print(f"\nErros: {erros}/{MAX_ERROS}")

    def desenhar_enforcado():
        """Desenha o enforcado baseado no número de erros"""
        boneco = [
            """
              -----
              |   |
                  |
                  |
                  |
                  |
            =========
            """,
            """
              -----
              |   |
              O   |
                  |
                  |
                  |
            =========
            """,
            """
              -----
              |   |
              O   |
              |   |
                  |
                  |
            =========
            """,
            """
              -----
              |   |
              O   |
             /|   |
                  |
                  |
            =========
            """,
            """
              -----
              |   |
              O   |
             /|\\  |
                  |
                  |
            =========
            """,
            """
              -----
              |   |
              O   |
             /|\\  |
             /    |
                  |
            =========
            """,
            """
              -----
              |   |
              O   |
             /|\\  |
             / \\  |
                  |
            =========
            ENFORCADO!
            """
        ]
        print(boneco[erros])

    print("Tente adivinhar a palavra secreta!")
    print(f"A palavra tem {len(palavra)} letras")
    
    while(not acertou and not enforcou):
        desenhar_enforcado()
        mostrar_letras_acertadas()
        
        chute = input("\nDigite uma letra: ").lower()
        
        if len(chute) != 1 or not chute.isalpha():
            print("Digite apenas uma letra válida!")
            print("-" * 30)
            continue
            
        acertou_nessa_rodada = False
        indice = 0

      
        for letra in palavra:
            if chute == letra:
                letras_acertadas[indice] = letra
                acertou_nessa_rodada = True
            indice += 1
        
       
        if acertou_nessa_rodada:
            print(f" ÓTIMO! A letra '{chute}' está na palavra!")
        else:
            erros += 1
            print(f" ERRO! A letra '{chute}' NÃO está na palavra!")
        
        
        if erros >= MAX_ERROS:
            desenhar_enforcado()
            print(f"\n VOCÊ FOI ENFORCADO! A palavra era: {palavra}")
            print(f"Você fez {erros} erros!")
            enforcou = True

        
        if letras_acertadas.count("_") == 0:
            print("\n PARABÉNS! Você acertou a palavra secreta!")
            mostrar_letras_acertadas()
            print(f" Você venceu em {tentativa} tentativas com apenas {erros} erros!")
            acertou = True

        tentativa += 1
        print("-" * 40)  


jogar()
