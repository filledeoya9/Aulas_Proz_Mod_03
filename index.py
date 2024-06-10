produto = input ("Informe o nome do produto:")
preco = input ("Informe o preço do produto:")

def classifica_preco(valor):
  valor= float(valor)
  if valor > 100:
      print ("Caro")
  elif valor >=50 and valor <=100:
      print("Médio")
  else:
      print ("Baixo")
classifica_preco(preco)