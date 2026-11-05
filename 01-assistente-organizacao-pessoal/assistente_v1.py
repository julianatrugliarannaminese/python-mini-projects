print("Assistente de Organização Pessoal")

nome = input("Qual seu nome?")
idade = int(input("qual sua idade?"))
horas_estudadas = int(input("quantas horas estudou?"))
calculo_de_horas = horas_estudadas * 60
print(f"você estou por {calculo_de_horas} minutos.")
if calculo_de_horas > 59:
  print("Parabéns você estudou mais de uma hora!")
else:
  print("Continue praticando! Você está evoluindo.")
