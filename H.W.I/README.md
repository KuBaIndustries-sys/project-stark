# Holograficzny Interfejs Warsztatu

## Opis Projektu
Holograficzny Interfejs Warsztatu to zaawansowane oprogramowanie umożliwiające interaktywną wizualizację modeli 3D w rzeczywistości rozszerzonej. Aplikacja pozwala użytkownikom manipulować modelami za pomocą gestów i poleceń głosowych, co ułatwia pracę w środowiskach inżynieryjnych, edukacyjnych i projektowych.

## Kluczowe Funkcje
- **Holograficzna wizualizacja** – realistyczne modele 3D wyświetlane w przestrzeni.
- **Obsługa gestów** – interakcja z modelami za pomocą ruchów dłoni.
- **Sterowanie głosowe** – wykonywanie poleceń za pomocą komend głosowych.
- **Integracja z systemami CAD** – możliwość importu modeli z popularnych narzędzi projektowych.
- **Analiza w czasie rzeczywistym** – pomiary, symulacje oraz dynamiczna modyfikacja modeli.

## Struktura Projektu
```
holographic_interface/
├── models/                # Przechowywanie modeli 3D
│   ├── example_model.obj  # Przykładowy model 3D
├── src/                   # Główne pliki źródłowe aplikacji
│   ├── hologram.py        # Obsługa wizualizacji holograficznej
│   ├── voice.py           # Moduł obsługi poleceń głosowych
│   ├── hand_tracking.py   # Moduł wykrywania ruchów dłoni
├── README.md              # Dokumentacja projektu
├── requirements.txt       # Lista wymaganych bibliotek
├── main.py                # Plik główny aplikacji
```

## Wymagania Systemowe
- **System operacyjny**: macOS / Windows / Linux
- **Sprzęt**: Kamera do śledzenia gestów oraz kompatybilne urządzenie AR/VR
- **Oprogramowanie**: OpenCV, Open3D, pyttsx3

## Instalacja
1. Pobierz repozytorium i przejdź do katalogu projektu:
   ```sh
   git clone https://github.com/user/holographic_interface.git
   cd holographic_interface
   ```
2. Zainstaluj wymagane zależności:
   ```sh
   pip install -r requirements.txt
   ```
3. Uruchom aplikację:
   ```sh
   python main.py
   ```

## Instrukcja Obsługi
- **Gesty**:
  - Zacisnąć dłoń na 10 sekund – zamknięcie programu.
  - Przesunięcie dłoni w lewo/prawo – obracanie modelu.
  - Rozszerzenie dłoni – powiększanie modelu.
- **Głos**:
  - "Load model [nazwa]" – załadowanie modelu.
  - "Rotate left" / "Rotate right" – obracanie modelu.
  - "Scale up" / "Scale down" – zmiana skali modelu.

## Zastosowania
- **Przemysł inżynieryjny** – prototypowanie i wizualizacja projektów technicznych.
- **Edukacja** – interaktywne nauczanie z wykorzystaniem hologramów.
- **Medycyna** – analiza skanów 3D dla diagnostyki i planowania zabiegów.
- **Architektura i design** – modelowanie oraz prezentacja koncepcji projektowych.

## Autorzy
Projekt stworzony w ramach **Project Stark**.

## Licencja
Projekt objęty licencją MIT. Szczegóły w pliku LICENSE.



user manual:

dense 

-closed hand for 10 seconds - closing program
