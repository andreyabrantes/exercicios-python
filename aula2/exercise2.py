#ESCREVA UM PROGRAMA QUE LEIA UMA LISTA DE NÚMEROS INTEIROS E EXIBA-OS EM ORDEM CRESCENTE.

def main():
    # Pergunta ao usuário quantos números ele vai inserir
    try:
        quantidade = int(input("Quantos números você deseja inserir? "))
        if quantidade <= 0: 
            print("A quantidade de números deve ser um número inteiro positivo.")
            return
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        return

    # Inicializa uma lista para armazenar os números
    lista = []

    # Lê os números do usuário
    for i in range(quantidade):
        while True:
            try:
                numero = int(input(f"Digite o número {i + 1}: "))
                lista.append(numero)
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")

    # Ordena a lista em ordem crescente
    lista.sort(reverse=True)

    # Exibe os números em ordem crescente
    print("Números em ordem crescente:")
    for numero in lista:
        print(numero)

if __name__ == "__main__":
    main()
