from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.button import MDFlatButton


from tkinter import filedialog
from tkinter import *

import arquivo
from blocos import bloco3

#Globals
import Global

'''ola'''
#----------------------------------------- Gerenciador de Telas ----------------------------------------#
class GerenciarTelas(ScreenManager):
    pass
#------------------------------------------ Telas Principais -------------------------------------------#
class Tela_Inicial(Screen):
    pass
class Tela_Menu(Screen):
    pass

class Tela_Arquivo(Screen):
    caminho_arquivo=''
    sys1=0
    sys2=0
    error='nenhum'  
    
    texto1=StringProperty('Anexe o arquivo .txt com as matrizes')
        
    def caminho_arquivo(self, *args):
        root = Tk()
        root.withdraw()
        root.directory = filedialog.askopenfilename(filetypes=(("text files","txt"),))
        print (root.directory)
        
        Global.caminho_arquivo=root.directory        
        Global.sys1,Global.sys2,Global.error = arquivo.dados_finais(Global.caminho_arquivo)
        if(Global.error !='sem erro'):
            Global.texto1=Global.error
        print(Global.sys1)
        print(Global.sys2)
        print(Global.error)
        

    

    def confirmacao(self,*args):
        
        if(Global.error=='nenhum'):
            self.manager.current=Projetoele.tela_menu
            
            
    pass

class Tela_Representacao_Sistema(Screen):
    pass
class Tela_Tempo_Resposta(Screen):
    pass        
class Tela_Resposta_Frequencia(Screen):
    pass
class Tela_Diagrama_Bloco(Screen):
    pass
class Tela_Estabilidade(Screen):
    pass
class Tela_Desing_Controle(Screen):
    pass
class Tela_Digitalizacao(Screen):
    pass

# ----------------------------------------- Telas_Secundárias ------------------------------------------- #

#---Tempo Resposta---#

class Entrada_Tempo(Screen):
    pass


#---Resposta de Frequência---#

#2°

class Entrada_Tempo_Ini_Fim(Screen):
  
    def gerar_grafico_bode(self):
        if(self.ids.fmax.text == "" or self.ids.fmin.text == ""):
            return

        f_max = int(self.ids.fmax.text)
        f_min = int(self.ids.fmin.text)
        print(Global.sys1)
        bloco3.diagrama_bode(f_max, f_min,Global.sys1)
        

    def clear(self):
        self.ids.fmin.text = ""
        self.ids.fmax.text = ""

#---Diagrama de Bloco---#

#2°
class Entrada_Realimentacao_Tipo(Screen):
    pass


#App
class Projetoele(MDApp):
    #string das telas principais e secundárias
    tela_inicio='tela_inicio'
    tela_arquivo='tela_arquivo'        
    tela_menu='tela_menu'
    tela_representacao_sistema='tela_representacao_sistema'
    tela_tempo_resposta='tela_tempo_resposta'
    tela_resposta_frequencia='tela_resposta_frequencia'
    tela_diagrama_bloco='tela_diagrama_bloco'
    tela_estabilidade='tela_estabilidade'
    tela_desing_controle='tela_desing_controle'
    tela_digitalizacao='tela_digitalizacao'

    #titulo do app
    titulo='Controller Design'
    Window.size =(300,600)
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Yellow" ##FFEB3B


Projetoele().run()