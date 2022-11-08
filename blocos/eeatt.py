import control as ctl

import os  #Biblioteca para verificar se o arquivo é vazio ou não

#Analisando se a EE pode ser utilizada ou não (Tratamento das Entradas):


def analisando_matriz(espaco_estado, verificador, erro3):
  a1 = 0
  b1 = 0
  c1 = 0
  d1 = 0
  a2 = 0
  b2 = 0
  c2 = 0
  d2 = 0
  cont = 1
  if erro3 == 'sem erro':
    erro4 = 'sem erro'

    if verificador == 1:
      cont = 2
    for cont in range(cont):
      for i in range(4):
        linha = 1
        coluna = 0
        #print(linha)
        #print(coluna)
        #Lista que recebe os dados do usuário:
        if cont == 0:
          lista = espaco_estado[i].split()
        else:
          lista = espaco_estado[
            i + 4].split()  # i + 4, pois sao 4 linhas pra cada sistema

        #Analisando os elementos da lista:
        for j in range(len(lista)):
          if lista[j] != ';':
            coluna = coluna + 1
          else:
            coluna = 0
            linha = linha + 1

        #Verificando as matrizes:

        #Analisando Matriz A (n x n)
        if i == 0:
          if cont == 0:
            a1 = espaco_estado[i]
          else:
            a2 = espaco_estado[i + 4]

          linha_a = linha
          coluna_a = coluna
          if linha_a != coluna_a:
            erro4 = "Matriz A do sistema" + str(
              (cont + 1)
            ) + "incorreta!! Essa matriz deve ser uma matriz quadrada!!! \n "
            print(erro4)

            return (a1, b1, c1, d1, a2, b2, c2, d2, erro4)
        #Analisando a Matriz B (n x p)
        if i == 1:
          if cont == 0:
            b1 = espaco_estado[i]
          else:
            b2 = espaco_estado[i + 4]
          linha_b = linha
          coluna_b = coluna
          if linha_b != linha_a:
            erro4 = "Matriz B do sistema" + str(
              (cont + 1)
            ) + "incorreta!!! O número de linhas da Matriz B desse igual  ao numero de linhas da Matriz A!! \n"
            print(erro4)
            return (a1, b1, c1, d1, a2, b2, c2, d2, erro4)
        #Analisando a Matriz C (q x n)
        if i == 2:
          if cont == 0:
            c1 = espaco_estado[i]
          else:
            c2 = espaco_estado[i + 4]
          linha_c = linha
          coluna_c = coluna
          if coluna_c != coluna_a:
            erro4 = "Matriz C do sistema" + str(
              (cont + 1)
            ) + "incorreta!!! O número de colunas da Matriz C desse igual  ao numero de colunas da Matriz A!! \n"
            print(erro4)
            return (a1, b1, c1, d1, a2, b2, c2, d2, erro4)
        #Analisando a Matriz D (q x p )
        if i == 3:
          if cont == 0:
            d1 = espaco_estado[i]
          else:
            d2 = espaco_estado[i + 4]
          linha_d = linha
          coluna_d = coluna
          #Auxiliar pra ajudar a executar as duas condições da matriz D.
          aux = 0
          if linha_d != linha_c:
            erro4 = "Matriz D do sistema" + str(
              (cont + 1)
            ) + "incorreta!!! O número de linhas da Matriz D desse igual  ao numero de linhas da Matriz C!! \n"

            aux = aux + 1
          if coluna_d != coluna_b:
            erro4 = "Matriz D do sistema" + str(
              (cont + 1)
            ) + "incorreta!!! O número de colunas da Matriz D desse igual  ao numero de colunas da Matriz C!! \n"

            aux = aux + 1
          if aux >= 1:
            print(erro4)
            exit()

    return (a1, b1, c1, d1, a2, b2, c2, d2, erro4)
  else:
    print("Erro")
    return (a1, b1, c1, d1, a2, b2, c2, d2, erro4)


#_______________________________________

# Extraindo os dados do arquivo. seja arquivo de EE ou FT:


