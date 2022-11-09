import csv
from ajustar_data import ajustar_data_lancar

def ler_planilha_csv():
    # Ler planilha CSV
    # Criar um dicionario dos dados dos colaboradores
    cadastro_colaborador = {}
    cabecalho = True
    with open('Cadastro de Colaborador.csv', 'r', encoding='utf-8') as cadastro:
        reader = csv.reader(cadastro)
        for linha in reader:
            if not cabecalho:
                # Trabalhar os dados 
                cadastro_colaborador['Código da Empresa'] = linha[1]
                cadastro_colaborador['Nome do Colaborador'] = linha[2]
                # Classe tirar o numero
                cadastro_colaborador['Classe'] = linha[3].split('-')[0].strip()
                # CPF - tirar pontos e traço
                cadastro_colaborador['CPF'] = linha[4].replace('.', '').replace('-', '')
                # PIS - tirar pontos
                cadastro_colaborador['PIS'] = linha[5].replace('.', '')
                # formatar data para digitacao
                cadastro_colaborador['Data de Admissão'] = ajustar_data_lancar(linha[6])
                cadastro_colaborador['Data de Nascimento'] = ajustar_data_lancar(linha[7])
                # tipo admissao , retirar o numero
                cadastro_colaborador['Tipo de Admissão'] = linha[8].split('-')[0].strip()
                cadastro_colaborador['Função'] = linha[9]
                cadastro_colaborador['Tipo de Colaborador'] = linha[10]
                # pegar e trabalhar o valor salario e retirar ponto se tiver
                cadastro_colaborador['Salário Base'] = linha[11].replace('.', '')
                cadastro_colaborador['Tipo de Contrato'] = linha[12]
                cadastro_colaborador['Prazo de Contrato'] = linha[13]
            cabecalho = False
    return cadastro_colaborador