from filter import output_audio_file
import speech_recognition as sr
import re
import philips_hue as ph
import soundclassify as sc
import pyaudio
import wave

from jesica4 import create_dashboard
from jesica4 import command_light
from jesica4 import command_SoundSystem
from jesica4 import command_Door
from jesica4 import command_detectsound

r = sr.Recognizer()
m = sr.Microphone()

stopCommands = ["stop","stop listening"]
callCommand = ["OK Google" , "hey Google" , "hey Alexa" , "Alexa", "hey", "hey Jeffrey","Jeffrey","hey Dennis"]

command_light(True, '#FFC200', 'Turn on the light Jesica to red')
command_SoundSystem('On', 30, 'Can you turn on the speakers to 30%')
command_Door('Open', 'Please open the door')
command_detectsound('dog_bark')

app = create_dashboard()
app.run_server(debug=True)

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

    for stopCmd in stopCommands:
        if stopCmd in value:
            print("stop listening...")



            exit()

    for cmd in callCommand:
        if (cmd in speech):
            print("call command specified")
            break
    else:
        return

    lights_on = re.compile(r'^(?=.*turn)((?=.*lights)|(?=.*light))(?=.*on).*$', re.I)
    lights_off = re.compile(r'^(?=.*turn)((?=.*lights)|(?=.*light))(?=.*off).*$', re.I)
    decrease_brightness = re.compile(r'^(?=.*decrease)(?=.*brightness).*$', re.I)
    increase_brightness = re.compile(r'^(?=.*increase)(?=.*brightness).*$', re.I)
    set_brightness = re.compile(r'^(?=.*set)(?=.*brightness).*$', re.I)
    rotate_color = re.compile(r'^(?=.*rotate)((?=.*color)|(?=.*colour)).*$', re.I)
    set_color = re.compile(r'^(?=.*set)((?=.*color)|(?=.*colour)).*$', re.I)
    
    play_song = re.compile(r'^(?=.*play)*((?=.*song)|(?=.*something)).*$', re.I)
    stop_song = re.compile(r'^(?=.*stop)*((?=.*playing)|(?=.*music)).*$', re.I)
    pause_song = re.compile(r'^(?=.*pause)*((?=.*song)|(?=.*music))*.*$', re.I)
    increase_volume = re.compile(r'^((?=.*increase)(?=.*volume))|((?=.*make)(?=.*louder)).*$', re.I)
    decrease_volume = re.compile(r'^((?=.*decrease)(?=.*volume))|((?=.*make)(?=.*softer)).*$', re.I)

    increase_temperature = re.compile(r'^(?=.*increase)(?=.*temperature).*$', re.I)
    decrease_temperature = re.compile(r'^(?=.*decrease)(?=.*temperature).*$', re.I)

    open_door = re.compile(r'^(?=.*open)(?=.*door).*$', re.I)
    close_door = re.compile(r'^(?=.*close)(?=.*door).*$', re.I)

    if lights_on.match(speech):
        ph.turn_on_group('lights')
        print("turning lights on")
        return
    
    if lights_off.match(speech):
        ph.turn_off_group('lights')
        print("turning lights off")
        return
    
    if decrease_brightness.match(speech):
        ph.decrease_brightness_group('lights')
        print("decreasing brightness")
        return

    if increase_brightness.match(speech):
        ph.increase_brightness_group('lights')
        print("decreasing brightness")
        return

    if set_brightness.match(speech):
        temp = re.findall(r'\d+', speech)
        percentage = list(map(int, temp))
        
        if percentage[0] > 100:
            ph.set_brightness_group('lights', 100)
            print("setting brightness to 100%")
        elif percentage[0] < 0:
            ph.set_brightness_group('lights', 0)
            print("setting brightness to 0%")
        else:
            ph.set_brightness_group('lights', percentage[0])
            print("setting brightness to " + str(percentage[0]) + "%")

        return

    if set_color.match(speech):
        temp = speech.split(" ")
        color = temp[-1]
        ph.set_color('lights', color)
        return

    if rotate_color.match(speech):
        ph.rotate_color()
        return

    if play_song.match(speech):
        print("playing a song")
        return
    
    if stop_song.match(speech):
        print("stopping song")
        return
    
    if pause_song.match(speech):
        print("pausing a song")
        return

    if increase_volume.match(speech):
        print("increasing volume")
        return

    if decrease_volume.match(speech):
        print("decreasing volume")
        return

    if increase_temperature.match(speech):
        print("increasing the temperature")
        return
    
    if decrease_temperature.match(speech):
        print("decreasing the temperature")
        return
    
    if open_door.match(speech):
        print("opening door")
        return
    
    if close_door.match(speech):
        print("closing door")
        return

    if("identify" in speech):
        #todo
        #filtered = output_audio_file(Record())
        #print(filtered)
        sc.classify(Record())
        return

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

