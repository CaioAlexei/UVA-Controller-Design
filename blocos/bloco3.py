import control as ctl
import matplotlib.pyplot as plt


def diagrama_bode(freq_min, freq_max,sys):

    #sys = ctl.ss("1. -2; 3. -4", "5.; 7", "6. 8", "9.")
    #sys = ctl.tf([1, 2, 3, 4], [1, 2]) 

    # Gráfico 1
    mag, phase, omega = ctl.bode_plot(sys, dB=True)

    plt.show()
    
    #Grafico 2
    ctl.bode_plot(sys, omega=[freq_min, freq_max], dB=True) 

    #Como fazer subplot??
    plt.show()


def diagrama_nyquist(sys):
    ctl.nyquist_plot(sys)
    plt.show()

