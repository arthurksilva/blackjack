import random

def cards():
    cont_negativo = 1
    qtd_de_passadas = 0
    cards_typs = [
        ["Card 2", 2],
        ["Card 3", 3],
        ["Card 4", 4],
        ["Card 5", 5],
        ["Card 6", 6],
        ["Card 7", 7],
        ["Card 8", 8],
        ["Card 9", 9],
        ["Card 10", 10],
        ["Valete", 10],
        ["Dama", 10],
        ["Rei", 10],
        ["ÁS", 11]  # Adicionei o valor 11 para o ÁS
    ]
    
    random_cards = random.randint(0, 12) 
    card_valor = cards_typs[random_cards]
    return card_valor

cards_do_usuario = []
cont = 1

for i in range(0,2):
    card = cards()
    nome_do_cartao = card[0]  # Obtém o nome do cartão
    valor_do_cartao = card[1]  # Obtém o valor do cartão
    cards_do_usuario.append((valor_do_cartao))


opecao = input("Você deseja jogar BLACKJACK? S/N").lower()

print("Cartas sorteadas:")
for valor in cards_do_usuario:
    print(f"{valor}")

if opecao == "s":
    cont = 1
else:
    cont = 0

while cont == 1:
    hit = int(input("Puxar uma CARTA? (1 para HIT, 0 para parar)"))
    if hit == 1:
        card = cards()  # Sorteie uma carta
        cards_do_usuario.append((valor_do_cartao))  # Adiciona a carta à lista
    else:
        cont = 0

# Exibir as cartas sorteadas
print("Cartas sorteadas:")
for valor in cards_do_usuario:
    print(f"{valor}")