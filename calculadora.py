#IMPORTANTE: Comentários adicionais ao fim do código.

#Input 01: O primeiro input para determinar se o usuário tem a idade necessária
#para ganhar os descontos.

print("Seja bem-vindo(a) ao sistema de desconto da Playstation®Store.")
print("Em comemoração aos 31 anos da Playstation®, estamos oferecendo descontos especiais"
      "para nossos usuários.")
print("Os descontos serão aplicados de acordo com o valor da sua compra.")
idade = int(input("Antes de prosseguir, insira sua idade: "))

#Input 02: Estrutura condicional para estabelecer se o usuário está de acordo
#com a política de compra da Playstation Store.

if idade <= 18:
    print("Desculpe, você não possui o requisito necessário para o receber desconto.")
    print("O Controle Parental não permite que usuários menores de idade efetuem compras.")
    print("Consulte o Manual do Usuário para mais informações.")
    import sys
    sys.exit()

else:
    valor = float(input("Digite o valor da sua compra: "))

#Processing e Output das infos: Os cálculos juntamente com as estruturas condicionais if, elif, else.
#Uma simples fórmula de porcentagem (divisão de dois valores numéricos e multiplicação com o desconto)
#para determinar o valor final da compra.


if valor < 200:
   valor1 = 5 / 100 * valor
   result1 = valor - valor1
   print("A sua compra se qualifica para ganhar 5% de desconto.")
   print(f"Valor do desconto: R${valor1:.2f}.")
   print(f"Valor total da compra com o desconto incluso: R${result1:.2f}.")

elif valor >= 200 and valor < 300:
     valor2 = 10 / 100 * valor
     result2 = valor - valor2
     print("A sua compra se qualifica para ganhar 10% de desconto.")
     print(f"Valor do desconto: R${valor2:.2f}.")
     print(f"Valor total da compra com o desconto incluso: R${result2:.2f}.")

elif valor >= 300 and valor < 400:
     valor3 = 15 / 100 * valor
     result3 = valor - valor3
     print("A sua compra se qualifica para ganhar 15% de desconto.")
     print(f"Valor do desconto: R${valor3:.2f}.")
     print(f"Valor total da compra com o desconto incluso: R${result3:.2f}.")

else:
    print("Infelizmente sua compra não se qualifica para o desconto.")

#Output: Mensagem simples de saída, para estabelecer o fim do programa.

print("A Playstation® agradece sua preferência.")

#Comentários adicionais:
#
#01. Decidi impor um limite de compra até R$400, pois sem o limite, o programa jamais iria
#retornar a mensagem de "else" e obviamente eu gostaria que essa mensagem aparecesse em algum momento.

#02. Decidi estabelecer uma nova condição: somente usuários maiores de idade podem prosseguir com a
#compra, sendo aptos para receber o desconto. Devido a isso, se o usuário for menor de idade, o
#programa é encerrado com uma mensagem. Para não gerar nenhum bug, descobri em um fórum de ajuda que,
#se eu colocasse 'import sys sys.exit() o programa encerraria, sem prejudicar o resto do código.