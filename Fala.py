import pyttsx3
fala = pyttsx3.init()
fala.say(input('Digite seu texto: '))
fala.runAndWait()