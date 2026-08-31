# pyttsx3 is one type of model which speaks what we write inside the "engine.say("") statement"
# to install this model we need to write this in terminal : pip install pyttsx3
# below is the code to perform this type of action :

import pyttsx3
engine = pyttsx3.init()
engine.say("you looking hot,sexy and have big boobs")
engine.runAndWait()