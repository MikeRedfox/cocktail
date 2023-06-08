import PySimpleGUI as sg
from sqlmodel import SQLModel, Session, create_engine, Field, JSON, Column, select
from main import Cocktail
import random
import textwrap

def display_random_cocktail():
    r = random.choice(results)
    window['cn'].update(f'{r.name}')
    window['ca'].update(f'Alcoholic: {r.alcoholic}')
    window['cg'].update(f'Glass: {r.glass}')
    ing_str = [(k,v) for k,v in r.ingredients.items()]
    s = ''
    for k,v in ing_str:
        s += f'{k}: {v}\n'
    window['ci'].update(f'{s}')
    window['ing'].update(f'Ingredients')
    window['istr'].update(f'Istruzioni')

    inst = textwrap.fill(r.instructions,40)

    window['cin'].update(f'{inst}')
    

    


engine = create_engine("sqlite:///database.db")
HEIGHT = 900
WIDTH = 700

with Session(engine) as session:
    statement = select(Cocktail)
    results = session.exec(statement).all()

h1 = ("Firacode", 32)
h2 = ('Firacode',20)
h3 = ('Firacode',10)
row1 = [sg.Push(),sg.Text('Random Cocktail Recipe',font=h1),sg.Push()]
row2 = [sg.Push(),sg.Image('cocktail.png'),sg.Push()]
row3 = [sg.Push(),sg.RealtimeButton('Get Random Cocktail',key='rc'),sg.Push(),]
row4 = [sg.Push(),sg.Text('',key='cn',font=h2),sg.Push()]
row5 = [sg.Text('',key='cg',font=h3),sg.Text('',key='ca',font=h3),]
row6 = [sg.Push(),sg.Text('',key='ing',font=h2),sg.Push()]
row7 = [sg.Text('',key='ci',font=h3),]
row8 = [sg.Push(),sg.Text('',key='istr',font=h2),sg.Push()]
row9 = [sg.Text('',key='cin',font=h3)]
layout = [row1,
          row2,
          row3,
          row4,
          row5,
          row6,
          row7,
          row8,
          row9,]
window = sg.Window('Cocktail',layout,size=(WIDTH,HEIGHT))

while True:

    event,values = window.read()


    if event in (sg.WIN_CLOSED, 'Cancel'):
        break

    if event == 'rc':
        display_random_cocktail()


window.close()