#Bloco 1
import control as ctl


#Botao 1: De FT para EE
def FT_EE(sys1, sys2):
  #Exemplo de entrada:
  resultado2 = sys2
  resultado = ctl.tf2ss(sys1)
  if (sys2 != 0):
    resultado2 = ctl.tf2ss(sys2)

  #Exibir para o usuario
  return resultado, resultado2


#Botao2: De EE para FT
def EE_FT(sys1, sys2):
  #exemplo de entrada:
  resultado2 = sys2

  resultado = ctl.ss2tf(sys1)
  if (sys2 != 0):
    resultado2 = ctl.ss2tf(sys2)

  #Exibir para o usuario
  return resultado, resultado2
