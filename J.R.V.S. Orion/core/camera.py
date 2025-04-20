import cv2

class CameraHandler:
    def __init__(self):
        self.camera = None

    def start_camera(self):
        """Inicjalizuje kamerę."""
        self.camera = cv2.VideoCapture(0)
        if not self.camera.isOpened():
            raise Exception("Nie można otworzyć kamery.")

    def get_frame(self):
        """Pobiera pojedynczą klatkę z kamery."""
        if self.camera is None or not self.camera.isOpened():
            raise Exception("Kamera nie jest uruchomiona.")
        ret, frame = self.camera.read()
        if not ret:
            raise Exception("Nie udało się odczytać klatki.")
        return frame

    def stop_camera(self):
        """Zatrzymuje kamerę."""
        if self.camera is not None:
            self.camera.release()
            self.camera = None
