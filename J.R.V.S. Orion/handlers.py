from tkinter import messagebox, filedialog
from core.speech_recog import record_audio, speech_to_text
from core.nlp_engine import generate_response
from core.tts import play_response

def handle_text_input(text_entry, output_text):
    """Obsługuje zapytania wpisane przez użytkownika w polu tekstowym."""
    user_input = text_entry.get()
    if not user_input:
        messagebox.showwarning("Uwaga", "Pole tekstowe nie może być puste!")
        return

    response = generate_response(user_input)
    output_text.insert("end", f"Użytkownik: {user_input}\nJ.R.V.S.: {response}\n\n")
    play_response(response)
    text_entry.delete(0, "end")

def handle_voice_input(output_text):
    """Obsługuje wejście głosowe od użytkownika."""
    try:
        audio = record_audio()
        user_input = speech_to_text(audio)
        output_text.insert("end", f"Użytkownik (mowa): {user_input}\n")

        response = generate_response(user_input)
        output_text.insert("end", f"J.R.V.S.: {response}\n\n")
        play_response(response)
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił błąd: {e}")

def save_conversation(output_text):
    """Zapisuje historię rozmowy do pliku tekstowego."""
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Pliki tekstowe", "*.txt")],
        title="Zapisz historię rozmowy"
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(output_text.get("1.0", "end"))
        messagebox.showinfo("Sukces", "Historia rozmowy została zapisana!")
