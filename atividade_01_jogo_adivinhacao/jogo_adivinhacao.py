import random

# 1. PREPARAÇÃO
numero_sorteado = random.randint(1, 100)
palpites = []

# 2. REPETIÇÃO (LOOP)
while True:
    palpite = int(input("Digite seu palpite (entre 1 e 100): "))
    palpites.append(palpite)  # Armazena o palpite na lista
    
    # 3. VERIFICAÇÃO DO PALPITE
    if palpite < numero_sorteado:
        print("O número sorteado é maior")
    elif palpite > numero_sorteado:
        print("O número sorteado é menor")
    else:
        print("Parabéns! Você acertou!")
        break  # Interrompe o loop quando o jogador acerta

# 4. ESTATÍSTICAS
total_tentativas = len(palpites)
maior_palpite = max(palpites)
menor_palpite = min(palpites)
media_palpites = sum(palpites) / total_tentativas

print("\n=== Estatísticas da Partida ===")
print(f"1. Quantidade de tentativas: {total_tentativas}")
print(f"2. Palpites informados: {palpites}")
print(f"3. Maior palpite: {maior_palpite}")
print(f"4. Menor palpite: {menor_palpite}")
print(f"5. Média dos palpites: {media_palpites:.2f}")
