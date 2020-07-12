import speech_recognition as sr
import playsound
import os
import random
from gtts import gTTS

r = sr.Recognizer() #Class responsible for recognizing speech

def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    rr = random.randint(1,1000000)
    audio_file = 'audio-'+ str(rr) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

with sr.Microphone() as source:
    print("Speak Something")
    audio = r.listen(source)
    voice_data = r.recognize_google(audio)
    speak(voice_data)



'''from playsound import playsound
from gtts import gTTS

def convert_to_audio(text):
    audio = gTTS(text)
    audio.save("textaudio.mp3")
    playsound("textaudio.mp3")

convert_to_audio("Hello World")'''
