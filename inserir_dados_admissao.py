import pyautogui
from time import sleep

def cadastrar_admissao(cadastro):
    # digitar numero da empresa
    pyautogui.write(cadastro['Código da Empresa'])
    sleep(1)
    # enter
    pyautogui.press('enter')
    sleep(1)
    # enter
    pyautogui.press('enter')
    sleep(1)
    # digita o nome do colaborador
    pyautogui.write(cadastro['Nome do Colaborador'])
    sleep(1)
    # enter
    pyautogui.press('enter')
    sleep(1)
    # digita classe
    pyautogui.write(cadastro['Classe'])
    sleep(1)
    # enter
    pyautogui.press('enter')
    sleep(1)
    # digita cpf
    pyautogui.write(cadastro['CPF'])
    sleep(1)
    # digita pis
    pyautogui.write(cadastro['PIS'])
    sleep(1)
    # digita data admissao
    pyautogui.write(cadastro['Data de Admissão'])
    sleep(1)
    # digita data nascimento
    pyautogui.write(cadastro['Data de Nascimento'])
    sleep(1)
    # digita tipo admissao
    pyautogui.write(cadastro['Tipo de Admissão'])
    sleep(1)
    # enter
    pyautogui.press('enter')
    sleep(1)
    # enter
    pyautogui.press('enter')
    sleep(1)
    # digita funcao
    pyautogui.write(cadastro['Função'])
    sleep(1)
    # enter
    pyautogui.press('enter')
    sleep(1)
    # digita tipo colaborador 
    pyautogui.write(cadastro['Tipo de Colaborador'])
    sleep(1)
    # enter
    pyautogui.press('enter')
    sleep(1)
    # digita salario base
    pyautogui.write(cadastro['Salário Base'])
    sleep(1)
    # enter
    pyautogui.press('enter')
    sleep(1)
    # digita tipo de contrato
    pyautogui.write(cadastro['Tipo de Contrato'])
    sleep(1)
    # se tipo contrato for 3 entao:
    if cadastro['Tipo de Contrato'] == '3':
        # enter
        pyautogui.press('enter')
        sleep(1)
        # digita o prazo em dias
        pyautogui.write(cadastro['Prazo de Contrato'])
        sleep(1)
    
    pyautogui.hotkey('pagedown')
    sleep(4)
    # pagdown
    # se o prazo for indeterminado
    # pagdown

