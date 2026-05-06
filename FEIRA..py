print("=== Carrinho da Feira ===\n")

total = 0
carrinho = []

while True:
    item = input("Item (ou 'sair' para finalizar): ").strip()
    
    if item.lower() == 'sair':
        break
        
    preco = float(input(f"Preço do {item}: R$ "))
    qtd = int(input("Quantidade: "))
    
    # Cálculo do subtotal (preço vezes quantidade)
    subtotal = preco * qtd
    total += subtotal
    
    # Adicionando à lista do carrinho com formatação de 2 casas decimais
    carrinho.append(f"{qtd}x {item} - R$ {subtotal:.2f}")

print("\n=== Seu Carrinho ===")
for i in carrinho:
    print(i)

print("-" * 20)
print(f"Total a pagar: R$ {total:.2f}")
