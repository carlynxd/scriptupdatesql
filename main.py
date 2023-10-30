import pandas as pd

arquivo = 'PLANILHA MOTORISTAS.xlsx'

dfsheets = pd.read_excel(arquivo, sheet_name=None)

cpf2 = []

for sheets, df in dfsheets.items():
    cpf = df['CPF']
    print(sheets)
    for num in range(len(cpf)):
        control = str(cpf[num])
        control = control.replace(".", "").replace("-", "").replace("/", "").replace(" ", "").replace(" ", "")
        cpf2.append(control)
        print(cpf2)


i = 0
with open("UPDATE.TXT", 'w') as arquivo:
    arquivo.write(f"update tb_motorista set motorista_ativo = 'S' where MOTORISTA_CADASTRO IN (")
    for i in range(len(cpf2)):
        if i == len(cpf2) - 1:
            arquivo.write(f"'{cpf2[i]}')")
        else:
            arquivo.write(f"'{cpf2[i]}',\n")

