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

# atribuição, a partir de leitura do arquivo de entrada, do salario bruto como item da lista
for linha in arquivo_entrada:
    SalBruto = float(linha)
    salarios.append(SalBruto)

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
    if BaseIR <= 1903.98:
        AliqIR = 0
    elif BaseIR <= 2826.65:
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

# função que, usando todas as funções definidas acima, 
# calcula os campos de alíquota do INSS, valor do INSS,
# base do Imposto de Renda, alíquota do Imposto de Renda,
# valor do Imposto de Renda e, por fim, o salário líquido
def calculo_val(SalBruto):
    AliqINSS = calculo_aliq_inss(SalBruto)
    ValINSS = calculo_val_inss(SalBruto, AliqINSS)
    BaseIR = SalBruto - ValINSS
    AliqIR = calculo_aliq_ir(SalBruto, ValINSS)
    ValIR = calculo_val_ir(SalBruto, ValINSS, BaseIR, AliqIR)
    SalLiquido = SalBruto - ValINSS - ValIR
    # função finaliza retornando uma lista, conforme citado anteriormente
    return [SalBruto, AliqINSS, ValINSS, BaseIR, AliqIR, ValIR, SalLiquido]
    

#PARTE 3 - DEFINIR FORMATAÇÃO EM TABELA PARA SAÍDA DOS DADOS

saida = ""
# inclusão do cabeçalho na saída que será gravada no arquivo de saída
saida += f"{'Bruto': >12}{'AliqINSS': >12}{'Val.INSS': >12}{'Base I.R.': >12}{'AliqIR': >12}{'Val.IR': >12}{'Liquido': >12}\n"

for salario in salarios:
    salario_calculado = calculo_val(salario)
    # pega os valores e os salva em uma vari após serem calculados pela função 'calculo_val'
    SalBruto, AliqINSS, ValINSS, BaseIR, AliqIR, ValIR, SalLiquido = salario_calculado
    # os campos de alíquotas são formatadas com 1 casa decimal, enquanto os demais com 2
    AliqINSS, AliqIR = map(lambda x: f"{x:.1f}", [AliqINSS, AliqIR])
    SalBruto, ValINSS, BaseIR, ValIR, SalLiquido = map(lambda x: f"{x:.2f}", [SalBruto, ValINSS, BaseIR, ValIR, SalLiquido])
    # com as casas decimais dos campos definidas, podemos aplicar o mesmo espaçamento que demos ao cabeçalho a cada um dos campos
    saida += f"{SalBruto: >12}{AliqINSS: >12}{ValINSS: >12}{BaseIR: >12}{AliqIR: >12}{ValIR: >12}{SalLiquido: >12}\n"

# retirada da última quebra-linha gerada no laço for anterior
saida = saida.rstrip("\n")

arquivo_saida = open("CALCULOS.TXT", "w")
arquivo_saida.write(saida)
arquivo_saida.close()

print("Fim do Programa")  
