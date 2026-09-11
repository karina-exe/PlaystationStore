valor = float(input("Digite o valor: "))

if valor < 200:
   valor1 = 5 / 100 * valor
   result1 = valor - valor1
   print("A sua compra se qualifica para ganhar 5% de desconto.")
   print(f"Valor do desconto {valor1:.2f}")
   print(f"Valor total da compra com o desconto incluso: {result1:.2f}")

elif valor >= 200 and valor < 300:
     valor2 = 10 / 100 * valor
     result2 = valor - valor2
     print("A sua compra se qualifica para ganhar 10% de desconto.")
     print(f"Valor do desconto {valor2:.2f}")
     print(f"Valor total da compra com o desconto incluso: {result2:.2f}")

elif valor >= 300 and valor < 400:
     valor3 = 15 / 100 * valor
     result3 = valor - valor3
     print("A sua compra se qualifica para ganhar 15% de desconto.")
     print(f"Valor do desconto {valor3:.2f}")
     print(f"Valor total da compra com o desconto incluso: {result3:.2f}")

else:
    print("Não tem desconto")