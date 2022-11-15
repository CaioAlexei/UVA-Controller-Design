import os  # Biblioteca para verificar se o arquivo é vazio ou não

import control as ctl

#Analisando se a FT pode ser utilizada ou não (Tratamento das Entradas):


def analisando_funcao(funcao, verificador):
  num1 = 0
  den1 = 0
  num2 = 0
  den2 = 0
  aux = 1
  erro3 = 'sem erro'
  apto_root_locus = True
  atencao3=''
  #Criando Auxiliar pra 2 entradas:

  if verificador == 1:
    aux = 2

  for cont in range(aux):
    lista = []
    lista.clear()
    for i in range(2):
      if cont == 0:
        lista = funcao[i].split()
      else:
        lista = funcao[i + aux].split()
      for j in range(len(lista)):
        try:
          lista[j] = float(lista[j])
        except:  # Para elemento diferente de int ( k, x, y, etc > variavel string)
          #lista[j] = lista[j]
          erro3 = "Erro!! Todos os elementos da função de transferência devem ser números! substituia o valor a variável" + str(
            lista[j]) + "pelo valor desejado a ser analisado \n"
          print(erro3)
          raise Exception(erro3)

      if i == 0:
        if cont == 0:
          num1 = lista
        else:
          num2 = lista
      else:
        if cont == 0:
          den1 = lista
        else:
          den2 = lista

  #Exibir ATENÇÃO PARA O USUÁRIO!! NÃO ENCERRA O PROGRAMA!:
  if len(num1) > len(den1):
    atencao3 = "ATENÇÃO!!! Para o SISTEMA 1, o número de zeros (z)  é maior que o número de polos (p) ! Para z > p, o sistema não pode ser modelado fisicamente, podendo gerar inconsistência nos resultados de análise!!"
    apto_root_locus = False
    print(atencao3)

  if len(num2) > len(den2):
    atencao3 += " ATENÇÃO!!! Para o SISTEMA 2, o número de zeros (z)  é maior que o número de polos (p)! Para z > p, o sistema não pode ser modelado fisicamente, podendo gerar inconsistência nos resultados de análise!!"
    print(atencao3)
  
  return (num1, den1, num2, den2, erro3, atencao3, apto_root_locus)


#_______________________________________

# Extraindo os dados do arquivo. seja arquivo de EE ou FT:


def recebendo_arquivo(nome):
  lista_arquivo = []
  lista_arquivo.clear()
  verificador = 0
  j = 1
  erro = 'sem erro'
  atencao = ''
  try:

    arquivo = open(nome, 'r')
  except:
    erro = "\nNão foi possível abrir o arquivo. Verifique se o nome e localização no diretório do arquivo estão corretos!!"
    print(erro)
    raise Exception(erro)
  else:
    #Verificando se o arquivo é vazio:
    isempty = os.stat(nome).st_size == 0
    if isempty == True:
      erro = "Arquivo Vazio!! Insira os dados!!"
      print(erro)
      raise Exception(erro)
    else:
      #Analisando cada linha do arquivo
      for i in arquivo:
        if i == "\n" or i == "":
          erro = "A linha" + j + "deve conter valor diferente de nulo!!!"
          print(erro)
          raise Exception(erro)
        elif i == "0" or i == "0\n":
          erro = "A linha" + j + "deve conter outros valores além do valor zero!! \n"
          print(erro)
          raise Exception(erro)
        else:
          lista_arquivo.append(i)
          j = j + 1

    arquivo.close()

    # Se o arquivo tiver pelo menos 4 linhas:
  if len(lista_arquivo) >= 4:
    verificador = 1

    # Se o arquivo tiver pelo menos de  2linhas:
  if len(lista_arquivo) < 2:
    erro = "O arquivo deve conter no mínimo deve conter no mínimo de 4 linhas\n"
    print(erro)
    raise Exception(erro)

    #Se o arquivo tiver apenas 3 linhas. EXIBIRÁ SOMENTE UM AVISO!!
  if len(lista_arquivo) == 3:
    atencao = "Se for inserir 2 sistemas, o arquivo deve conter no mínimo 4 linhas\n"
    print(erro)

  return (lista_arquivo, verificador, erro, atencao)


#________________________________________
# EXIBINDO O RESULTADO!!:
#Funcao de Transferência
def dados_finais_FT(x):
  sys1 = 0
  sys2 = 0
  funcao, verificador, erro2, atencao2 = recebendo_arquivo(x)

  if (erro2 == 'sem erro'):
    num1, den1, num2, den2, erro4, atencao4, apto_root_locus = analisando_funcao(
      funcao, verificador)

  else:
    return (sys1, sys2, erro2, atencao2, apto_root_locus)

  #Se o numero de linhas no arquivo igual ou menor que 2:

  if (erro4 == 'sem erro'):

    if verificador == 0:
      sys1 = ctl.tf(num1, den1)
      print("Sistema 1: \n")
      print(sys1)
      return (sys1, sys2, erro4, atencao4, apto_root_locus)
    #Se for maior que 2 linhas, indica que tem outro sistema. Logo:
    else:
      sys1 = ctl.tf(num1, den1)
      sys2 = ctl.tf(num2, den2)
      print("Sistema 1: \n")
      print(sys1)
      print("Sistema 2: \n")
      print(sys2)
      return (sys1, sys2, erro4, atencao4, apto_root_locus)
  else:

    return (sys1, sys2, erro4, atencao4, apto_root_locus)



