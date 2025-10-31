# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 1 # tempo de espera entre cada ação

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.click(x=947, y=606)
# pyautogui.click(x=703, y=96)
time.sleep(2)


# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)


# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=669, y=628)
# escrever o seu email
pyautogui.write("ayrton.ess@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("python123")
# pyautogui.click(x=955, y=638) # clique no botao de login
pyautogui.press("enter")
time.sleep(3)
  # clicar no campo de código
pyautogui.click (x=580, y=435)
# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv", sep=";")

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    # pyautogui.click (x=580, y=435)
    # pegar da tabela o valor do campo que a gente quer preencher
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(10000)
    # Passo 5: Repetir o processo de cadastro até o fim
