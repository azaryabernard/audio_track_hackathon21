import numpy as np
import librosa
import matplotlib.pyplot as plt
#import noisereduce as nr
from keras.models import model_from_json
from sklearn.preprocessing import LabelEncoder
import IPython
from tensorflow import keras
import os
from scipy.io.wavfile import read
import noisereduce as nr

os.chdir('/Users/azaryabernard/_HACKATHON/audio_track_hackathon21')

#Load segment audio classification model
model = keras.models.load_model('Main/testmodel.model')

# Replicate label encoder
lb = LabelEncoder()
lb.fit_transform(['air_conditioner', 'car_horn', 'children_playing', 'dog_bark', 'drilling',  'engine_idling', 'gun_shot', 'jackhammer', 'siren', 'street_music'])

#Some Utils

# Plot audio with zoomed in y axis
def plotAudio(output):
    fig, ax = plt.subplots(nrows=1,ncols=1, figsize=(20,10))
    plt.plot(output, color='blue')
    ax.set_xlim((0, len(output)))
    ax.margins(2, -0.1)
    plt.show()

# Plot audio
def plotAudio2(output):
    fig, ax = plt.subplots(nrows=1,ncols=1, figsize=(20,4))
    plt.plot(output, color='blue')
    ax.set_xlim((0, len(output)))
    plt.show()

# Split a given long audio file on silent parts.
# Accepts audio numpy array audio_data, window length w and hop length h, threshold_level, tolerence
# threshold_level: Silence threshold
# Higher tolence to prevent small silence parts from splitting the audio.
# Returns array containing arrays of [start, end] points of resulting audio clips
def split_audio(audio_data, w, h, threshold_level, tolerence=10):
    print("masuk0")
    split_map = []
    start = 0
    data = np.abs(audio_data)
    print(np.mean(data))
    threshold = threshold_level*np.mean(data[:25000])
    inside_sound = False
    near = 0
    print("threshold")
    print(threshold)
    for i in range(0,len(data)-w, h):
        win_mean = np.mean(data[i:i+w])
        #print("mean")
        #print(win_mean)
        if(win_mean>threshold and not(inside_sound)):
            print("MASUK1")
            inside_sound = True
            start = i
        if(win_mean<=threshold and inside_sound and near>tolerence):
            inside_sound = False
            near = 0
            print("MASUK2")
            split_map.append([start, i])
        if(inside_sound and win_mean<=threshold):
            print("MASUK3")
            near += 1
    return split_map

def minMaxNormalize(arr):
    mn = np.min(arr)
    mx = np.max(arr)
    return (arr-mn)/(mx-mn)

def predictSound(X):
    stfts = np.abs(librosa.stft(X, n_fft=512, hop_length=256, win_length=512))
    stfts = np.mean(stfts,axis=1)
    stfts = minMaxNormalize(stfts)
    print(np.array([stfts]))
    result = model.predict(np.array([stfts]))
    predictions = [np.argmax(y) for y in result]
    return lb.inverse_transform([predictions[0]])[0]

#noisy_part = raw_audio[0:50000]  # Empherically selected noisy_part position for every sample
#nr_audio = nr.reduce_noise(audio_clip=data, noise_clip=noisy_part, verbose=False)
audiodir = 'Main/UrbanSound8K/audio/fold5/111671-8-0-14.wav'

def extract_features(file_name):
    audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast') 
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfccs_processed = np.mean(mfccs.T,axis=0)
     
    return mfccs_processed


raw_audio, sr = librosa.load(audiodir)
noisy_part = raw_audio[0:50000]  # Empherically selected noisy_part position for every sample
audionp = nr.reduce_noise(audio_clip=raw_audio, noise_clip=noisy_part, verbose=False)

#print(audionp)

#plotAudio2(audionp)
#print("len audio: " + str(len(audionp)))
sound_clips = split_audio(audionp, 10000, 2500, 2)

print("MASUK!K!!!!")
print(sound_clips)
print("!!!!!")

for intvl in sound_clips:
    print("INTVL")
    print(intvl)
    print("MASUK!!!")
    clip, index = librosa.effects.trim(audionp[intvl[0]:intvl[1]], top_db=20, frame_length=512, hop_length=64) # Empherically select top_db for every sample
    print("CLIP")
    print(clip)
    print(predictSound(clip))
    plotAudio2(clip)
    IPython.display.display(IPython.display.Audio(data=clip, rate=sr))