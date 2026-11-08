nome = input("Qual seu nome? ")
tarefas = int(input("Quantas tarefas realizou hoje? "))

total = 0

for i in range(tarefas):
    tempo = int(input("Quanto tempo gastou nessa atividade? "))
    total = total + tempo

print(f"{nome}, você gastou {total} minutos para realizar as tarefas.")

def classificar(total):
    if total <= 60:
        return "Estudou pouco."
    elif total <= 120:
        return "Estudou dentro do padrão."
    else:
        return "Você estudou mais do que o esperado, parabéns!"

print(classificar(total))
