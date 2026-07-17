print("\n")
ganho_hora = float(input("Qual o ganho por hora? "))
horas_trabalhadas = float(input("Quantas horas trabalhadas no mês? "))

ir = (ganho_hora * horas_trabalhadas) * 0.11
inss = (ganho_hora * horas_trabalhadas) * 0.08
sindicato = (ganho_hora * horas_trabalhadas) * 0.05
salario_bruto = ganho_hora * horas_trabalhadas
salario_liquido = salario_bruto - ir - inss - sindicato


print("\n")
print(f"IR: {ir} ")
print(f"INSS: {inss}")
print(f"Sindicato: {sindicato}")
print(f"Salário Bruto: {salario_bruto}")
print(f"Salário Líquido: {salario_liquido}")



