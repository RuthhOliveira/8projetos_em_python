import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'você gostaria de gerar um novo valor para o dado ?'
        #layout
        self.layout = [
            [sg.Text('jogar o dado?')],
            [sg.Button('sim'),sg.Button('não')]
        ]
        
    
    def Iniciar(self):
        #criar janela
        self.janela = sg.Window('simulador de dado', layout=self.layout)
        #ler valores
        self.eventos, self.valores = self.janela.Read()
        #fazer alguams coisa com os valores
        
        try:
            if self.eventos == 'sim' or self.eventos =='s':
                self.ValorDoDado()
            elif self.eventos == 'não' or self.eventos == 'n' or self.eventos== 'nao':
                print('Obrigado!')
            else:
                print('favor digitar sim ou não')
        except:
                print('ocorreu um erro ao receber sua resposta')
            
    def ValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))
        
        
Simulador = SimuladorDeDado()
Simulador.Iniciar()
