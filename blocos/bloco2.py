import control as ctl
import matplotlib.pyplot as plt
import numpy as np
from control.matlab import *


def plotar_grafico(t, y, title=""):
  plt.plot(t, y)
  plt.title(title)
  plt.xlabel('Tempo (s)')
  plt.ylabel('Amplitude')
  plt.show() 

#------------------------------------------------------------------------------------------------------------------------#

#Botao 1: Resposta ao Impulso Unitario

def resp_impulso_unitario(sys, T, X0):

  #Entradas para o usuário:

  #Vetor para plotagem
  try:
    t, y = ctl.impulse_response(sys, T, X0)
    plotar_grafico(t, y, 'Resposta ao Impulso Unitário')
  except:
    raise Exception('Verifique se a função não é imprópria( nº de zeros > nº de polos)')


def resp_degrau_unitario(sys, T, X0):

  t, y = ctl.step_response(sys, T, X0)

  plotar_grafico(t, y, 'Resposta ao Degrau Unitário')

def resp_condicao_inicial(sys, T, X0): #Resposta com uma condição inicial

  t , y = ctl.initial_response(sys, T, X0)

  plotar_grafico(t, y, 'Resposta com Condição Inicial')


def resp_senoidal(sys, T, X0, amp): #Resposta a uma Senoide - Resposta com Entrada Senoidal
  #Para o Botao 4, É NECESSÁRIO TER VALORES DE CONDIÇÃO INICIAL!!

  #Senoide:
  try:
    senoide = np.sin(amp*T)
    t , y = ctl.forced_response(sys,T,senoide, X0)
  except:
    raise Exception('Verifique se a função não é imprópria( nº de zeros > nº de polos)')
  
  plotar_grafico(t, y, 'Resposta a uma Senoide de Amplitude %.2f'%amp)
