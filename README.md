# Mini SIEM Project

Prosty projekt typu Mini SIEM stworzony w celu nauki analizy logów, konteneryzacji oraz budowania dashboardów analitycznych. System w czasie rzeczywistym monitoruje plik tekstowy z logami serwera, wykrywa próby ataków Brute Force (SSH), zapisuje dane do bazy SQLite, wysyła powiadomienia na Discorda i wizualizuje statystyki w przeglądarce.

Całość została w pełni skonteneryzowana przy użyciu Dockera, dzięki czemu aplikacja uruchamia się identycznie na każdym systemie.

## 🚀 Jak to działa?

Projekt składa się z dwóch głównych usług działających równolegle:
1. **Parser (`parser.py`)** – Skrypt działający w tle. Śledzi plik `server_logs.txt`. Jeśli wykryje frazę o błędnym logowaniu SSH, wyciąga z niej adres IP, wysyła alert na webhook Discorda i zapisuje zdarzenie do bazy SQLite.
2. **Dashboard (`dashboard.py`)** – Panel webowy napisany w bibliotece Streamlit. Pobiera dane z bazy i generuje wykresy oraz tabele (np. TOP 5 adresów IP, wykres liczby ataków w czasie).

## 🛠️ Użyte technologie

* **Python 3.13** (wbudowane moduły `re`, `sqlite3`, `time`)
* **Pandas** (agregacja danych i przygotowanie statystyk)
* **Streamlit** (frontend i wizualizacja danych)
* **Docker & Docker Compose** (konteneryzacja i zarządzanie usługami)

## 📦 Jak to uruchomić?

Dzięki wykorzystaniu Docker Compose nie trzeba instalować Pythona ani żadnych bibliotek bezpośrednio na swoim komputerze.

1. Upewnij się, że masz uruchomioną aplikację **Docker Desktop**.
2. Otwórz terminal w głównym folderze projektu.
3. Uruchom cały system za pomocą jednej komendy:
   ```bash
   docker compose up --build
