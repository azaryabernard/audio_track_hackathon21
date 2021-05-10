from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
import numpy as np
import librosa
import matplotlib.pyplot as plt

file_name = '/Users/brigittajesica/Downloads/146186-5-0-0.wav'

def extract_features(file_name):
    audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast') 
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfccs_processed = np.mean(mfccs.T,axis=0)
     
    return mfccs_processed

#Load segment audio classification model
model = keras.models.load_model('Main/testmodel.model')
# Replicate label encoder
lb = LabelEncoder()
lb.fit_transform(['air_conditioner', 'car_horn', 'children_playing', 'dog_bark', 'drilling',  'engine_idling', 'gun_shot', 'jackhammer', 'siren', 'street_music'])

data = extract_features(file_name)
print(type(data))
print(data.shape)

data = data.reshape(1,40)

result = model.predict(data)
print(result)
predictions = [np.argmax(y) for y in result]
print(lb.inverse_transform([predictions[0]])[0])