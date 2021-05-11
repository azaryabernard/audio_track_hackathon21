import speech_recognition as sr
import re
import philips_hue as ph
import pyaudio
import wave

r = sr.Recognizer()
m = sr.Microphone()

stopCommands = ["stop","stop listening","turn off"]
callCommand = ["OK Google" , "hey Google" , "hey Alexa" , "Alexa", "hey", "hey Jeffrey","Jeffrey"]

def Record():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return WAVE_OUTPUT_FILENAME


def processCommand(speech):

    for cmd in callCommand:
        if (cmd in speech):
            print("call command specified")
            break
    else:
        return

    lights_on = re.compile(r'^(?=.*turn)((?=.*lights)|(?=.*light))(?=.*on).*$', re.I)
    lights_off = re.compile(r'^(?=.*turn)((?=.*lights)|(?=.*light))(?=.*off).*$', re.I)
    play_song = re.compile(r'^(?=.*play)((?=.*song)|(?=.*something)).*$', re.I)

    if lights_on.match(speech):
        ph.turn_on_group('lights')
        print("turning lights on")
        return
    
    if lights_off.match(speech):
        ph.turn_off_group('lights')
        print("turning lights off")
        return
    
    if play_song.match(speech):
        print("playing a song")
        return

    for stopCmd in stopCommands:
        if stopCmd in value:
            print("stop listening...")
            exit()
    
keywords_lights_off = re.compile(r'^(?=.*turn)((?=.*lights)|(?=.*light))(?=.*off).*$', re.I)
keywords_lights_on = re.compile(r'^(?=.*turn)((?=.*lights)|(?=.*light))(?=.*on).*$', re.I)

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        try :
            with m as source: audio = r.listen(source, timeout = 3, phrase_time_limit = 7)
        except sr.WaitTimeoutError as e:
            print("Timeout!")
            print(e)
            continue
        except Exception as e:
            print(e)

        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)

            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes:  # this version of Python uses bytes for strings (Python 2)

                print(u"You said {}".format(value).encode("utf-8"))

            else:  # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(value))

                processCommand(value)

        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
        
except KeyboardInterrupt:
    pass

