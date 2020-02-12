import numpy as np
import scipy.io as sio
import scipy.io.wavfile
import matplotlib.pyplot as plt
from scipy import fftpack
import RPi.GPIO as GPIO
import time

samplerate, data = sio.wavfile.read('test.wav')
times = np.arange(len(data))/float(samplerate)

fftsize = 16000
segment_size = 16000
segment = data

data_fft = fftpack.fft(data[0:segment_size], fftsize)
data_freq = fftpack.fftfreq(fftsize, 1/samplerate)
peak_freq = data_freq[np.argmax(data_fft)]
print("peak frequency:" + str(peak_freq))

# set PWM output
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
myPwm = GPIO.PWM(18, 1000)

# calculate duty ratio
duty = 100*peak_freq/(800 - 100)
duty = np.clip(duty, 0, 100)
print("duty ratio:" + str(duty))
myPwm.start(duty)

# output PWM signal for 5 seconds
try:
    print("PWM output enabled for 5 seconds")
    start = time.time()
    while (time.time()-start) < 5:
        continue
except:
    pass

# terminate the program
myPwm.stop()
GPIO.cleanup()
print("Terminating the program")


'''
plt.plot(data_freq, data_fft)
plt.xlabel('frequency [Hz]')
plt.ylabel('amplitude')
plt.show()
'''
