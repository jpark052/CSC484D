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

data = create_sinusoid(frequency=440, dur=3, srate=44100)
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
# [noteon, time, pitch(frequency)]
SKINIlist = ["NoteOn          2 220",
    "NoteOff         3 110",
    "NoteOn          1 440"]


def SKINI_to_sound(skiniList: list[str]):
    melody = []
    print(SKINIlist)

    for oneLine in skiniList:
        print(oneLine)
        skiniMsg = oneLine.split()

        if (len(skiniMsg) != 0):
            data = create_sinusoid(frequency=int(skiniMsg[2]), dur=int(skiniMsg[1]))
            melody = np.concatenate((melody, data), axis=None)

    return melody

mel=SKINI_to_sound(SKINIlist)
write("Q3.wav", srate, mel.astype(np.int16))

#q4
