from datetime import datetime
import webbrowser
import speech_recognition
import pyttsx3, os
from pydub import AudioSegment
from pydub.playback import play

command = {
    'se': {
        'jarvis': ('джарвис', 'привет джарвис', 'jarvis'),
        'break': ('стоп', 'break'),
        'thanks': ('спасибо', 'красавчик', 'благодарю'),
        'negative': ('да не ты тупой', 'ты тупой', 'не ты тупой')
    }
}

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5
speak_engine = pyttsx3.init()

def speak(what):
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()

def time():
    times = datetime.now()
    return str(times.strftime('%H:%M'))

def hello(func):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            func(*args, **kwargs)
            wrapper.has_run = True
    wrapper.has_run = False
    return wrapper

@hello
def my_function():
    play_audio('sounds/app_sound_jarvis-og_run.wav')
# Вызываем функцию

def play_audio(filename):
    sound = AudioSegment.from_file(filename, format="wav")
    play(sound)