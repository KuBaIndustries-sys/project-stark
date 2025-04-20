from hologram import load_3d_model, display_hologram
from voice import speak
from hand_tracking import track_hands


def main():
    """Główna funkcja uruchamiająca system holograficzny."""
    model_path = "models/helmet.obj"

    try:
        speak("Holographic interface activated.")
        model = load_3d_model(model_path)
        display_hologram(model)
        track_hands()
    except Exception as e:
        print(f"Błąd: {e}")


if __name__ == "__main__":
    main()
