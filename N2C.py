print("Cálculo de Salários\n")

print("Mateus Anunciato Sobral")
print("Matheus Silva e Sousa")
print("Tomás Carrera Massabki")
print("Vinicius Esposito Cava\n")

#PARTE 1 - LER O ARQUIVO DE ENTRADA, LINHA A LINHA, E ARMAZENAR SALÁRIOS BRUTOS EM LISTA.

# abrindo arquivo de entrada
arquivo_entrada = open("SALARIO.TXT", "r")

# criando lista geral para funcionarios, a qual conterá uma lista para cada funcionario
salarios = []
# cada sub-lista de funcionário terá o seguinte desenho:
# [SalBruto, AliqINSS, ValINSS, BaseIR, AliqIR, ValIR, SalLiquido]

# atribuição, a partir de leitura do arquivo de entrada, do salario bruto como item 0
# da lista individual de cada funcionario
for linha in arquivo_entrada:
    SalBruto = float(linha)
    salario = [SalBruto]
    salarios.append(salario)

# fechando arquivo de entrada
arquivo_entrada.close()

#PARTE 2 - DEFINIR FUNÇÕES QUE FAZEM, CADA UMA DELAS,
# O CÁLCULO DOS DEMAIS CAMPOS, A PARTIR DO SALÁRIO BRUTO

def calculo_aliq_inss(SalBruto):
    AliqINSS = 0
    if SalBruto <= 1751.81:
        AliqINSS = 8.0
    elif SalBruto <= 2919.73:
        AliqINSS = 9.0
    elif SalBruto <= 5839.45:
        AliqINSS = 11.0
    return AliqINSS


def calculo_val_inss(SalBruto, AliqINSS):
    if AliqINSS != 0:
        ValINSS = SalBruto * (AliqINSS / 100)
    else:
        ValINSS = 642.34
    return ValINSS
    

def calculo_aliq_ir(SalBruto, ValINSS):
    BaseIR = SalBruto - ValINSS
    AliqIR = 0
    if 1903.99 <= BaseIR <= 2826.65:
        AliqIR = 7.5
    elif BaseIR <= 3751.05:
        AliqIR = 15
    elif BaseIR <= 4664.68:
        AliqIR = 22.5
    elif BaseIR > 4664.68:
        AliqIR = 27.5
    return AliqIR


def calculo_val_ir(SalBruto, ValINSS, BaseIR, AliqIR):
    DeducaoIR = 0
    if AliqIR == 7.5:
        DeducaoIR = 142.8
    elif AliqIR == 15:
        DeducaoIR = 354.8
    elif AliqIR == 22.5:
        DeducaoIR = 636.13
    elif AliqIR == 27.5:
        DeducaoIR = 869.36
    ValIR = BaseIR * (AliqIR / 100) - DeducaoIR
    if ValIR < 10:
        ValIR = 0
    return ValIR


def calculo_val(salario):
    SalBruto = salario[0]
    AliqINSS = calculo_aliq_inss(SalBruto)
    ValINSS = calculo_val_inss(SalBruto, AliqINSS)
    BaseIR = SalBruto - ValINSS
    AliqIR = calculo_aliq_ir(SalBruto, ValINSS)
    ValIR = calculo_val_ir(SalBruto, ValINSS, BaseIR, AliqIR)
    SalLiquido = SalBruto - ValINSS - ValIR
    return [SalBruto, AliqINSS, ValINSS, BaseIR, AliqIR, ValIR, SalLiquido]
    

#PARTE 3 - DEFINIR FORMATAÇÃO EM TABELA PARA SAÍDA DOS DADOS

saida = ""
saida += f"{'Bruto': >12}{'AliqINSS': >12}{'Val.INSS': >12}{'Base I.R.': >12}{'AliqIR': >12}{'Val.IR': >12}{'Liquido': >12}\n"

for salario in salarios:
    salario_calculado = calculo_val(salario)
    SalBruto, AliqINSS, ValINSS, BaseIR, AliqIR, ValIR, SalLiquido = salario_calculado
    AliqINSS, AliqIR = map(lambda x: f"{x:.1f}", [AliqINSS, AliqIR])
    SalBruto, ValINSS, BaseIR, ValIR, SalLiquido = map(lambda x: f"{x:.2f}", [SalBruto, ValINSS, BaseIR, ValIR, SalLiquido])
    saida += f"{SalBruto: >12}{AliqINSS: >12}{ValINSS: >12}{BaseIR: >12}{AliqIR: >12}{ValIR: >12}{SalLiquido: >12}\n"

saida = saida.rstrip("\n")

arquivo_saida = open("CALCULOS.TXT", "w")
arquivo_saida.write(saida)
arquivo_saida.close()

print("Fim do Programa")  