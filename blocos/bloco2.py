import control as ctl
import matplotlib.pyplot as plt
import numpy as np
from control.matlab import *

P = ctl.tf([0, 4], [1, 2, 3])# Função de transferencia
P_ss = ctl.tf2ss(P) #transformar função de transferencia em espaço estado
P_tf = ctl.ss2tf(P_ss)# transformar espaço estado para função de transferencia

print(P)

print(P_ss)

print(P_tf)


def resp_impulso_unitario(m, n):
  #Resposta ao Impulso Unitario
  print('\nResposta ao Impulso Unitario\n')
  T = np.arange(m, n, 0.01)
  t1, y1 = impulse(P, T)
  
  plotar_grafico(t1, y1, 'Resposta ao Impulso Unitário')

def resp_degrau_unitario(m, n):
  #Resposta ao Degral Unitario
  print('Resposta ao Degrau Unitário\n')
  T = np.arange(m, n, 0.01)
  t1, y1 = ctl.step_response(P, T)
  
  plotar_grafico(t1, y1, 'Resposta ao Degrau Unitário')
  
def resp_condicao_inicial(m, k, n):
  #Resposta com uma condição inicial
  print('Resposta com uma condição inicial\n')
  
  print(n)
  
  T = np.arange(m, k, 0.01)
  u = np.sin(T)
  y1, t1 = initial(P_ss, T, n)
  
  plotar_grafico(t1, y1, 'Resposta com uma condição inicial')

def resp_forcada(m, k, n):
  #Resposta Forçada
  print('Resposta Resposta Forçada\n')

  print(n)
    
  T = np.arange(m, k, 0.01)
  U = np.sin(5*T)
 
  y1, t1, x0 = lsim(P_ss, U, T, n)
  
  plotar_grafico(t1, y1, 'Resposta Resposta Forçada')

def plotar_grafico(t, y, title=""):
  plt.plot(t, y)
  plt.title(title)
  plt.xlabel('tempo (s)')
  plt.ylabel('amplitude')
  plt.show() 
