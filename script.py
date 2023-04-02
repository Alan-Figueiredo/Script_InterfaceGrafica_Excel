import pandas as pd
import pyautogui as pg
import numpy as np
import time

df = pd.read_excel("baseDeDados.xlsx")

def start(a:int):
    teste = df.iloc[a,0]
    teste1 = df.iloc[a,1]
    teste2 = df.iloc[a,2]
    teste3 = df.iloc[a,3]
    teste4 = df.iloc[a,5]
    teste5 = df.iloc[a,6]
    teste6 = df.iloc[a,7]

    arr = np.array([teste,teste1,teste2,teste3,teste5,teste6])

    time.sleep(1)
    for a in arr[:4]:
        pg.write(a)
        pg.press("tab")

    pg.write("ba")
    pg.press("tab")
    pg.write(teste4)
    pg.press("tab")

    for a in arr[4:]:
        pg.write(a)
        pg.press("tab")
        
    pg.press("enter")