def recebendo_arquivo(nome):
  lista_arquivo = []
  lista_arquivo.clear()
  verificador = 0
  j = 1
  atencao = ''
  erro = 'sem erro'

  atencao = ''
  try:

    arquivo = open(nome, 'r')
  except:
    erro = "\nNão foi possível abrir o arquivo. Verifique se o nome e localização no diretório do arquivo  estão corretos!!"
    print(erro)
    return (lista_arquivo, verificador, erro)

  else:
    #Verificando se o arquivo é vazio:
    isempty = os.stat(nome).st_size == 0
    if isempty == True:
      erro = "Arquivo Vazio!! Insira os dados!!"
      print(erro)
      return (lista_arquivo, verificador, erro)
    else:
      #Analisando cada linha do arquivo
      for i in arquivo:
        if i == "\n" or i == "":
          erro = "A linha" + j + "deve conter valor diferente de nulo!!!"
          print(erro)
          return (lista_arquivo, verificador, erro)
        elif (i == "0" or i == "0\n") and (j != 4 and j != 8 and j <= 8):
          erro = "A linha" + j + "deve conter outros valores além do valor zero!! \n"
          print(erro)
          return (lista_arquivo, verificador, erro)
        else:
          lista_arquivo.append(i)
          j = j + 1

    arquivo.close()
    #print(lista_arquivo)

    # Se o arquivo tiver pelo mais de  8 linhas:
  if len(lista_arquivo) >= 8:
    verificador = 1

    # Se o arquivo tiver pelo menos de  4 linhas:
  if len(lista_arquivo) < 4:
    erro = "O arquivo deve conter no mínimo deve conter no mínimo de 4 linhas\n"
    print(erro)
    return (lista_arquivo, verificador, erro)

    #Se o arquivo tiver mais de 4 linhas, porém menos de 8 linhas. EXIBIRÁ SOMENTE UM AVISO!!
  if len(lista_arquivo) > 4 and len(lista_arquivo) < 8:
    atencao = "Se for inserir 2 sistemas, o arquivo deve conter no mínimo 8 linhas\n"
    print(atencao)

  return (lista_arquivo, verificador, erro, atencao)


#________________________________________
# EXIBINDO O RESULTADO!!:


#Espaco de Estado:
def dados_finais_EE(x):
  #Definindo Valores iniciais de sys1 e sys2
  sys1 = 0
  sys2 = 0
  atencao_DF = ''
  espaco_estado, verificador, erro2, atencao_RA = recebendo_arquivo(x)
  a1, b1, c1, d1, a2, b2, c2, d2, erro5 = analisando_matriz(
    espaco_estado, verificador, erro2)
  if erro5 == 'sem erro':
    #Se o numero de linhas no arquivo igual ou menor que 2:
    if verificador == 0:
      sys1 = ctl.ss(a1, b1, c1, d1)
      #__________________________________________
      #Exibir ATENÇÃO PARA O USUÁRIO!! NÃO ENCERRA O PROGRAMA!:
      polo1, zero1 = ctl.pzmap(sys1)
      if len(zero1) > len(polo1):
        atencao_DF = "ATENÇÃO!!! Para o SISTEMA 1, o número de zeros (z)  é maior que o número de polos (p) ! Para z > p, o sistema não pode ser modelado fisicamente, podendo gerar inconsistência nos resultados de análise!!"

      #__________________________________________

      #Exibir ao Usuário
      print("Sistema 1:\n")
      print(sys1)
      return (sys1, sys2, atencao_RA, atencao_DF, erro5)

    #Se for maior que 4 linhas, indica que tem outro sistema. Logo:
    else:
      sys1 = ctl.ss(a1, b1, c1, d1)
      sys2 = ctl.ss(a2, b2, c2, d2)

      #__________________________________________
      #Exibir ATENÇÃO PARA O USUÁRIO!! NÃO ENCERRA O PROGRAMA!:
      polo1, zero1 = ctl.pzmap(sys1)
      polo2, zero2 = ctl.pzmap(sys2)

      if len(zero1) > len(polo1):
        atencao_DF = "ATENÇÃO!!! Para o SISTEMA 1, o número de zeros (z)  é maior que o número de polos (p) ! Para z > p, o sistema não pode ser modelado fisicamente, podendo gerar inconsistência nos resultados de análise!!"

      if len(zero2) > len(polo2):
        atencao_DF = "ATENÇÃO!!! Para o SISTEMA 2, o número de zeros (z)  é maior que o número de polos (p) ! Para z > p, o sistema não pode ser modelado fisicamente, podendo gerar inconsistência nos resultados de análise!!"

      #__________________________________________

      #Exibir para o usuário:
      print("Sistema 1:\n")
      print(sys1)
      print("Sistema 2:\n")
      print(sys2)
      print(atencao_RA)
      print(erro5)
      print(atencao_DF)
      return (sys1, sys2, atencao_RA, atencao_DF, erro5)
  else:
    #Exibir para o usuário:
    print("Sistema 1:\n")
    print(sys1)
    print("Sistema 2:\n")
    print(sys2)
    print(atencao_RA)
    print(erro5)
    print(atencao_DF)
    return (sys1, sys2, atencao_RA, atencao_DF, erro5)



