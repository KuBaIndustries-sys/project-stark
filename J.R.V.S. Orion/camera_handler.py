from tkinter import messagebox

def handle_camera_input(camera, object_recognizer, output_text):
    """Obsługuje wejście z kamery i rozpoznawanie obiektów."""
    frame = camera.get_frame()
    if frame is not None:
        objects = object_recognizer.recognize(frame)
        output_text.insert("end", f"Rozpoznane obiekty: {', '.join(objects)}\n")
    else:
        messagebox.showerror("Błąd", "Nie można uzyskać klatki z kamery.")
