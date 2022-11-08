import control as ctl

import os  #Biblioteca para verificar se o arquivo é vazio ou não


#Analisando se a FT pode ser utilizada ou não (Tratamento das Entradas):
def recebendo_arquivo(caminho):
  lista_arquivo = []
  lista_arquivo.clear()
  verificador = 0
  j = 1
  erro = "sem erro"
  nome= caminho
  arquivo = open(nome, 'r')
  print(arquivo)
  try:    
    arquivo = open(nome, 'r')
  except:
    erro="\nNão foi possível abrir o arquivo. Verifique se o nome e localização no diretório do arquivo  estão corretos!!"
    print(erro)
    
    return (lista_arquivo, verificador,erro)
  else:
    #Verificando se o arquivo é vazio:
    isempty = os.stat(nome).st_size == 0
    if isempty == True:
      erro="Arquivo Vazio!! Insira os dados!!"
      print(erro)
      return (lista_arquivo, verificador,erro)
    else:
      #Analisando cada linha do arquivo
      for i in arquivo:
        if i == "\n" or i == "":
          erro="A linha"+j+ "deve conter valor diferente de nulo!!!"
          print(erro)
          return (lista_arquivo, verificador,erro)
        elif i == "0" or i == "0\n":
          erro="A linha"+j+"deve conter outros valores além do valor zero!! \n"
          print(erro)
          return (lista_arquivo, verificador,erro)
        else:
          lista_arquivo.append(i)
          j = j + 1

    arquivo.close()

    # Se o arquivo tiver pelo menos 4 linhas:
  if len(lista_arquivo) >= 4:
    verificador = 1

    # Se o arquivo tiver pelo menos de  2linhas:
  if len(lista_arquivo) < 2:
    erro="O arquivo deve conter no mínimo deve conter no mínimo de 4 linhas\n"
    print(erro)
    return (lista_arquivo, verificador,erro)

    #Se o arquivo tiver apenas 3 linhas. EXIBIRÁ SOMENTE UM AVISO!!
  if len(lista_arquivo) == 3:
    erro="Se for inserir 2 sistemas, o arquivo deve conter no mínimo 4 linhas\n"
    print(erro)

  print(lista_arquivo,verificador,erro)
  return (lista_arquivo, verificador,erro)


def analisando_funcao(funcao, verificador):
  num1 = 0
  den1 = 0
  num2 = 0
  den2 = 0
  aux = 1
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
          print(
            "Erro!! Todos os elementos da função de transferência devem ser números! substituia o valor a variável '%s' pelo valor desejado a ser analisado \n"
            % lista[j])
          exit()

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
    print(
      "ATENÇÃO!!! Para o SISTEMA 1, o número de zeros (z)  é maior que o número de polos (p) ! Para z > p, o sistema não pode ser modelado fisicamente, podendo gerar inconsistência nos resultados de análise!!"
    )
  if len(num2) > len(den2):
    print(
      "ATENÇÃO!!! Para o SISTEMA 2, o número de zeros (z)  é maior que o número de polos (p)! Para z > p, o sistema não pode ser modelado fisicamente, podendo gerar inconsistência nos resultados de análise!!"
    )

  return (num1, den1, num2, den2)


#_______________________________________

# Extraindo os dados do arquivo. seja arquivo de EE ou FT:

#________________________________________
# EXIBINDO O RESULTADO!!:
#Funcao de Transferência

def dados_finais():
    funcao, verificador = recebendo_arquivo()
    num1, den1, num2, den2 = analisando_funcao(funcao, verificador)

    sys1 = 0
    sys2 = 0

    #Se o numero de linhas no arquivo igual ou menor que 2:
    if verificador == 0:
        sys1 = ctl.tf(num1, den1)
        print("Sistema 1: \n")
        print(sys1)
    #Se for maior que 2 linhas, indica que tem outro sistema. Logo:
    else:
        sys1 = ctl.tf(num1, den1)
        sys2 = ctl.tf(num2, den2)
        print("Sistema 1: \n")
        print(sys1)
        print("Sistema 2: \n")
        print(sys2)


recebendo_arquivo('C:/Users/Caio/kivy_venv/app/Projeto/testes/teste.txt')