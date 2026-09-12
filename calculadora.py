#IMPORTANTE: Comentários adicionais ao fim do código.
#RESUMO DO ALGORITMO: Programa com três estruturas dividido em:
#Dois Input;
#Um Processing;
#Três Output.

#Input 01: Idade do usuário para que a primeira condição estabelecida (if/else) seja executada.

print("Seja bem-vindo(a) ao sistema de desconto da Playstation®Store.")
print("Em comemoração aos 31 anos da Playstation®, estamos oferecendo descontos* especiais "
      "para nossos usuários.")
print("Os descontos serão aplicados de acordo com o valor da sua compra.")
print("*Apenas para compras até R$400.00, variando conforme valores pré-estabelecidos.")
idade = int(input("Antes de prosseguir, insira sua idade: "))

#Processing: Estrutura condicional para estabelecer se o usuário está de acordo
#com a política de compra da Playstation Store.
#Maior de idade = True
#portanto, prossegue com o desconto. O Input 02 é permitido (valor da compra).
#Menor de idade = False
#portanto, não prossegue com o desconto. Output 01 é mostrado.

if idade < 18:
    #Output 01: Mensagem de justificativa.
    print("Desculpe, você não possui o requisito necessário para receber o desconto.")
    print("O Controle Parental não permite que usuários menores de idade efetuem compras.")
    print("Consulte o Manual do Usuário para mais informações.")
    import sys
    sys.exit()

else:
    #Input 02: Valor da compra para que o cálculo seja executado.
    valor = float(input("Digite o valor da sua compra: "))

#Processing: Cálculos executados com o auxílio da instrução "def" para evitar repetições
#dentro das três estruturas condicionais (if/elif/else). Uma simples fórmula de % (divisão
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

#Output 02: Saída dos resultados dos valores do desconto, junto com o valor final da compra, na
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

#Output 03: Mensagem simples de saída, para estabelecer o fim do programa.

print("A Playstation® agradece sua preferência.")

#Comentários adicionais:

#01. Decidi impor um limite de compra até R$400, pois sem o limite, o programa jamais iria
#retornar a mensagem de "else" e obviamente eu gostaria que essa mensagem aparecesse em algum momento,
#ao testar todas as possibilidades possíveis.

#02. Decidi estabelecer uma condição extra: somente usuários maiores de idade podem prosseguir com a
#compra, sendo aptos para receber o desconto. Se o usuário for menor de idade, o programa é encerrado com
#uma mensagem. Para não gerar nenhum bug, descobri através de um fórum de ajuda que, se eu adicionasse
#'import sys sys.exit()', o script "if" da primeira estrutura condicional encerraria sem prejudicar o resto do código.

#03. Fazia um tempo que eu estava curiosa sobre a instrução 'def / return' e sua funcionalidade, assim como
#ela faria sentido dentro de um código. Após rever uma atividade que fiz no curso introdutório de Python, pela
#Fundação Bradesco, decidi copiar a sintaxe da instrução e intuitivamente, fui construindo a lógica por trás
#dos cálculos. Fico feliz que tenha dado certo. :)
