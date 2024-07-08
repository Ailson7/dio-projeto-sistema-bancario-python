import random

def gerar_jogos(quantidade):
    jogos = []
    for _ in range(quantidade):
        jogo = sorted(random.sample(range(1, 61), 6))
        jogos.append(jogo)
    return jogos

def main():
    try:
        quantidade = int(input("\nInforme a quantidade de apostas que deseja realizar: "))
        if quantidade <= 0:
            raise ValueError("\nA quantidade deve ser um número positivo.")
    except ValueError as e:
        print(f"Erro: {e}")
        return
    
    print ("\n============== APOSTA ===============")

    print (f"\nQuantidade de apostas geradas = {quantidade:.0f}")

    print("")

    jogos = gerar_jogos(quantidade)
    for idx, jogo in enumerate(jogos, start=1):
        print(f"Aposta {idx}: {jogo}")

    print("\nBoa sorte!")
    print("")

if __name__ == "__main__":
    main()

