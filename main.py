print("Ola Mundo")
Nome = input("Qual é o seu nome?")
print("olá", Nome)

Idade = input("Qual é a sua idade?")
if int(Idade) > 18:
  print("Você é adulto")
else: 
  print("Você é adolescente")

ano = input("Em que ano você nasceu?")
if int(ano) > 2000:
 print("Você é da geração Z")
else:
 print("Você é da geração X")

Altura = input("Qual sua altura?")
if int(Altura) > 170:
  print("Você é alto")
else:
  print("Você é baixo")

mora = input("Você mora sozinho? S/N")
if mora == "S":
  print("Legal!!!!")
else:
  print("Legal")

peso = input("Qual seu peso?")
if int(peso) > 70:
  print("Você é gordo")
else:
  print("Você é magro")