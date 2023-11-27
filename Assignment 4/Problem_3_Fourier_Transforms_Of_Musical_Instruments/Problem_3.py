import numpy as np
from numpy.fft import fft, fftfreq
import matplotlib.pyplot as plt
import seaborn as sns
import sys

sns.set_style('darkgrid')
sys.path.insert(0, '.')

piano = np.loadtxt(r'piano.txt')
n_p = len(piano)

trumpet = np.loadtxt(r'trumpet.txt')
n_t = len(trumpet)

# Setting the sample spacing
d_given = 1 / 44100

# Plotting the waveform given
plt.plot(np.arange(0, n_p), piano)
plt.xlabel('Sample')
plt.ylabel('Measured Value')
plt.title('Plot showing the waveform of a Piano')
plt.show()

# Implementing the FFT for the above waveform
s_piano = fft(piano)
freq_piano = fftfreq(n_p, d = d_given)

plt.plot(freq_piano[0: 10**4], abs(s_piano[0: 10**4])**2)
plt.xlabel('Frequency')
plt.title('Discrete Fourier Transform of Piano Waveform')
plt.show()

f_max_Piano = freq_piano[np.argmax(s_piano)]

# Repeating the above exercise for the trumpet
# Plotting the waveform given
plt.plot(np.arange(0, n_t), trumpet)
plt.xlabel('Sample')
plt.ylabel('Measured Value')
plt.title('Plot showing the waveform of a Trumpet')
plt.show()

# Implementing the FFT for the above waveform
s_trumpet = fft(trumpet)
freq_trumpet = fftfreq(n_t, d = d_given)

plt.plot(freq_trumpet[0: 10**4], abs(s_trumpet[0: 10**4])**2)
plt.xlabel('Frequency')
plt.title('Discrete Fourier Transform of Trumpet Waveform')
plt.show()

f_max_Trumpet = freq_trumpet[np.argmax(s_trumpet)]

print(f"The most predominant frequency in the piano waveform is: {f_max_Piano} Hz")
print(f"The most predominant frequency in the trumpet waveform is: {abs(f_max_Trumpet)} Hz")

# The question in part (b) relating to the note being played is answered in the remarks given in
# the file 'Problem_3_Output.txt'