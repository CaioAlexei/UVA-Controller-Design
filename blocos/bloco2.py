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
    
def FuncaoTempo():
  #X0 = []
  aux = 0
  #Se a pessoa não quiser definir o tempo, basta deixar a variável em branco.
  try:
    tempo_inicial = input("Digite o tempo inicial: \n")
    if (tempo_inicial != ''):
      tempo_inicial = float(tempo_inicial)
    else:
      aux = aux + 1
    print(tempo_inicial)
  except:
    print("Valor errado!!! Digite um NÚMERO!!")
    exit()
  try:
    tempo_final = input("Digite o tempo final: \n")
    if tempo_final != '':
      tempo_final = float(tempo_final)
    else:
      aux = aux + 1
    print(tempo_final)
  except:
    print("Valor errado!!! Digite um NÚMERO!!")
    exit()
  #Condição Inicial (X0):
  try:
    X0 = input("Digite o valor da condição inicial: \n")
    if X0 != '':
      X0 = float(X0)
    else:
      X0 = 0.0
  except:
    print("Valor errado!!! Digite um NÚMERO!!")
    exit()

#Verificação para envio de Dados ( T e X0)
  if aux == 2:
    T = None
  elif aux == 1:
    if tempo_final == '':
      print(" Para a simução, é necessário informar o valor do tempo final")
      exit()
    else:
      #Valor Padrão de tempo_inicial:0
      tempo_inicial = 0
      #Criando vetor de tempo_inicial a tempo_final, com passo de 0.01, para plotagem de gráfico.
      T = np.arange(tempo_inicial, tempo_final, 0.01)
  else:
    #Criando vetor de tempo_inicial a tempo_final, com passo de 0.01, para plotagem de gráfico.
    T = np.arange(tempo_inicial, tempo_final, 0.01)
  return (T, X0, aux)

# sys1 = ctl.tf(1, [1, 0])  #Teste de vericidade
# print(sys1)
# #Entrada_teste:

# sys1 = ctl.tf([0, 4], [1, 2, 3])  # Função de transferencia

# T, X0 , aux= FuncaoTempo()


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


def resp_degrau_unitario(sys, T):

  t, y = ctl.step_response(sys, T, [[1][2]])

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
