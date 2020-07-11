import speech_recognition as sr

r = sr.Recognizer() #Class responsible for recognizing speech

with sr.Microphone() as source:
    print("Speak Something")
    audio = r.listen(source)
    voice_data = r.recognize_google(audio)
    print(voice_data)