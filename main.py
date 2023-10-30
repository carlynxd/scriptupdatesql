import pandas as pd

arquivo = 'PLANILHA MOTORISTAS.xlsx'

df = pd.read_excel(arquivo)

cpf = df['CPF']

for num in range(len(cpf)):
    control = cpf[num]
    cpf[num] = control.replace(".", "").replace("-", "").replace("/", "")

print(cpf)

i = 0
with open("UPDATE", 'w') as arquivo:
    arquivo.write(f"update tb_motorista set motorista_ativo = 'S' where MOTORISTA_CADASTRO IN (")
    for i in range(len(cpf)):
        if i == len(cpf) - 1:
            arquivo.write(f"{cpf[i]})")
        else:
            arquivo.write(f"{cpf[i]},")

