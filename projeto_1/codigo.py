#passo 1: abrir o sistema da empresa
import pyautogui
import time
import pandas

pyautogui.PAUSE = 2

#abrir o chrome
pyautogui.hotkey('alt', 'space')
pyautogui.write('chrome')
pyautogui.press('enter')

#abrir url do sistema
pyautogui.hotkey('ctrl', 't')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

#passo 2: fazer login
time.sleep(2)
pyautogui.click(x=714, y=563)
pyautogui.write('josed@silva.org')
pyautogui.press('tab')
pyautogui.write('nao atrapalha chrome fdp')
pyautogui.press('tab')
pyautogui.press('enter')

#passo 3: importar a base de dados do produto
arkivo = pandas.read_csv('produtos.csv')

#passo 4: cadastrar produtos
time.sleep(2)

for linha in arkivo.index:
    pyautogui.click(x=566, y=389)

    codigo = arkivo.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    marca = arkivo.loc[linha, 'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    tipo = arkivo.loc[linha, 'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    categoria = arkivo.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    preco_unitario = arkivo.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')

    custo = arkivo.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    obs = str(arkivo.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)

    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(22)
