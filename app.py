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

tabela = pandas.read_csv('alunos.csv')

for linha in tabela.index:
    pyautogui.press('tab', presses=5
    )   
    nome = tabela.loc[linha, 'Nome']
    pyautogui.write(nome)
    pyautogui.press('tab')
    email = tabela.loc[linha, 'Email']
    pyautogui.write(email)
    pyautogui.press('tab')
    endereco = tabela.loc[linha, 'Endereco']
    pyautogui.write(endereco)
    pyautogui.press('tab')
    telefone = tabela.loc[linha, 'Telefone']
    pyautogui.write(telefone)
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.scroll(5000)