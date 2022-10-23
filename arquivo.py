import os
import control as ctl

def analisando_funcao(funcao, verificador):
  aux = 0
  aux2 = 0
  num1 = 0
  den1 = 0
  num2 = 0
  den2 = 0
  erro='nenhum'

  while True:
    if verificador == 1:
      aux = aux + 1  # Auxiliar pra 2 entradas

    lista = []
    lista.clear()
    for i in range(2):
      #print(i)
      # x=1
      lista = funcao[i + aux2].split()
      # print(lista)
      for j in range(len(lista)):
        try:
          #  x=x+1
          #   print(lista[j])
          # print("entrei")
          lista[j] = float(lista[j])
      #  CONCERTAR AQUI!! if lista[j] == 0.0:
      # print("A linha %d deve conter valor diferente de zero !!!" %x)
      # exit()
      #Se algum elemento da lista for nulo ou zero, encerra-se o programa:

        except:  # Para elemento diferente de int ( k, x, y, etc > variavel string)
          #lista[j] = lista[j]
          
          erro="Erro!! Todos os elementos da função de transferência devem ser números! substituia o valor a variável " + str(lista[j]) + " pelo valor desejado a ser analisado."
             
          return (num1, den1, num2, den2, erro)

      if i == 0:
        if aux == 0 or aux == 1:
          num1 = lista
        else:
          num2 = lista
      else:
        if aux == 0 or aux == 1:
          den1 = lista
          aux2 = 2
        else:
          den2 = lista
    if aux == 0:
      break

    if aux == 2:
      break
    """print(num1)
    print(den1)
    print(num2)
    print(den2)"""

  return (num1, den1, num2, den2, erro)

def recebendo_arquivo(caminho):
  lista_arquivo = []
  lista_arquivo.clear()
  erro='nenhum'
  
  verificador = 0
  j = 0
  #caminho='C:/Users/Caio/Desktop/aloha.txt'
  try:
    arquivo = open(caminho, 'r')
  except:
    erro="Não foi possível abrir o arquivo. Verifique se o nome e localização no diretório do arquivo  estão corretos!!"
    
    arquivo.close()
    return (lista_arquivo, verificador,erro)
  else:
    #Verificando se o arquivo é vazio:
    isempty = os.stat(caminho).st_size == 0
    if isempty == True:
      erro="Arquivo Vazio!! Insira os dados!!"
      return (lista_arquivo, verificador,erro)
    else:
      for i in arquivo:
        j = j + 1
        #print(i)
        if i == "\n":
          j=str(j)
          erro="A linha " + j + "deve conter valor diferente de nulo!!!" 
          return (lista_arquivo, verificador,erro)
        else:
          lista_arquivo.append(i)
        #Parando de ler o arquivo a partir da linha 4:
        if len(lista_arquivo) == 4:
          break

    arquivo.close()
    #print(lista_arquivo)

    # Verificando se a lista tem mais de 2 linhas. Se tiver mais linhas:

  if len(lista_arquivo) > 2:
    verificador = 1

  return (lista_arquivo, verificador,erro)


#________________________________________
# EXIBINDO O RESULTADO!!:
#Funcao de Transferência

def dados_finais(x):
    funcao, verificador,erro = recebendo_arquivo(x)
    if(erro !='nenhum'):
      sys1=0
      sys2=0
      return sys1,sys2,erro

    else:
      num1, den1, num2, den2, erro = analisando_funcao(funcao, verificador)

      if(erro !='nenhum'):
        sys1=0
        sys2=0
        return sys1,sys2,erro

      else:
        #Se o numero de linhas no arquivo igual ou menor que 2:
        if verificador == 0:
            sys1 = ctl.tf(num1, den1)
            sys2 = 0
            error='sem erro'
            print(sys1)

            
        #Se for maior que 2 linhas, indica que tem outro sistema. Logo:
        else:
            sys1 = ctl.tf(num1, den1)
            sys2 = ctl.tf(num2, den2)
            error='sem erro'
            print(sys1)
            print(sys2)

        return sys1,sys2,erro

