import numpy as np
import matplotlib.pyplot as plt
# specify the file name
filename = 'data/noise/noise1.npy'
# Load the array using numpy
loaded_arr = np.load(filename)
# Flatten the data
loaded_arr= [individual for sublist in loaded_arr for individual in sublist]
len(loaded_arr)
sampling_rate=len(loaded_arr)//60 #in Hz
print(sampling_rate)
fft_result = np.fft.fft(loaded_arr)  #'loaded_arr' is your saved voltage data
n = len(loaded_arr)
frequencies = np.fft.fftfreq(n, d=1/sampling_rate)
plt.plot(frequencies, np.abs(fft_result),color='r')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')

# Identify peaks using, for example, the find_peaks function from scipy
from scipy.signal import find_peaks
peaks, _ = find_peaks(np.abs(fft_result))
peak_frequencies = frequencies[peaks]

plt.show()

