def abrir_navegador():
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    time.sleep(5)

def acessar_sistema(https://dlp.hashtagtreinamentos.com/python/intensivao/login):
    pyautogui.write(https://dlp.hashtagtreinamentos.com/python/intensivao/login)
    pyautogui.press("enter")
    time.sleep(5)

def fazer_login(email, senha):
    pyautogui.click(x=642, y=622)
    pyautogui.write(email)
    pyautogui.press("tab")
    pyautogui.write(senha)
    pyautogui.press("enter")
    time.sleep(5)

def cadastrar_produto(produto):
    pyautogui.click(x=653, y=294)
    pyautogui.write(str(produto["codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(produto["marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(produto["tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(produto["categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(produto["preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(produto["custo"]))
    pyautogui.press("tab")
    if not pd.isna(produto["obs"]):
        pyautogui.write(str(produto["obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(10000)
