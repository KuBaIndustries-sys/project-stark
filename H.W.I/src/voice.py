import pyttsx3

def initialize_tts():
    """Inicjalizuje silnik syntezatora mowy."""
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Ustawienie szybkości mowy
    engine.setProperty('volume', 1.0)  # Ustawienie głośności
    return engine

def speak(text):
    """Wypowiada podany tekst."""
    engine = initialize_tts()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Holographic interface activated.")