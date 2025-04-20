import tkinter as tk
from handlers import handle_text_input, handle_voice_input, save_conversation
from camera_handler import handle_camera_input
from core.camera import CameraHandler
from core.object_recognition import ObjectRecognizer
from menu import create_menu
from models.model import AIModel  # Import modelu AI


def run_gui():
    """Uruchamia główną aplikację GUI."""
    global text_entry, output_text, camera, object_recognizer, ai_model

    camera = CameraHandler()
    object_recognizer = ObjectRecognizer()
    ai_model = AIModel()  # Inicjalizacja modelu AI

    root = tk.Tk()
    root.title("J.R.V.S. Orion - Asystent AI (Polski)")
    root.geometry("700x500")

    # Menu aplikacji
    create_menu(root, save_conversation, root.quit)

    # Pole tekstowe do wpisywania zapytań
    frame_input = tk.Frame(root)
    frame_input.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

    text_entry = tk.Entry(frame_input, font=("Arial", 14), width=50)
    text_entry.pack(side=tk.LEFT, padx=10)

    # Przycisk do obsługi zapytań tekstowych
    text_button = tk.Button(frame_input, text="Wyślij", font=("Arial", 12), command=lambda: handle_text_input(text_entry, output_text))
    text_button.pack(side=tk.LEFT, padx=5)

    # Przycisk do obsługi zapytań głosowych
    voice_button = tk.Button(frame_input, text="Mów", font=("Arial", 12), command=lambda: handle_voice_input(output_text))
    voice_button.pack(side=tk.LEFT, padx=5)

    # Przycisk do obsługi rozpoznawania obiektów
    camera_button = tk.Button(frame_input, text="Kamera", font=("Arial", 12), command=lambda: handle_camera_input(camera, object_recognizer, output_text))
    camera_button.pack(side=tk.LEFT, padx=5)

    # Pole tekstowe do wyświetlania wyników
    output_text = tk.Text(root, font=("Arial", 12), height=20, state=tk.NORMAL, wrap=tk.WORD)
    output_text.pack(pady=10, fill=tk.BOTH, padx=20)

    # Uruchomienie kamery
    camera.start_camera()

    # Uruchomienie głównej pętli aplikacji
    root.mainloop()

    # Wyłączenie kamery po zamknięciu aplikacji
    camera.stop_camera()

if __name__ == '__main__':
    run_gui()
