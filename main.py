from tkinter import *
from tkinter import filedialog

from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.button import MDFlatButton


from blocos import bloco3, eeatt, ftatt

#Globals
import Global



#----------------------------------------- Gerenciador de Telas ----------------------------------------#
class GerenciarTelas(ScreenManager):
    pass
#------------------------------------------ Telas Principais -------------------------------------------#
class Tela_Inicial(Screen):
    pass
class Tela_Escolha_Tipo_Sistema(Screen):
    pass
class Tela_Menu(Screen):
    pass

class Tela_Arquivo(Screen):
    
        
    
        
    
        

    

    
    

    
            
    pass

class Tela_Representacao_Sistema(Screen):
    pass
class Tela_Tempo_Resposta(Screen):
    pass        
class Tela_Resposta_Frequencia(Screen):
    def gerar_grafico_nyquist(self):
        bloco3.diagrama_nyquist()
        
class Tela_Diagrama_Bloco(Screen):
    pass
class Tela_Estabilidade(Screen):
    pass
class Tela_Design_Controle(Screen):
    pass
class Tela_Digitalizacao(Screen):
    pass

# ----------------------------------------- Telas_Secundárias ------------------------------------------- #

#--- Escolha Tipo Sistema ---#

class Tela_Arquivo_FT(Screen):
    caminho_arquivo=''
    sys1=0
    sys2=0
    error='nenhum'  
    
    
    texto1=StringProperty('Anexe o arquivo .txt com as matrizes.')
    texto_A=StringProperty('Nenhuma Atenção.')
    texto_E=StringProperty('Nenhum Erro.')
    def caminho_arquivo_FT(self, *args):
        root = Tk()
        root.withdraw()
        root.directory = filedialog.askopenfilename(filetypes=(("text files","txt"),))
        print (root.directory)
        self.texto1=root.directory
        
        Global.caminho_arquivo=root.directory        
        Global.sys1,Global.sys2,Global.error,Global.atencao = ftatt.dados_finais_FT(Global.caminho_arquivo)
        if(Global.error !='sem erro'):
            Global.texto1=Global.error
        print(Global.sys1)
        print(Global.sys2)
        print(Global.error)
        self.texto_A=Global.atencao
        self.texto_E=Global.error
        print(Global.atencao)
        

    def confirmacao(self,*args):
    
        if(Global.error=='sem erro'):
            self.manager.current=Projetoele.tela_menu   
    pass

class Tela_Arquivo_EE(Screen):
    caminho_arquivo=''
    sys1=0
    sys2=0
    error='nenhum'  
    
    texto1=StringProperty('Anexe o arquivo .txt com as matrizes.')
    texto_A=StringProperty('Nenhuma Atenção.')
    texto_E=StringProperty('Nenhum Erro.')
    def caminho_arquivo_EE(self, *args):
        root = Tk()
        root.withdraw()
        root.directory = filedialog.askopenfilename(filetypes=(("text files","txt"),))
        print (root.directory)
        
        Global.caminho_arquivo=root.directory        
        Global.sys1,Global.sys2,Global.atencao_EE_RA,Global.atencao_EE_DF,Global.error = eeatt.dados_finais_EE(Global.caminho_arquivo)
        if(Global.error !='sem erro'):
            Global.texto1=Global.error
        print(Global.sys1)
        print(Global.sys2)
        print(Global.error)
        print(Global.atencao)
        self.texto1=root.directory
        self.texto_A=Global.atencao_EE_DF
        self.texto_E=Global.error
    def confirmacao(self,*args):
        
        if(Global.error=='sem erro'):
            self.manager.current=Projetoele.tela_menu
    pass    

#---Tempo Resposta---#

class Entrada_Tempo_impulso_unit(Screen):
    def gerar_grafico_imp_unit(self):
        if(self.ids.t_inicial.text == "" or self.ids.t_final.text == ""):
            return

        inicial = float(self.ids.t_inicial.text)
        final = float(self.ids.t_final.text)

        bloco2.resp_impulso_unitario(inicial, final)
    
    def clear(self):
        self.ids.t_inicial.text = ""
        self.ids.t_final.text = ""

class Entrada_Tempo_degrau_unit(Screen):
    def gerar_grafico_deg_unit(self):
        if(self.ids.t_inicial.text == "" or self.ids.t_final.text == ""):
            return
        
        inicial = float(self.ids.t_inicial.text)
        final = float(self.ids.t_final.text)

        bloco2.resp_degrau_unitario(inicial, final)

    def clear(self):
        self.ids.t_inicial.text = ""
        self.ids.t_final.text = ""

class Entrada_Tempo_condicao_ini(Screen):
    def gerar_grafico_codicao_ini(self):
        if(self.ids.t_inicial.text == "" or self.ids.t_final.text == "" or
        self.ids.elemento1.text == "" or self.ids.elemento2.text == ""):
            return

        inicial = float(self.ids.t_inicial.text)
        final = float(self.ids.t_final.text)

        vetor = list((int(self.ids.elemento1.text), int(self.ids.elemento2.text)))

        bloco2.resp_condicao_inicial(inicial, final, vetor)
        
    def clear(self):
        self.ids.t_inicial.text = ""
        self.ids.t_final.text = ""
        self.ids.elemento1.text = ""
        self.ids.elemento2.text = ""

class Entrada_Tempo_forcada(Screen):
    def gerar_grafico_resp_forcada(self):
        if(self.ids.t_inicial.text == "" or self.ids.t_final.text == "" or
        self.ids.elemento1.text == "" or self.ids.elemento2.text == ""):
            return

        inicial = float(self.ids.t_inicial.text)
        final = float(self.ids.t_final.text)

        vetor = list((int(self.ids.elemento1.text), int(self.ids.elemento2.text)))

        bloco2.resp_forcada(inicial, final, vetor)


    def clear(self):
        self.ids.t_inicial.text = ""
        self.ids.t_final.text = ""
        self.ids.elemento1.text = ""
        self.ids.elemento2.text = ""
    

#---Resposta de Frequência---#

#2°

class Entrada_Tempo_Ini_Fim(Screen):
  
    def gerar_grafico_bode(self):
        if(self.ids.fmax.text == "" or self.ids.fmin.text == ""):
            return

        f_max = float(self.ids.fmax.text)
        f_min = float(self.ids.fmin.text)
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
    tela_escolha_sistema='tela_escolha_sistema'
    tela_arquivo_ft='tela_arquivo_ft'
    tela_arquivo_ee='tela_arquivo_ee'        
    tela_menu='tela_menu'
    tela_representacao_sistema='tela_representacao_sistema'
    tela_tempo_resposta='tela_tempo_resposta'
    tela_resposta_frequencia='tela_resposta_frequencia'
    tela_diagrama_bloco='tela_diagrama_bloco'
    tela_estabilidade='tela_estabilidade'
    tela_design_controle='tela_design_controle'
    tela_digitalizacao='tela_digitalizacao'

    #titulo do app
    titulo='Controller Design'
    Window.size =(300,600)
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Yellow" ##FFEB3B


Projetoele().run()
