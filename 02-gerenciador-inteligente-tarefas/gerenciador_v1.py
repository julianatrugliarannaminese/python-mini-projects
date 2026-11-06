print("gerenciador inteligente de tarefas inicializado")
total_minutos = 0
tarefas = ""
for i in range(3):
  tarefas_atual = input(f"Digite a tarefa {i + 1}: ")
  minutos = int(input("quantos minutos pra essa tarefa?"))
  total_minutos = total_minutos + minutos

  tarefas = tarefas + tarefas_atual + ""


horas = total_minutos / 60
print(f"total de minutos: {total_minutos}")
print(f"total de horas: {horas}")


def classificar_planejamento(total_minutos):
  if total_minutos <= 60:
   return("planejamento leve")
  elif total_minutos <= 120:
   return("planejamento normal")
  elif total_minutos <= 180:
   return("planejamento extraordinário")
  else:
   return("planejamento explêndido!")

print(classificar_planejamento(total_minutos))
print(f"suas tarefas: {tarefas}")
