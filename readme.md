# 🖤Calculadora de descontos  — Playstation Store🖤

<img src="https://i.ibb.co/Gw85ZBG/playstation-store2.gif" alt="Banner" width="100%">


A calculadora foi desenvolvida para aplicar descontos para usuários que efetuam compras 
na Playstation Store, de acordo com os valores estabelecidos, sendo:

- 5% de desconto em compras no valor igual ou abaixo de R$200;
- 10% de desconto em compras no valor acima de R$$200 e abaixo de R$300;
- 15% de desconto em compras no valor acima de R$300.

<b>Adendo:</b> Como o programa usava a condição <b>IF/ELIF/ELSE</b>, decidi impor um limite
de R$400 para receber o desconto de 15%, se não, a mensagem "else" não iria retornar, 
o que faria com que o uso de "else" fosse inútil.

# 🖤Condição extra —  idade🖤

O programa irá calcular os descontos <b>SE</b> o usuário for maior de idade, <b>SENÃO</b>, uma
mensagem retorna explicando o motivo pelo qual o cálculo foi recusado, sendo os parâmetros:

- Maior de idade (=>18) = True
- Menor de idade (<18)  = False
- True: Tem a idade necessária, portanto, o sistema irá calcular o desconto.
- False: Não tem a idade necessária e isso vai contra o Controle Parental, portanto, o 
sistema não irá calcular o desconto.

# 🖤Algoritmo🖤

- Mensagem inicial
- Input idade
- Análise da idade
- SE menor de idade: fora
- Mensagem de justificativa
- SE NÃO: dentro
- Input valor da compra
- Fórmula: desconto / 100 * valor da compra
- Calcular descontos: 5% SE =<200
- Mensagem de aprovação
- Mensagem de agradecimento
- Calcular descontos: 10% SE NÃO, SE =>200 e <=300
- Mensagem de aprovação
- Mensagem de agradecimento
- Calcular descontos: 15% SE NÃO, SE >=300 e <=400
- Mensagem de aprovação
- Mensagem de agradecimento
- SE NÃO: não calcular descontos
- Mensagem de justificativa

# 🖤Instruções de uso🖤
<p><b>Desktop:</b></p>

- Fazer o download do arquivo do script e abri-lo em qualquer IDE (VS Code, Pycharm, etc) ou no Python.

<p><b>Smartphone:</b></p>

- Android: Fazer download do script e abrir com o app Pydroid 3.
- iOS: Fazer o download do script e abrir com o app Pythonista.

Obs: Para fazer o download do script, basta abrir "calculadora.py" e clicar em "download raw file".

 # 🖤Ferramentas utilizadas🖤


- <img align="center" alt="karina-exe" height="50" width="50" src="https://devicon-website.vercel.app/api/python/plain.svg?color=%23000000">
- <img align="center" alt="karina-exe" height="50" width="50" src="https://devicon-website.vercel.app/api/pycharm/plain.svg?color=%23000000">
- <img align="center" alt="karina-exe" height="50" width="50" src="https://devicon-website.vercel.app/api/git/plain.svg?color=%23000000">
- <img align="center" alt="karina-exe" height="50" width="50" src="https://64.media.tumblr.com/845f35d211b70c90cfd89976ee29b858/6fc7e20c4e3f102b-a5/s2048x3072/f69d08a67fdaefea6225bf13e7c53af7d9239418.pnj">  
- <img align="center" alt="karina-exe" height="50" width="50" src="https://devicon-website.vercel.app/api/photoshop/plain.svg?color=%23000000">