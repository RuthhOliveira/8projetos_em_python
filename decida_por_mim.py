import random
import PySimpleGUI as sg

class DecidaporMim:
    def __init__(self):
        self.respostas = [
            'com certeza, você deve fazer isso',
            'não sei, você que sabe',
            'não faz isso NÃO!',
            'Acho que tá na hora certa!'
        ]
    
    def Iniciar(self):
        #layout
        layout = [
            [sg.Text('Faça sua pergunta:')],
            [sg.Input(size=(30,2))],
            [sg.Output(size=(50,10))],
            [sg.Button('Decida por mim')]
        ]
        #janela
        self.janela = sg.Window('Decida por mim!', layout=layout)
        while True:
            #ler os valores
            self.eventos, self.valores = self.janela.read()
            #fazer algo com os valores
            if self.eventos == 'Decida por mim':
                print(random.choice(self.respostas))
            
        
decida = DecidaporMim()
decida.Iniciar()
        