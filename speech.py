import speech_recognition as sr

def listenAudio():
    # obtain audio from the microphone
    r = sr.Recognizer()
    WIT_AI_KEY = ""  # Wit.ai keys are 32-character uppercase alphanumeric strings
    with sr.Microphone(device_index=4) as source:
        r.adjust_for_ambient_noise(source) #only do this once before we start listening
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Did you say: " + r.recognize_wit(audio, key=WIT_AI_KEY))
        translatedAudio = r.recognize_wit(audio, key = WIT_AI_KEY)
        return translatedAudio;
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Wit.ai service; {0}".format(e))

