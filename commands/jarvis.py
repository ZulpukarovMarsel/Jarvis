import os
import webbrowser
from datetime import datetime
import speech_recognition
import pyttsx3
from pydub import AudioSegment
from pydub.playback import play
from pydub.utils import which

command = {
    'os': {
        'switch_off': ('выключи ноутбук', 'выключи ноут')
    },
    'se': {
        'jarvis': ('джарвис', 'привет джарвис', 'jarvis'),
        'break': ('стоп', 'break'),
        'thanks': ('спасибо', 'красавчик', 'благодарю'),
        'negative': ('да не ты тупой', 'ты тупой', 'не ты тупой')
    },
    'cmds': {
        'audio': ('музыка', 'включи музыку'),
        'youtube': ('открой ютуб', 'открой youtube'),
        'kino': ('открой кино', 'время фильма'),
        'github': ('открой git hub', 'открой гит хаб'),
        'time': ('какое время', 'какое сейчас время')
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


def play_audio(filename):
    sound = AudioSegment.from_file(filename, format="wav")
    play(sound)


def activate_jarvis():
    play_audio(os.path.join('sounds', 'app_sound_jarvis-og_greet1.wav'))


def process_command(cmd):
    if any(word in cmd for word in command['cmds']['audio']):
        play_audio(os.path.join('sounds', 'app_sound_jarvis-og_ok2.wav'))
        webbrowser.open_new_tab('https://www.youtube.com/watch?v=fjUGC8g4GOE')


def jarvis_main():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio, language='ru-RU').lower()
            print(query)

            if any(word in query for word in command['se']['jarvis']):
                activate_jarvis()

                while True:
                    audio = sr.listen(source=mic)
                    query = sr.recognize_google(audio, language='ru-RU').lower()
                    print(query)

                    if any(word in query for word in command['se']['break']):
                        play_audio(os.path.join('sounds', 'app_sound_jarvis-og_not_found.wav'))
                        break
                    elif any(word in query for word in command['se']['thanks']):
                        play_audio(os.path.join('sounds', 'app_sound_jarvis-og_thanks.wav'))
                    elif any(word in query for word in command['se']['negative']):
                        play_audio(os.path.join('sounds', 'app_sound_jarvis-og_stupid.wav'))

                    process_command(query)

    except speech_recognition.UnknownValueError:
        speak("Не удалось распознать речь")
    except speech_recognition.RequestError as e:
        speak(f"Ошибка сервиса распознавания речи: {e}")


if __name__ == "__main__":
    jarvis_main()
