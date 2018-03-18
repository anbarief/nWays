#Author: anbarief@live.com
#Date created: 15 Mar 2018

import matplotlib.pyplot as plt
import math
pi = math.pi


ex_1 = "1. Using lists (comprehension) to contain A*sin(a*x), B*cos(b*x), and the superposition. \
Using plt.subplots to created the plots."

def trig_subplots_1(x=[], amplitude=(1, 1), frequency=(1, 1)):

    sine = [amplitude[0]*math.sin(frequency[0]*i) for i in x]
    cosine = [amplitude[1]*math.cos(frequency[1]*i) for i in x]
    superposition = [s+c for s,c in zip(sine, cosine)]

    fig, ax = plt.subplots(3,1)

    ax[0].plot(x, sine)
    ax[0].set_title('Sine wave')

    ax[1].plot(x, cosine)
    ax[1].set_title('Cosine wave')

    ax[2].plot(x, superposition)
    ax[2].set_title('Bichromatic wave')

    plt.tight_layout()
    plt.show()


ex_2 = "2. Generate A*sin(a*x), B*cos(b*x), and the superposition by list.append in a for-loop. \
Using plt.subplots to created the plots."

def trig_subplots_2(x=[], amplitude=(1, 1), frequency=(1, 1)):

    sine, cosine, superposition = [], [], []
    for i in x:
        sine.append( amplitude[0]*math.sin(frequency[0]*i) )
        cosine.append( amplitude[1]*math.cos(frequency[1]*i) )
        superposition.append( sine[-1] + cosine[-1] )

    fig, ax = plt.subplots(3,1)

    ax[0].plot(x, sine)
    ax[0].set_title('Sine wave')

    ax[1].plot(x, cosine)
    ax[1].set_title('Cosine wave')

    ax[2].plot(x, superposition)
    ax[2].set_title('Bichromatic wave')

    plt.tight_layout()
    plt.show()


ex_3 = "3. Similar as no.1, but creating each subplot axes by using plt.subplot(nrows, ncols, index)."

def trig_subplots_3(x=[], amplitude=(1, 1), frequency=(1, 1)):

    sine = [amplitude[0]*math.sin(frequency[0]*i) for i in x]
    cosine = [amplitude[1]*math.cos(frequency[1]*i) for i in x]
    superposition = [s+c for s,c in zip(sine, cosine)]

    plt.subplot(3,1,1)
    plt.title('Sine wave')
    plt.plot(x, sine)

    plt.subplot(3,1,2)
    plt.title('Cosine wave')
    plt.plot(x, cosine)

    plt.subplot(3,1,3)
    plt.title('Bichromatic wave')
    plt.plot(x, superposition)

    plt.tight_layout()
    plt.show()


ex_4 = "4. Similar as no.1, but the superposition wave is generated after plotting the sine and cosine then and \
get the y values from each plot using .get_ydata()."

def trig_subplots_4(x=[], amplitude=(1, 1), frequency=(1, 1)):

    sine = [amplitude[0]*math.sin(frequency[0]*i) for i in x]
    cosine = [amplitude[1]*math.cos(frequency[1]*i) for i in x]

    fig, ax = plt.subplots(3,1)

    sine_plot = ax[0].plot(x, sine)
    ax[0].set_title('Sine wave')

    cosine_plot = ax[1].plot(x, cosine)
    ax[1].set_title('Cosine wave')

    superposition = sine_plot[0].get_ydata() + cosine_plot[0].get_ydata()
    ax[2].plot(x, superposition)
    ax[2].set_title('Bichromatic wave')

    plt.tight_layout()
    plt.show()



x = [i*0.01*pi for i in range(1000)]
amplitude = (1, 1)
frequency = (1, 0.75)

print(ex_1)
trig_subplots_1(x, amplitude, frequency)
print(ex_2)
trig_subplots_2(x, amplitude, frequency)    
print(ex_3)
trig_subplots_3(x, amplitude, frequency)    
print(ex_4)
trig_subplots_4(x, amplitude, frequency)    
