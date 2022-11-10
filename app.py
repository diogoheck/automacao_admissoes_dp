from leitura_csv import ler_planilha_csv
from login_unico import logar_unico
from selecionar_mod_DP import acessar_modulo_folha
from admissao_preliminar import acessar_modulo_admissao_preliminar
from inserir_dados_admissao import cadastrar_admissao
from time import sleep

cadastro_colaborador = ler_planilha_csv()

print(cadastro_colaborador)


# logar no unico
# logar_unico()
# entrar no unico->folha
# acessar_modulo_folha()
# Admissao preliminar
sleep(5)
acessar_modulo_admissao_preliminar()
# cadastro admissao preliminiar
cadastrar_admissao(cadastro_colaborador)

print('*' * 50)
print('FIM')
print('*' * 50)