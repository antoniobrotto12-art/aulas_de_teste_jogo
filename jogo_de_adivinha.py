import random

print("=== Adivinhe o Número ===\n")

# Gerando o número secreto entre 1 e 100
secreto = random.randint(1, 100)
tentativas = 0
palpite = 0

while palpite != secreto:
    palpite = int(input("Seu palpite (1-100): "))
    tentativas += 1  # Incrementa o número de tentativas
    
    if palpite < secreto:
        print("Muito baixo!")
    elif palpite > secreto:
        print("Muito alto!")
    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativas!")
