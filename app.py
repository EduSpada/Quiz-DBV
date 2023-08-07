"""
Desenvolvido por:

Eduardo Rodrigo Spada
Ano: 2023

Aberto para uso ou modificações, com a 
única premissa de manter os créditos do 
desenvolvedor original estampado no 
aplicativo e código.
"""


from bin.views.theme import Theme as tm
import PySimpleGUI as sg
import os, time, random, threading, json


tm.themes('#151515', '#ffffff')
cwd = os.getcwdb().decode('UTF-8')

def questjs():
    with open(cwd+r"\quest.json", 'r',  encoding='utf8') as f:
        return json.load(f)

quest = questjs()

def update(item, info, window):
    window[item].update(info)

def quiz_dbv(classe, window):
    update("resp", "", window)
    qt = len(quest[classe])
    if qt > 0:
        id = random.randint(0, qt-1)
        pergunta = quest[classe][str(id)]["quest"]
        resposta = quest[classe][str(id)]["resp"]
        window["quest"].update(pergunta)
        for x in range(40, 0, -1):
            update("time", str(x), window)
            time.sleep(1)
        update("time", "0", window)
        update("resp", resposta, window)

def quiz_agr(window):
    classes = ["ami", "com", "pes", "pio", "exc", "gui"]
    classe = classes[random.randint(0, 5)]
    quiz_dbv(classe, window)



class Quiz:
    def __init__(self):
        menu_def = [
                ['&Ajuda', '&Sobre...'], ]
    # ------ GUI Defintion ------ #
        s = 1
        layout = [
            [sg.Menu(menu_def, tearoff=False, pad=(200, 1))],
            [sg.Text('Pergunta: ', size=(20, 1)), sg.Text("Uma pergunta estará aqui em breve?", font=("Roboto", 20), key="quest", size=(100, 1))],
            [sg.T("")],
            [sg.Text('Resposta: ', size=(20, 1)), sg.Output(key="resp", size=(200,3))],
            [sg.T("")],
            [sg.T("")],
            [sg.Button('Amigo', key='ami',  size=(20,2), button_color="blue", font=("Roboto", 20)), sg.Button('Companheiro', key='com',  size=(20,2), button_color="red", font=("Roboto", 20))],
            [sg.Button('Pesquisador', key='pes',  size=(20,2), button_color="green", font=("Roboto", 20)), sg.Button('Pioneiro', key='pio',  size=(20,2), button_color="grey", font=("Roboto", 20))],
            [sg.Button('Excursionista', key='exc',  size=(20,2), button_color="purple", font=("Roboto", 20)), sg.Button('Guia', key='gui',  size=(20,2), button_color="yellow", font=("Roboto", 20))],
            [sg.Button('Agrupadas', key='agr',  size=(20,2), button_color="orange", font=("Roboto", 20))], 
            [sg.T("")],
            [sg.T("")],
            [sg.Text('40', key='time',  size=(20,2), font=("Roboto", 100))]
            ]
        window = sg.Window("Quiz DBV By Eduardo Rodrigo Spada",
                           layout,
                           default_element_size=(12, 1),
                           default_button_element_size=(12, 1),
                           button_color=('white','Indigo'), 
                           icon=cwd+r'\bin\img\icon.ico',  
                           size=(1600, 760),
                           resizable=True)
        # ------ Loop & Process button menu choices ------ #        
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            # ------ Process menu choices ------ #
            if event == 'Sobre...':
                window.disappear()
                sg.popup('Sobre o SIB', 'Version 3.0.1',
                         'Layout Version', sg.version,  grab_anywhere=True)
                window.reappear()
            elif event == 'ami':
                threading.Thread(target=quiz_dbv, args=("ami", window, )).start()
            elif event == 'com':
                threading.Thread(target=quiz_dbv, args=("com", window, )).start()
            elif event == 'pes':
                threading.Thread(target=quiz_dbv, args=("pes", window, )).start()
            elif event == 'pio':
                threading.Thread(target=quiz_dbv, args=("pio", window, )).start()
            elif event == 'exc':
                threading.Thread(target=quiz_dbv, args=("exc", window, )).start()
            elif event == 'gui':
                threading.Thread(target=quiz_dbv, args=("gui", window, )).start()
            elif event == 'agr':
                threading.Thread(target=quiz_agr, args=(window, )).start()
        window.close()

Quiz()