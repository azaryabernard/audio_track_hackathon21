import speech_recognition as sr
import re

r = sr.Recognizer()
m = sr.Microphone()

stopCommands = ["stop","stop listening"]

lights_off = re.compile(r'^(?=.*turn)((?=.*lights)|(?=.*light))(?=.*off).*$', re.I)


try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        try :
            with m as source: audio = r.listen(source, timeout = 3, phrase_time_limit = 5)
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

                if lights_off.match(value):
                    print("turning lights off")

                if "stop listening" in value:
                    print("stop listening...")
                    break
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
        
except KeyboardInterrupt:
    pass

