from tkinter import *
from tkinter import filedialog

from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

import arquivo
#Globals
import Global
from blocos import bloco2, bloco3, bloco5, eeatt, ftatt


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
        bloco3.diagrama_nyquist(Global.sys1)
        
class Tela_Diagrama_Bloco(Screen):
    pass
class Tela_Estabilidade(Screen):
    def gerar_mapa_polos_zeros(self):
        polos, zeros = bloco5.mapa_polos_zeros(Global.sys1)
        self.dialog = MDDialog(
            title = "Polos e Zeros", 
            text= f"Sistema:\n{Global.sys1}\nPolos:\n{polos}\nZeros:\n{zeros}",
            buttons=[MDFlatButton(
                text="Ok",
                on_release = self.fechar
                )
            ])
        
        self.dialog.open()

    def gerar_root_locus(self):
        self.dialog = MDDialog(
            title = "ERROR", 
            text= "Sistema impróprio para Root Locus.",
            buttons=[MDFlatButton(
                text="Ok",
                on_release = self.fechar
                )
            ])
        if(Global.apto_root_locus):
            bloco5.lugar_raizes(Global.sys1)
        else:
            self.dialog.open()

    def gerar_margem_estabilidade(self):
        marg_mag, marg_fase, freq_mag, freq_fase = bloco5.margem_estabilidade(Global.sys1)
        self.dialog = MDDialog( 
            text= """
                Sistema: {}\n
                Margem de magnitude (dB): {:.4f}\n
                Margem de fase (graus): {:.4f}\n
                Frequência de cruzamento de magnitude (rad/s): {:.4f}\n
                requência de cruzamento de fase (rad/s): {:.4f}
            """.format(Global.sys1, marg_mag, marg_fase, freq_mag, freq_fase),  
            buttons=[MDFlatButton(
                text="Ok",
                on_release = self.fechar
                )
            ])
        self.dialog.open()
    
    def fechar(self, obj):
        self.dialog.dismiss()

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
        Global.sys1,Global.sys2,Global.error,Global.atencao, Global.apto_root_locus = ftatt.dados_finais_FT(Global.caminho_arquivo)
        if(Global.error !='sem erro'):
            Global.texto1=Global.error
        print(Global.sys1)
        print(Global.sys2)
        print(Global.error)
        self.texto_A=Global.atencao
        self.texto_E=Global.error
        print(Global.atencao)
        print("Apto para root locus? ", Global.apto_root_locus)
        

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

        bloco2.resp_impulso_unitario(Global.sys1, inicial, final)
    
    def clear(self):
        self.ids.t_inicial.text = ""
        self.ids.t_final.text = ""

class Entrada_Tempo_degrau_unit(Screen):
    def gerar_grafico_deg_unit(self):
        if(self.ids.t_inicial.text == "" or self.ids.t_final.text == ""):
            return
        
        inicial = float(self.ids.t_inicial.text)
        final = float(self.ids.t_final.text)

        bloco2.resp_degrau_unitario(Global.sys1, inicial, final)

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

        bloco2.resp_condicao_inicial(Global.sys1, inicial, final, vetor)
        
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

        bloco2.resp_forcada(Global.sys1, inicial, final, vetor)


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
