import os
import sys
from tkinter import *
from tkinter import filedialog

import numpy as np
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from kivy.resources import resource_add_path, resource_find
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

#Globals
import Global
from blocos import bloco2, bloco3, bloco4, bloco5, eeatt, ftatt


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
    def resp_serie(self):
        serie=bloco4.serie_bl4(Global.sys1,Global.sys2)
        print(serie)
        
        self.dialog = MDDialog(
            title = "Resposta Serie",   
            text= f"{serie}",
            buttons=[MDFlatButton(
                text="Ok",
                on_release = self.fechar
                )
            ])
        self.dialog.open()

    def resp_paralelo(self):
        paralelo=bloco4.paralelo_bl4(Global.sys1,Global.sys2)
        print(paralelo)
        self.dialog = MDDialog(
            title = "Resposta Paralelo",   
            text= f"{paralelo}",
            buttons=[MDFlatButton(
                text="Ok",
                on_release = self.fechar
                )
            ])
        self.dialog.open()

    
    def fechar(self, obj):
        self.dialog.dismiss()    
    pass
class Tela_Estabilidade(Screen):
    def gerar_mapa_polos_zeros(self):
        polos, zeros = bloco5.mapa_polos_zeros(Global.sys1)

        abrir_popup(self, 
            f"Sistema:\n{Global.sys1}\nPolos:\n{polos}\nZeros:\n{zeros}", 
            "Polos e Zeros"
        )
    
    def gerar_root_locus(self):
        if(Global.tem_atencao):
            bloco5.lugar_raizes(Global.sys1)
        else:
            abrir_popup(self, "Sistema impróprio para Root Locus.")

    def gerar_margem_estabilidade(self):
        marg_mag, marg_fase, freq_mag, freq_fase = bloco5.margem_estabilidade(Global.sys1)

        msgm = """
                Sistema: {}\n
                Margem de magnitude (dB): {:.4f}\n
                Margem de fase (graus): {:.4f}\n
                Frequência de cruzamento de magnitude (rad/s): {:.4f}\n
                requência de cruzamento de fase (rad/s): {:.4f}
            """.format(Global.sys1, marg_mag, marg_fase, freq_mag, freq_fase)

        abrir_popup(self, msgm, 'Margem de Estabilidade')

    
    def fechar(self, obj):
        self.dialog.dismiss()


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
        try:  
            Global.sys1,Global.sys2,Global.error,Global.atencao, Global.tem_atencao = ftatt.dados_finais_FT(Global.caminho_arquivo)
        except Exception as e:
            abrir_popup(self, str(e))
            return
            
        if(Global.error !='sem erro'):
            Global.texto1=Global.error
        print(Global.sys1)
        print(Global.sys2)
        print(Global.error)
        self.texto_A=Global.atencao
        self.texto_E=Global.error
        print(Global.atencao)
        print("Apto para root locus? ", Global.tem_atencao)
    
    def fechar(self, obj):
        self.dialog.dismiss()
        

    def confirmacao(self,*args):
        self.texto1 = ''
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
        try:     
            Global.sys1,Global.sys2,Global.atencao_EE_RA,Global.atencao_EE_DF,Global.error = eeatt.dados_finais_EE(Global.caminho_arquivo)
        except Exception as e:
            abrir_popup(self, str(e))
            return
            
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

    def fechar(self, obj):
        self.dialog.dismiss()

#---Tempo Resposta---#

def FuncaoTempo(t_final, t_inicial=0.0, X0=0.0):
    #X0 = []
    aux = 0
    erro = 'sem erro'
    #Se a pessoa não quiser definir o tempo, basta deixar a variável em branco.
    if (t_inicial != ''):
        t_inicial = float(t_inicial)
    else:
        t_inicial = 0.0
        aux = aux + 1
    print("Tempo inicial: ", t_inicial)

    if t_final != '':
        t_final = float(t_final)
    else:
        t_final = 100.0
        aux = aux + 1
    print("Tempo final: ", t_final)

    #Condição Inicial (X0):
    if X0 != '':
        X0 = float(X0)
    else:
        X0 = 0.0

    #Criando vetor de tempo_inicial a tempo_final, com passo de 0.01, para plotagem de gráfico.
    T = np.arange(t_inicial, t_final, 0.01)
    return (T, X0, aux)

