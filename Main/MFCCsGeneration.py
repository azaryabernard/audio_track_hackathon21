#### Dependencies ####
import IPython.display as ipd
import numpy as np
import pandas as pd
import librosa
import librosa.display
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('agg')
import tensorflow as tf
from scipy.io import wavfile as wav
#### Dependencies ####

fn = 'UrbanSound8K/audio/fold9/7975-3-0-0.wav'
librosa_audio, librosa_sample_rate = librosa.load(fn)
scipy_sample_rate, scipy_audio = wav.read(fn)
mfccs = librosa.feature.mfcc(y=librosa_audio, sr=librosa_sample_rate, n_mfcc=40)

print(mfccs)
print(mfccs.shape)

print("END OF SESSION")


