import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure(figsize=(8,3))

#intervalo de tempo
t = np.arange(-1, 5, 0.01)

def f1(t):
    return (t > 1) * (t < 3) * abs(np.sin(2*np.pi*t))

def f2(t):
    return 0.8*(abs(t-0.2)<0.5)

#faz a integral do produto entre f1 e a f2 invertida
convolution = np.zeros(len(t))
for n, itT in enumerate(t):
    convolution[n] = scipy.integrate.simps(f1(t) * f2(itT-t), t)

def update(t0, f1, f2):
    plt.clf()

    #primeiro plot
    plt.subplot(211)
    plt.plot(t, f1(t)) #plota f1
    plt.plot(t, f2(t0-t)) #plota f2 invertida
    plt.fill(t, f1(t) * f2(t0-t), color='r', alpha=0.5) #preenchimento com a interceccao entre as duas
    plt.grid()
    
    #segundo plot
    plt.subplot(212)
    plt.plot(t, convolution) #plota convolucao
    plt.plot(t0, scipy.integrate.simps(f1(t) * f2(t0-t), t), 'ro') #plota ponto atual
    plt.grid()

#animacao
anim = animation.FuncAnimation(fig, update, frames=np.arange(0,5.0, 0.05), fargs=(f1,f2), interval=80)
plt.show()