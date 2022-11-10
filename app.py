from leitura_csv import ler_planilha_csv
from login_unico import logar_unico
from selecionar_mod_DP import acessar_modulo_folha
from admissao_preliminar import acessar_modulo_admissao_preliminar

cadastro_colaboradro = ler_planilha_csv()

print(cadastro_colaboradro)


# logar no unico
logar_unico()
# entrar no unico->folha
acessar_modulo_folha()
# Admissao preliminar
acessar_modulo_admissao_preliminar()
# digitar numero da empresa
# enter
# enter
# digita o nome do colaborador
# enter
# digita classe
# enter
# digita cpf
# digita pis
# digita data admissao
# digita data nascimento
# digita tipo admissao
# enter
# enter
# digita funcao
# enter
# digita tipo colaborador 
# enter
# digita salario base
# enter
# digita tipo de contrato
# se tipo contrato for 3 entao:
# enter
# digita o prazo em dias
# pagdown
# se o prazo for indeterminado
# pagdown
