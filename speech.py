import speech_recognition as sr

from chess import *

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone(device_index=1) as source:
    r.adjust_for_ambient_noise(source) #only do this once before we start listening
    print("Say something!")
    audio = r.listen(source)


WIT_AI_KEY = "3SJGCEANYYUJQSVMTMCNGVC4XX22LMMW"  # Wit.ai keys are 32-character uppercase alphanumeric strings
try:
    print("Did you say: " + r.recognize_wit(audio, key=WIT_AI_KEY))
    
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Wit.ai service; {0}".format(e))
