import pyttsx3
speech = pyttsx3.init()  # initialize the text-to-speech engine
speech.say(input('Digite seu texto: '))  # prompt for the text to be spoken
speech.runAndWait()  # run the speech engine
