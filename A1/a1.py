import numpy as np
from scipy.io.wavfile import write
import math
from scipy import signal

#q1
srate=44100

# Create a sine wave, sampled at 44100Hz. Write to 16-bit PCM, Mono.
def create_sinusoid(frequency=440, dur=1, srate=44100, phase = 0): 
    t = np.linspace(0,dur,int(srate*dur))
    print(t.size)

    amp = np.iinfo(np.int16).max
    data = amp * np.sin(2*np.pi*frequency *t+phase)
    print(data.size)
    return data

data = create_sinusoid(frequency=440, dur=3, srate=44100)

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

# mel=midi_to_freq(midiList)
# write("Q2.wav", srate, mel.astype(np.int16))

#q3
# [noteon, time, pitch(frequency)]
SKINIlist = ["NoteOn          2 220",
    "NoteOff         3 110",
    "NoteOn          1 440"]


def SKINI_to_sound(skiniList: list[str]):
    melody = []

    for oneLine in skiniList:
        skiniMsg = oneLine.split()

        if (len(skiniMsg) != 0):
            data = create_sinusoid(frequency=int(skiniMsg[2]), dur=int(skiniMsg[1]))
            melody = np.concatenate((melody, data), axis=None)

    return melody

# mel=SKINI_to_sound(SKINIlist)
# write("Q3.wav", srate, mel.astype(np.int16))

#q4
def triangle_wave(freq, dur=1.0, srate=44100):

	t = np.arange(0, dur, 1.0/srate)
	x = np.zeros(t.shape[0])
	for i in range(4):
		n = 2*i + 1
		x += ((-1)**i)*(n**(-2))*(np.sin(2*np.pi*freq*n*t))
	return (8/(np.pi**2)) * x

# triangle_data = triangle_wave(freq=660, dur=3, srate=44100)
# write("triangle.wav", srate, triangle_data.astype(np.int16))


def square_wave(freq, dur=1.0, srate=44100):

	t = np.arange(0, dur, 1.0/srate)
	return 2 * (2*np.floor(freq*t) - np.floor(2*freq*t)) + 1

# square_data = square_wave(freq=440, dur=3, srate=44100)
# write("square.wav", srate, data.astype(np.int16))


def sawtooth_wave(freq, dur=1.0, srate=44100):

	t = np.arange(0, dur, 1.0/srate)
	return signal.sawtooth(2 * freq * np.pi * t)

# sawtooth_data = sawtooth_wave(freq=440, dur=3, srate=44100)
# write("sawtooth.wav", srate, sawtooth_data.astype(np.int16))

#q5
def create_sinusoid_buffered(freq=440, dur=1, srate=44100, bufferSize=256, phase=0): 
    t = np.linspace(0,dur,int(srate*dur))

    bufferNum = int((srate*dur) / bufferSize)
    amp = np.iinfo(np.int16).max
    total = []
    for i in range(bufferNum):
        data = amp * np.sin(2*np.pi*freq *t[int(bufferSize*i):int(bufferSize*(i+1))]+phase)
        total = np.concatenate((total, data), axis=None)

    return total

# data = create_sinusoid_buffered(freq=660, dur=5, srate=44100, bufferSize=512)
# write("buffered.wav", srate, data.astype(np.int16))

#q6
def polyphony(dataList:list):
    sum = []
    amp = np.iinfo(np.int16).max
    for data in dataList:
        t = np.linspace(0,data[1],int(data[2]*data[1]))
        oneSound = amp * np.sin(2*np.pi*data[0] *t)
        if sum == []:
            sum = np.zeros(int(data[2]*data[1]))
        sum = np.add(sum, oneSound)
    
    return sum

soundList = [[220, 3, 44100],[440, 3, 44100],[660, 3, 44100]]

polyphony_data = polyphony(soundList)
write("polyphony.wav", srate, polyphony_data.astype(np.int16))
