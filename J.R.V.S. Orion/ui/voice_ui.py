from core.speech_recog import record_audio, speech_to_text
from core.tts import play_response

def voice_interface():
    """
    Uruchamia interfejs głosowy.
    """
    print("Witaj! Mów do mikrofonu, aby rozpocząć.")
    try:
        while True:
            print("\nNasłuchuję...")
            audio = record_audio()
            user_input = speech_to_text(audio)
            print(f"Użytkownik: {user_input}")

            response = f"Otrzymałem: {user_input}"  # Zmień na integrację z NLP
            print(f"Asystent: {response}")
            play_response(response)
    except KeyboardInterrupt:
        print("\nZamykam interfejs głosowy.")