#TODO: centralizar os popups utilizando essa função
def abrir_popup(self, msg, titl='ERROR'):
    self.dialog = MDDialog(
        title = titl, 
        text= msg,
        buttons=[MDFlatButton(
            text="Ok",
            on_release = self.fechar
            )
        ]
    )
    self.dialog.open()

class Entrada_Tempo_impulso_unit(Screen):
    
    def gerar_grafico_imp_unit(self):
        T, X0 , aux = FuncaoTempo(self.ids.t_final.text, self.ids.t_inicial.text)

        try:
            bloco2.resp_impulso_unitario(Global.sys1, T, X0)
        except Exception as e:
            abrir_popup(self, str(e))
    
    def clear(self):
        self.ids.t_inicial.text = ""
        self.ids.t_final.text = ""

    def fechar(self, obj):
        self.dialog.dismiss()

class Entrada_Tempo_degrau_unit(Screen):
    def gerar_grafico_deg_unit(self):
        T, X0 , aux = FuncaoTempo(self.ids.t_final.text, self.ids.t_inicial.text)

        try:
            bloco2.resp_degrau_unitario(Global.sys1, T, X0)
        except Exception as e:
            abrir_popup(self, str(e))

    def clear(self):
        self.ids.t_inicial.text = ""
        self.ids.t_final.text = ""

    def fechar(self, obj):
        self.dialog.dismiss()

class Entrada_Tempo_condicao_ini(Screen):
    def gerar_grafico_codicao_ini(self):
        T, X0, aux = FuncaoTempo(self.ids.t_final.text, self.ids.t_inicial.text)

        try:
            bloco2.resp_condicao_inicial(Global.sys1, T, X0)
        except Exception as e:
            abrir_popup(self, str(e))
        
    def clear(self):
        self.ids.t_inicial.text = ""
        self.ids.t_final.text = ""
        self.ids.elemento1.text = ""
        self.ids.elemento2.text = ""

    def fechar(self, obj):
        self.dialog.dismiss()

class Entrada_Tempo_forcada(Screen):
    def gerar_grafico_resp_senoidal(self):

        T, X0, aux = FuncaoTempo(self.ids.t_final.text, self.ids.t_inicial.text)
        try:
            bloco2.resp_senoidal(Global.sys1, T, X0, float(self.ids.amplitude.text))
        except Exception as e:
            abrir_popup(self, str(e))

    def clear(self):
        self.ids.t_inicial.text = ""
        self.ids.t_final.text = ""
        self.ids.amplitude.text = ""

    def fechar(self, obj):
        self.dialog.dismiss()
    

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
    def rea_positiva(self):
        posi=bloco4.reali_posi(Global.sys1,Global.sys2)
        print(posi)
        self.dialog = MDDialog(
            title = "Realimentação Positiva",   
            text= f"{posi}",
            buttons=[MDFlatButton(
                text="Ok",
                on_release = self.fechar
                )
            ])
        self.dialog.open()
    def rea_negativa(self):
        nega=bloco4.reali_neg(Global.sys1,Global.sys2)
        print(nega)
        self.dialog = MDDialog(
            title = "Realimentação Negativa",   
            text= f"{nega}",
            buttons=[MDFlatButton(
                text="Ok",
                on_release = self.fechar
                )
            ])
        self.dialog.open()

            

    def fechar(self, obj):
        self.dialog.dismiss()    

    pass


#App
class Projetoele(MDApp):
    #string das telas principais e secundárias
    #inicio
    tela_inicio='tela_inicio'
    tela_escolha_sistema='tela_escolha_sistema'
    tela_arquivo_ft='tela_arquivo_ft'
    tela_arquivo_ee='tela_arquivo_ee'
    #menu        
    tela_menu='tela_menu'
    tela_representacao_sistema='tela_representacao_sistema'
    tela_tempo_resposta='tela_tempo_resposta'
    tela_resposta_frequencia='tela_resposta_frequencia'
    tela_diagrama_bloco='tela_diagrama_bloco'
    tela_estabilidade='tela_estabilidade'

    #diagrama de bloco (4)

    tela_resposta_realimentacao='rela_resposta_realimentacao'

    #titulo do app
    titulo='Controller Design'
    Window.size =(600,600)
    Window.minimum_width = 300
    Window.minimum_height = 600
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Yellow" ##FFEB3B
        return Builder.load_file('projetoele.kv')

if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    Projetoele().run()

