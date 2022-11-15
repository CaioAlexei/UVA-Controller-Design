import control as ctl

# As duas entradas devem ser do mesmo sistema:

# Se o sistema 1 for escolhido como EE, o sistema 2 também deve ser EE:

# Se o sistema 1 for escolhido como FT, o sistema 2 tambem deve ser FT:

# Simulacao do botao  atraves das entradas no terminal:

#Botao Serie
def serie_bl4(sys1,sys2):
  serie = ctl.series(sys1, sys2)
  print(serie)
  return serie
#Botao Paralelo
def paralelo_bl4(sys1,sys2):
  paralelo = ctl.parallel(sys1, sys2)
  print(paralelo)
  return paralelo

#Botao Feedback (Realimentação)

#Botões Secundário:

#Realimentacao Negativa
def reali_neg(sys1,sys2):  
    realimentacao = ctl.feedback(sys1, sys2, -1)
    print(realimentacao)
    return realimentacao
# Realimentacao Positiva
def reali_posi(sys1,sys2):
    realimentacao = ctl.feedback(sys1, sys2, 1)
    print(realimentacao)
    return realimentacao
