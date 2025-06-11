# Instalar as bibliotecas
# Usar as bibliotecas no meu código
# Iniciar a automação
## Abrir o navegador
## Acessar o site
## Autenticar usuário
## Carregar o arquivo que contém os dados a serem inseridos
## Cadastrar os alunos
#### --> Repetir os passos acima até cadastrar todos os alunos


import pyautogui
import pandas
import time

pyautogui.PAUSE = 1
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)
pyautogui.write('https://aula01.simplificapython.com.br')
pyautogui.press('enter')
# pyautogui.hotkey('win', 'up')
time.sleep(2)
# pyautogui.click(x=718, y=683)
# time.sleep(1)
pyautogui.press('tab')
pyautogui.write('admin')
pyautogui.press('tab')
time.sleep(1)
pyautogui.write('simplificapython')
pyautogui.press('tab')
pyautogui.press('enter')

pyautogui.press('tab', presses=3)






