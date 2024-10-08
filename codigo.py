import pyautogui
import pandas as pd
import time

pyautogui.PAUSE = 1

# Abrir navegador
# Apertar a tecla win
pyautogui.press("Win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Digitando link do site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# Digitar email
time.sleep(3)
pyautogui.click(x= 667, y=378)
pyautogui.write("raphaelsoarescosta@gmail.com")

# Digitar senha
pyautogui.press("tab")
pyautogui.write("minha senha aqui")
pyautogui.click(x= 683, y=542)

time.sleep(2)

# Importar base de dados
tabela = pd.read_csv("produtos.csv")
print(tabela)


linha = 0

# Percorrer e cadastrar todos os dados da planilha
for linha in tabela.index:

    pyautogui.click(x=524, y=253)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]

    #verificando se coluna obs está vazia
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    # Seleciona o botão enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)
