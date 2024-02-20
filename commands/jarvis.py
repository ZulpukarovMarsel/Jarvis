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


def activate_jarvis():
    play_audio('sounds/app_sound_jarvis-og_greet1.wav')


def process_command(cmd):
    if any(word in cmd for word in command['cmds']['audio']):
        play_audio('sounds/app_sound_jarvis-og_ok2.wav')
        webbrowser.open_new_tab('https://www.youtube.com/watch?v=fjUGC8g4GOE')
    elif any(word in cmd for word in command['cmds']['youtube']):
        play_audio('sounds/app_sound_jarvis-og_ok2.wav')
        webbrowser.open_new_tab('https://www.youtube.com/')
    elif any(word in cmd for word in command['cmds']['kino']):
        play_audio('sounds/app_sound_jarvis-og_ok3.wav')
        webbrowser.open_new_tab('https://kinojump.com/')
    elif any(word in cmd for word in command['cmds']['github']):
        play_audio('sounds/app_sound_jarvis-og_ok4.wav')
        webbrowser.open_new_tab('https://github.com/MarsGeeks/')
    elif any(word in cmd for word in command['cmds']['time']):
        speak(time())
    elif any(word == cmd for word in command['os']['switch_off']):
        play_audio('sounds/app_sound_jarvis-og_off.wav')
        os.system("shutdown /s /t 0")

