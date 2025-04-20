import pyttsx3

# Inicjalizacja TTS
engine = pyttsx3.init()

def play_response(response_text):
    """
    Odtwarza odpowiedź asystenta głosowo.
    """
    engine.say(response_text)
    engine.runAndWait()
