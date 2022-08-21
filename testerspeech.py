import pyttsx3
import speech_recognition as sr

#API config
engine = pyttsx3.init('sapi5') #microsoft api sapi5
voices = engine.getProperty('voices')
print(voices[1].id) 
engine.setProperty('voice', voices[1].id) #zira voice

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def preak(s):
	from rem2 import rem
	rem(s)
	speak(s)
	print(s)

import speech_recognition as sr
def ear():
	k = 0
	while k < 1:
		r = sr.Recognizer()
		with sr.Microphone() as source:
			r.pause_threshold = 1 #duration for how long it records
			audio = r.listen(source) #listen
		try:
			print("Recognizing...")
			query = r.recognize_google(audio, language='en-in') #translate stt
			print(query) #result
			return query
			break
		except Exception as e:
			continue


def glassear(): #ear() but without print functions, good for bg listening
	k = 0
	while k < 1:
		r = sr.Recognizer()
		with sr.Microphone() as source:
			r.pause_threshold = 1 #duration for how long it records
			audio = r.listen(source) #listen
		try:
			query = r.recognize_google(audio, language='en-in') #translate stt
			return query
			break
		except Exception as e:
			continue
