import numpy as np
from scipy.io.wavfile import write
import math

#q1
srate=44100

# Create a sine wave, sampled at 44100Hz. Write to 16-bit PCM, Mono.
def create_sinusoid(frequency=440, dur=1, srate=44100, phase = 0): 
    t = np.linspace(0,dur,int(srate*dur))
    amp = np.iinfo(np.int16).max
    data = amp * np.sin(2*np.pi*frequency *t+phase)
    return data

data = create_sinusoid(frequency=220, dur=3, srate=44100)
# data2 = create_sinusoid(frequency=440, dur=3, srate=44100)
# sum = np.concatenate((data, data2), axis=None)

# write("Q1.wav", srate, data.astype(np.int16))
write("Q1.wav", srate, data.astype(np.int16))

#q2
# num=440 * 2**((100-69)/12)
# print(round(num))
midiList=[(45,1),(60,1),(68,2)]

def midi_to_freq(midiList: list):
    melody = []
    for midiNote in midiList:
        print("hi")
        if (midiNote[0] < 0 or midiNote[0] > 127):
            print("please enter valid mini note number")
            return
        
        # found this formula here: https://www.music.mcgill.ca/~gary/307/week1/node28.html
        freq = round(440 * 2**((midiNote[0]-69)/12))
        data = create_sinusoid(frequency=freq, dur=midiNote[1])
        melody = np.concatenate((melody, data), axis=None)

    return melody

mel=midi_to_freq(midiList)
write("Q2.wav", srate, mel.astype(np.int16))

#q3