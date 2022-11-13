import control as ctl
import matplotlib.pyplot as plt
import numpy as np


def mapa_polos_zeros(sys1):

    #Obtendo polos:
    polos = ctl.poles(sys1)
    #Obtendo Zeros:
    zeros = ctl.zeros(sys1)
    #Gerando gráfico de Polos e Zeros
    ctl.pzmap(sys1, plot=True, title='Mapa de Polos e Zeros')
    
    #Exibir para o Usuário:
    #Sistema
    #Polos
    #Zeros
    #Gráfico:
    plt.show()

    return polos, zeros

def margem_estabilidade(sys1):
    """
        gm = Margem de magnitude (gain margin)
        pm = Margem de fase (phase margin)
        wpc = Frequência de cruzamento de fase (onde a fase cruza -180 graus), que está associada à margem de ganho. (Phase crossover frequency ()
        wgc =  frequência de cruzamento de magnitude (onde o ganho cruza 1), que está associado à margem de fase. (Gain crossover frequency (where gain crosses 1), which is associated with the phase margin. )
    """
    #Essses "_", são pois, a função ctl.stability_margins retorna ao mesmo tempo: gm,pm,sm,wpc,wgc,wms . Onde: sm = margem de estabilidade; wms = Frequencia de margem de estabilidade. Como não se deseja esses, coloca-se o "_".
    gm, pm, _, wpc, wgc, _ = ctl.stability_margins(sys1)
   
    marg_mag = (20 * np.log10(gm))
    
    return marg_mag, pm, wgc, wpc

    #ESTUDAR POSSIBILIDADE! Por enquanto NÃO Considerar!!! SÓ EXIBIR POR ENQUANTO!!

    #arquivo = int(input("Deseja gerar arquivo do sistema?: \n '1': Para SIM , '2':Para NÃO"))

def lugar_raizes(sys1):
    ctl.root_locus(sys1, plot=True, print_gain=True)

    #Exibir para o Usuário:
    #Sistema:
    #Gráfico:
    plt.show()
