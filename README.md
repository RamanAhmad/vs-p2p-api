# Peer2Peer API Testing

## Übersicht
Dieses Repository wurde für die Praktikumsaufgabe **Peer-to-Peer** im Rahmen des Moduls **Verteilte Systeme (VS)** an der **HAW Hamburg** erstellt. Dies enthält eine Sammlung von Skripten, die dafür zuständig sind, die Sol- und Komponenten-Kommunikation für ein P2P-System in Docker-Containern zu starten und API-Tests durchzuführen.


## Repository-Struktur

- **Dockerfile**: Docker-Konfiguration für die Erstellung des Images.
- **run_sol.sh**: Skript zum Starten der **Sol-Umgebung**.
- **run_com.sh**: Skript zum Starten der **Komponenten-Umgebung**.
- **run_test.sh**: Skript zum Ausführen von API-Tests und Sammeln von Testergebnissen.
- **broadcast/resources/test_environment.postman_environment.json**: JSON-Datei mit Umgebungsvariablen für Postman-Tests.
- **test_results/**: Verzeichnis für die Testergebnisse.


## Voraussetzung

<details>
  <summary>Docker - Die Anwendung nutzt Docker-Container</summary>
  https://www.docker.com/get-started
</details>

<details>
  <summary>Docker Daemon muss aktiv sein, um Container zu starten</summary>
  Überprüfe, ob der Daemon läuft, mit `sudo systemctl status docker` (Linux) oder starte Docker Desktop (macOS/Windows).
</details>


## Setup

### 1. Die P2P-Anwendung als Docker-Image bauen
### 2. Skripte ausführbar machen

 ```bash
  chmod +x run_sol.sh run_com.sh run_test.sh
 ```

### 3. Skript `run_sol.sh` mit der image_id der P2P-Anwendung starten

```bash
  ./run_sol.sh <image_id>
```

### 4. Skript `run_com.sh` mit der image_id der P2P-Anwendung starten

```bash
  ./run_com.sh <image_id>
```

### 5. Die Umgebungsvariablen konfigurieren

Zu der Datei `broadcast/resources/test_environment.postman_environment.json` gehen und die folgenden Werte anpassen:

- `COM_OTHER_UUID`: UUID der aktiven Komponente.
- `COM_OTHER_IP`: IP-Adresse der aktiven Komponente.
- `COM_OTHER_TCP`: TCP-Port der aktiven Komponente.
- `COM_PATH`: UUID der aktiven Komponente


## Tests ausführen
In diesem Abschnitt testen wir **Sol-Instanz** sowie die **Komponenten-Instanz**, die im Setup-Abschnitt gestartet wurden.

### 1. Tests für die Sol-Instanz ausführen
Führe das Skript `run_test.sh` aus, um die Tests für die Sol-Instanz zu starten:

```bash
 ./run_test.sh <port> sol
```
Ersetze `<port>` mit dem Port der **Sol-Instanz**.

### 2. Tests für die Komponenten-Instanz ausführen
Führe das Skript `run_test.sh` aus, um die Tests für die Komponenten-Instanz zu starten:

```bash
  ./run_test.sh <port> com
```
Ersetze `<port>` mit dem gewünschten Port für die **Komponenten-Instanz**.

> **Hinweis:** Wenn du Windows verwendest, benutze das Cygwin- oder Git Bash-Terminal.

## Testberichte
Nach dem Ausführen der Tests kannst du die Ergebnisse in HTML-Dateien anzeigen. Die Testberichte befinden sich im Verzeichnis `test_results`.

- **Testberichte für die Sol-Instanz sind hier zu finden**:

	`
  	test_results/sol/newman/<date>.html
	`

- **Testberichte für die Komponenten-Instanz sind hier zu finden**:

	`
  	test_results/com/newman/<date>.html
	`