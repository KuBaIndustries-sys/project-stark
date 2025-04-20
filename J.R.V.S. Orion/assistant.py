import tkinter as tk
from tkinter import messagebox, filedialog
from core.speech_recog import record_audio, speech_to_text
from core.nlp_engine import generate_response
from core.tts import play_response
from core.camera import CameraHandler
from core.object_recognition import ObjectRecognizer

def handle_text_input():
    """Obsługuje zapytania wpisane przez użytkownika w polu tekstowym."""
    user_input = text_entry.get()
    if not user_input:
        messagebox.showwarning("Uwaga", "Pole tekstowe nie może być puste!")
        return

    # Generowanie odpowiedzi (założenie: generate_response obsługuje język polski)
    response = generate_response(user_input)

    # Wyświetlenie odpowiedzi w GUI
    output_text.insert(tk.END, f"Użytkownik: {user_input}\n")
    output_text.insert(tk.END, f"J.R.V.S.: {response}\n\n")

    # Odtwarzanie odpowiedzi głosowo
    play_response(response)

    # Czyszczenie pola tekstowego
    text_entry.delete(0, tk.END)

def handle_voice_input():
    """Obsługuje wejście głosowe od użytkownika."""
    try:
        # Nagrywanie i rozpoznawanie mowy (założenie: speech_to_text działa w języku polskim)
        audio = record_audio()
        user_input = speech_to_text(audio)

        # Wyświetlenie zapytania użytkownika w GUI
        output_text.insert(tk.END, f"Użytkownik (mowa): {user_input}\n")

        # Generowanie odpowiedzi
        response = generate_response(user_input)

        # Wyświetlenie odpowiedzi w GUI
        output_text.insert(tk.END, f"J.R.V.S.: {response}\n\n")

        # Odtwarzanie odpowiedzi głosowo
        play_response(response)

    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił błąd podczas rozpoznawania mowy: {e}")

def save_conversation():
    """Zapisuje historię rozmowy do pliku tekstowego."""
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Pliki tekstowe", "*.txt")],
        title="Zapisz historię rozmowy"
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(output_text.get("1.0", tk.END))
        messagebox.showinfo("Sukces", "Historia rozmowy została zapisana!")

def handle_camera_input():
    """Obsługuje wejście z kamery i rozpoznawanie obiektów."""
    frame = camera.get_frame()
    if frame is not None:
        objects = object_recognizer.recognize(frame)
        output_text.insert(tk.END, f"Rozpoznane obiekty: {', '.join(objects)}\n")
    else:
        messagebox.showerror("Błąd", "Nie można uzyskać klatki z kamery.")

# Tworzenie głównego okna aplikacji
def run_gui():
    """Uruchamia główną aplikację GUI."""
    global text_entry, output_text, camera, object_recognizer

    camera = CameraHandler()
    object_recognizer = ObjectRecognizer()

    root = tk.Tk()
    root.title("J.R.V.S. Orion - Asystent AI (Polski)")
    root.geometry("700x500")

    # Menu aplikacji
    menu_bar = tk.Menu(root)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Zapisz historię", command=save_conversation)
    file_menu.add_separator()
    file_menu.add_command(label="Wyjście", command=root.quit)
    menu_bar.add_cascade(label="Plik", menu=file_menu)
    root.config(menu=menu_bar)

    # Pole tekstowe do wpisywania zapytań
    frame_input = tk.Frame(root)
    frame_input.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

    text_entry = tk.Entry(frame_input, font=("Arial", 14), width=50)
    text_entry.pack(side=tk.LEFT, padx=10)

    # Przycisk do obsługi zapytań tekstowych
    text_button = tk.Button(frame_input, text="Wyślij", font=("Arial", 12), command=handle_text_input)
    text_button.pack(side=tk.LEFT, padx=5)

    # Przycisk do obsługi zapytań głosowych
    voice_button = tk.Button(frame_input, text="Mów", font=("Arial", 12), command=handle_voice_input)
    voice_button.pack(side=tk.LEFT, padx=5)

    # Przycisk do obsługi rozpoznawania obiektów
    camera_button = tk.Button(frame_input, text="Kamera", font=("Arial", 12), command=handle_camera_input)
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
