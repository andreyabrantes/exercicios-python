import random

def adivinhe_o_numero():
    # Escolhe um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False
    
    print("Bem-vindo ao jogo de adivinhar o número!")
    print("Tente adivinhar o número entre 1 e 100.")
    
    while not acertou:
        try:
            # Recebe o palpite do jogador
            palpite = int(input("Digite seu palpite: "))
            
            # Incrementa o número de tentativas
            tentativas += 1
            
            # Verifica se o palpite está correto
            if palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                acertou = True
        
        except ValueError:
            print("Por favor, digite um número válido.")
    
# Chama a função para iniciar o jogo
adivinhe_o_numero()
