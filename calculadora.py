#IMPORTANTE: Comentários adicionais ao fim do código.

#Input 01: Idade do usuário para que a primeira condição (if/else) seja executada.

print("Seja bem-vindo(a) ao sistema de desconto da Playstation®Store.")
print("Em comemoração aos 31 anos da Playstation®, estamos oferecendo descontos* especiais "
      "para nossos usuários.")
print("Os descontos serão aplicados de acordo com o valor da sua compra.")
print("*Apenas para compras até R$400.00, variando conforme valores pré-estabelecidos.")
idade = int(input("Antes de prosseguir, insira sua idade: "))

#Input 02: Estrutura condicional para estabelecer se o usuário está de acordo
#com a política de compra da Playstation Store.
#Maior de idade = True, portanto, prossegue com o desconto;
#Menor de idade = False, portanto, não prossegue com o desconto.

if idade < 18:
    print("Desculpe, você não possui o requisito necessário para receber o desconto.")
    print("O Controle Parental não permite que usuários menores de idade efetuem compras.")
    print("Consulte o Manual do Usuário para mais informações.")
    import sys
    sys.exit()

else:
    valor = float(input("Digite o valor da sua compra: "))

#Processing: Cálculos executados com o auxílio da instrução de "def" para evitar repetições
#dentro das três estruturas condicionais (if, elif, else). Uma simples fórmula de % (divisão
#de dois valores numéricos e multiplicação com o desconto) para determinar o valor final da compra.

def desconto():
    return 5 / 100 * valor
resultado = valor - desconto()

def desconto2():
    return 10 / 100 * valor
resultado2 = valor - desconto2()

def desconto3():
    return 15 / 100 * valor
resultado3 = valor - desconto3()

#Output: Saída ds resultados dos valores do desconto, junto com o valor final da compra, na
#estrutura condicional (if/elif/else) e mensagem do resultado aplicado para o usuário.

if valor < 200:
   print("Oba! Você foi contemplado com um desconto de 5%!")
   print(f"Valor do desconto: R${desconto():.2f}")
   print(f"Valor total da compra com o desconto incluso: R${resultado:.2f}")


elif valor >= 200 and valor < 300:
     print("Uau! Você foi contemplado com um desconto de 10%!")
     print(f"Valor do desconto: R${desconto2():.2f}")
     print(f"Valor total da compra com o desconto incluso: R${resultado2:.2f}")

elif valor >= 300 and valor < 400:
     print("Parabéns! Você foi contemplado com um desconto de 15%!")
     print(f"Valor do desconto: R${desconto3():.2f}")
     print(f"Valor total da compra com o desconto incluso: R${resultado3:.2f}")

else:
    print("Infelizmente sua compra não se qualifica para o desconto.")
    print("O valor da sua compra excede o limite para o desconto.")
    import sys

    sys.exit()

#Output: Mensagem simples de saída, para estabelecer o fim do programa.

print("A Playstation® agradece sua preferência.")

#Comentários adicionais:
#
#01. Decidi impor um limite de compra até R$400, pois sem o limite, o programa jamais iria
#retornar a mensagem de "else" e obviamente eu gostaria que essa mensagem aparecesse em algum momento.

#02. Decidi estabelecer uma nova condição: somente usuários maiores de idade podem prosseguir com a
#compra, sendo aptos para receber o desconto. Devido a isso, se o usuário for menor de idade, o
#programa é encerrado com uma mensagem. Para não gerar nenhum bug, descobri através de um fórum de ajuda que,
#se eu colocasse 'import sys sys.exit() o programa encerraria, sem prejudicar o resto do código.

#03. Decidi incluir def return para testar se daria certo no meu código e deu. Acredito que isso simplificou
#o processamento dos cálculos.


