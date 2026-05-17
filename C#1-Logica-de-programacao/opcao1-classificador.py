niveis = {
  "Ferro": [0, 1000],
  "Bronze": [1001, 2000],
  "Prata": [2001, 5000],
  "Ouro": [5001, 7000],
  "Platina": [7001, 8000],
  "Ascendente": [8001, 9000],
  "Imortal": [9001, 10000]
}

nomeDoHeroi = input("Nome do Heroi: ")
nivelAlcancado = ""


while True:
  try:
    vida = int(input("Vidas do Heroi: "))
    if vida > 10000:
      nivelAlcancado = "Radiante"
      print(f"O Herói de nome {nomeDoHeroi} está no nível de {nivelAlcancado}")
    else:
      for nivel, xp in niveis.items():
        nivelAlcancado = nivel if vida>=xp[0] and vida<=xp[1] else nivelAlcancado
        
        if nivelAlcancado == nivel:
          print(f"O Herói de nome {nomeDoHeroi} está no nível de {nivelAlcancado}")

    break

  except ValueError:
    print("Entre com um valor inteiro.")