    # pyautogui -> Fazer automacoes com Python
    # pyautogui.click  ->  Clicar em algum lugar
    # pyautogui.press  ->  Apertar 1 tecla
    # pyautogui.write  ->  Escrever um texto
    # pyautogui.hotkey -> Apertar uma combinacao de teclas
    # Nan -> Not a number

import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')

# Digite o site 

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# Espere 2.5 segundos

time.sleep(2.5)

# Fazer login 

pyautogui.click(x=728, y=398)
pyautogui.write('leonardo.esmarjassi@gmail.com')

# Pular para outro campo 

pyautogui.press('tab')
pyautogui.write('senhasecreta')

# Pular mais um campo para logar no site

pyautogui.press('tab')
pyautogui.press('enter')

#Esperar um pouco caso nao carregue

time.sleep(2.5)

# Importar base da dados (pandas)

import pandas

tabela = pandas.read_csv('produtos.csv')

print (tabela)

# Cadastrar produtos
for linha in tabela.index: # Para cada linha da minha tabela 
    pyautogui.click(x=732, y=280)

    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)


    pyautogui.press('tab') # Passar para o prox campo
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)


    pyautogui.press('tab') # Passar para o prox campo
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)


    pyautogui.press('tab') # Passar para o prox campo
    categoria = str(tabela.loc[linha, 'categoria']) # string = texto -> str()
    pyautogui.write(categoria)


    pyautogui.press('tab') # Passar para o prox campo
    preco_unitario = str(tabela.loc[linha, 'preco_unitario']) # string = texto -> str()
    pyautogui.write(preco_unitario)


    pyautogui.press('tab') # Passar para o prox campo
    custo = str(tabela.loc[linha, 'custo']) # string = texto -> str()
    pyautogui.write(custo)


    pyautogui.press('tab') # Passar para o prox campo
    obs = str(tabela.loc[linha, 'obs']) # string = texto -> str()
    if obs != 'nan':
        pyautogui.write(obs)


    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(100000)

# Repetir todos os produtos
