print('Bem vindo a Lanchonete do Leonardo Estigarribia Sila')
print('************** Cardápio ************** ')

produtos = {
    "100": {"nome": "Cachorro Quente", "preco": 9.00},
    "101": {"nome": "Cachorro Quente Duplo", "preco": 11.00},
    "102": {"nome": "X - Egg", "preco": 12.00},
    "103": {"nome": "X - Salada", "preco": 12.00},
    "104": {"nome": "X - Bacon", "preco": 14.00},
    "105": {"nome": "X - Tudo", "preco": 17.00},
    "200": {"nome": "X - Refrigerante Lata", "preco": 5.00},
    "201": {"nome": "X - Chá Gelado", "preco": 4.00},
}

for cod, produto in produtos.items():
    nome, preco = produto.values()
    print(f"{cod} | {nome}, |R${preco:.2f}|")

valor_total: list[float] = []
continuar = True

while continuar:
    cod = str(input("\nEntre com o codigo desejado: "))

    if produto := produtos.get(cod):
        nome, preco = produto.values()
        print(f"{nome} adicionado na sacola.")
        valor_total.append(preco)
    else:
        print("Código não existe.")
        continue

    while True:
        res = str(input(("\nVocê deseja adicionar mais um item na sacola? \nSIM - 1 \nNÃO - 2\n> ")))

        if (res == "1"):
            break

        if (res == "2"):
            continuar = False
            break

        else:
            print("\nCódigo não existe.")
            continue

print("\nValor total: R${:.2f}".format(sum(valor_total)))
