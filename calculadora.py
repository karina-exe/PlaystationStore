valor = float(input("Digite o valor: "))




if valor < 200:
   valor1 = 5 / 100 * valor
   result1 = valor - valor1
   print("Você ganhou 5% de desconto!")
   print(f"Portanto, o valor de sua compra foi de {result1:2f}")

elif valor >= 200 and valor <= 300:
     valor2 = 10 / 100 * valor
     result2 = valor - valor2
     print("Você ganhou 10% de desconto!")
     print(f"Portanto, o valor de sua compra foi de {result2:.2f}")

elif valor >= 300:
     valor3 = 15 / 100 * valor
     result3 = valor - valor3
     print("Você ganhou 15% de desconto!")
     print(f"Portanto, o valor de sua compra foi de {result3:.2f}")

else:
    print("sem desconto, si lascou")

