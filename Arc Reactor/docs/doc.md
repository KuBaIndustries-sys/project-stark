
# Dokumentacja Reaktora Łukowego z Superkondensatorami

## Zawartość

- Schemat blokowy
- Kod do Arduino
- Lista komponentów

---

### Założenia Projektu

| Element                  | Wartość / Typ                                  |
|--------------------------|------------------------------------------------|
| Zasilanie główne         | Superkondensator 2.7V 500F (lub kilka szeregowo) |
| Zasilanie pomocnicze     | Moduł ładowania z USB-C (lub solarny)          |
| Efekt świetlny           | Pierścień LED (np. Neopixel WS2812B)            |
| Kontrola                 | Arduino Nano / ESP32 / Attiny85                |
| Obudowa                  | Druk 3D lub aluminium + akryl                 |
| Moc wyjściowa            | ~3–5V dla systemu LED                          |
| Czas świecenia           | Kilka minut – doładowywalny w kilkanaście sekund |

---

### Schemat Blokowy

```
[USB-C / Solarna ładowarka]
          |
    [Moduł ładowania TP4056]
          |
  [Bank superkondensatorów] ───► [Przetwornica step-up 5V]
                                     |
                               [Kontroler LED (Arduino)]
                                     |
                             [Pierścień LED RGB]
```

---

### Lista Komponentów (BOM)

| Komponent                         | Ilość      | Uwagi                                      |
|-----------------------------------|------------|--------------------------------------------|
| Superkondensator 2.7V 500F        | 2–3        | Połączone szeregowo (dla 5.4–8.1V)         |
| Moduł ładowania TP4056 z ochroną  | 1          | USB-C lub microUSB                         |
| Przetwornica step-up (np. MT3608) | 1          | Podbija napięcie do 5V                     |
| Arduino Nano / Attiny85           | 1          | Sterowanie efektami LED                    |
| Pierścień LED WS2812B             | 1          | 12–16 diod                                 |
| Rezystory balansujące 10kΩ        | 2          | Między kondensatorami                      |
| Przewody, PCB, złącza             | wg potrzeb | Montaż i połączenia                        |
| Obudowa (druk 3D / DIY)           | 1          | STL do przygotowania                       |

---
