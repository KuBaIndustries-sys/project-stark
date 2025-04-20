Oczywiście! Poniżej znajdziesz kompletną **rozszerzoną dokumentację techniczną reaktora łukowego**, gotową do zapisania i przekonwertowania na kod QR:

---

## 📘 Dokumentacja Techniczna: Reaktor Łukowy

---

### 1. Opis Ogólny  
Reaktor łukowy to urządzenie przetwarzające energię elektryczną w ciepło za pomocą łuku elektrycznego. Łuk tworzy się pomiędzy dwiema elektrodami pod wysokim napięciem i natężeniem prądu, generując ekstremalne temperatury (do 5000°C). W zależności od zastosowania, może służyć do topienia metali, tworzenia plazmy, badań materiałowych lub eksperymentów naukowych.

---

### 2. Główne Komponenty

- **Elektrody**  
  - Materiał: wolfram lub grafit  
  - Średnica: 10–50 mm  
  - Odległość: 1–5 mm (regulowana)

- **Źródło zasilania**  
  - Typ: zasilacz DC/AC wysokoprądowy  
  - Napięcie: 30–100 V  
  - Natężenie: 100–400 A  
  - Moc: 10–50 kW

- **Komora robocza**  
  - Materiał: stal nierdzewna + izolacja ceramiczna  
  - Odporność termiczna: > 2000°C  
  - Osłona: stal + warstwa ognioodporna

- **System chłodzenia**  
  - Medium: woda destylowana  
  - Obieg: zamknięty z pompą i wymiennikiem ciepła  
  - Przepływ: 10–15 l/min

- **Sterowanie i zabezpieczenia**  
  - Wyłączniki nadprądowe i różnicowoprądowe  
  - Termistory, przekaźniki temperatury, czujniki ciśnienia  
  - System natychmiastowego odłączenia zasilania

---

### 3. Obliczenia Techniczne

#### 3.1 Parametry Łuku
- Napięcie: 70 V  
- Prąd: 250 A  
- Moc:  
  \[
  P = U \times I = 70\,V \times 250\,A = 17\,500\,W = 17.5\,kW
  \]

#### 3.2 Zużycie energii
- Praca 1 godzina:  
  \[
  17.5\,kW \times 1\,h = 17.5\,kWh
  \]

#### 3.3 Chłodzenie wodne
- Ciepło do odprowadzenia: 10 kW  
- Ciepło właściwe wody: 4.18 kJ/kg·K  
- Maks. wzrost temp.: 15°C  
- Przepływ:  
  \[
  \dot{m} = \frac{10\,000}{4180 \times 15} ≈ 0.16\,kg/s ≈ 9.6\,l/min
  \]

---

### 4. Schemat Elektryczny (Opis Tekstowy)

1. **Zasilanie główne** – podłączone do przemysłowego gniazda 400V AC.
2. **Transformator mocy** – obniża napięcie do 70V AC/DC.
3. **Mostek prostowniczy** (jeśli DC) – przekształca napięcie przemienne na stałe.
4. **Sterownik łuku** – umożliwia regulację prądu, napięcia, czasu trwania.
5. **Wyjście na elektrody** – przewody o dużym przekroju (min. 35 mm²), zakończone uchwytami.
6. **System zabezpieczeń** – wyłączniki, bezpieczniki, styczniki, przekaźniki termiczne.

---

### 5. Procedura Uruchomienia

1. Sprawdź podłączenia, układ chłodzenia, poziom wody i działanie zabezpieczeń.
2. Ustaw początkową odległość między elektrodami (np. 2 mm).
3. Włącz zasilanie główne, następnie sterownik łuku.
4. Stopniowo zwiększ napięcie i prąd, aż powstanie łuk.
5. Monitoruj parametry na wyświetlaczu (temperatura, napięcie, prąd, chłodzenie).
6. Po zakończeniu – rozłącz system w odwrotnej kolejności.

---

### 6. Bezpieczeństwo

- Praca wyłącznie w dobrze wentylowanym pomieszczeniu (gazy jonizacyjne).
- Ochrona wzroku: maska z filtrem UV/IR (spawalnicza lub plazmowa).
- Ochrona słuchu: nauszniki wygłuszające.
- Ochrona termiczna: rękawice i odzież ogniotrwała.
- Zakaz dotykania elektrod w czasie pracy.
- Obowiązkowy system automatycznego wyłączenia przy przeciążeniu.

---

### 7. Utrzymanie i Kalibracja

- Codziennie: sprawdzenie poziomu chłodziwa, stanu przewodów.
- Tygodniowo: kontrola elektrod, czyszczenie osadów.
- Miesięcznie: kalibracja sterownika i kontrola zabezpieczeń.
- Co 6 miesięcy: pełny przegląd systemu chłodzenia i zasilania.

---

### 8. Dodatkowe Informacje

- **Temperatura łuku**: 3500–5500°C  
- **Żywotność elektrod**: 30–100 h w zależności od intensywności pracy  
- **Możliwość pracy z atmosferą ochronną**: TAK (argon, azot)  
- **Opcjonalny system rejestracji parametrów**: czujniki + mikrokontroler (ESP32, Arduino)

---