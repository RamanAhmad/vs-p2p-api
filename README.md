# Peer2Peer API Testing

## Übersicht
Dieses Repository wurde für die Praktikumsaufgabe **Peer2Peer** im Rahmen des Moduls **Verteilte Systeme (VS)** an der **HAW Hamburg** erstellt. Dies enthält eine Sammlung von Skripten und einer Postman-Collection-Datei, um die Peer2Peer API zu testen.

Hier werden drei verschiedene Methoden beschrieben, wie man die API testen kann:

## 1. Manuelles Testen mit Postman
### Voraussetzung

**Postman-Installation**

  - Gehe auf die [offizielle Postman-Website](https://www.postman.com/downloads/)
  - Lade die Version für dein Betriebssystem herunter
  - Installationsanweisungen folgen


### Collection in Postman importieren

  - Öffne Postman
  - Klicke im oberen linken Bereich auf *Import*
  - Wähle im Pop-up-Fenster File aus
  - Wähle die Datei [Peer2Peer_API_Collection.json](p2p-postman-collection\Peer2Peer_API_Collection.json) aus und klicke auf *Open*


### Einrichten von Umgebungsvariablen
> **Hinweis:** Die Umgebungsvariablen können direkt in den API-Requests geändert werden. Es wird jedoch empfohlen, **Umgebungsvariablen** in Postman zu verwenden, um die Stabilität zu gewährleisten.

Für das manuelle Testen müssen die Umgebungsvariablen in Postman eingerichtet werden. Diese Variablen werden in den API-Anfragen verwendet, um dynamische Werte zu ersetzen, z.B. die UUIDs von Komponenten, IP-Adressen und etc.

**Umgebungsvariablen:**
- `COM_1_UUID`: UUID der ersten Komponente
- `COM_2_UUID`: UUID der zweiten Komponente
- `STAR_1_UUID`: UUID des Stars
- `COM_1_IP`: IP-Adresse der ersten Komponente
- `COM_2_IP`: IP-Adresse der zweiten Komponente
- `COM_2_TCP`: TCP-Port der zweiten Komponente
- `STATUS_OK`: Erfolgreicher Statuscode



## 2. Testen mit automatisch generierten Umgebungsvariablen
Diese Methode nutzt Skripte, die automatisch Umgebungsvariablen durch Broadcast-Nachrichten an Sol für die Postman-Tests/Collection generieren.

### Voraussetzungen

- Deine Server-App läuft in einem Docker-Container.
- Deine Server-App reagiert auf UDP-Broadcasts auf einem angegebenen Port mit einem JSON-formatierten String.

### Ressourcen einrichten (optional für die neueste Umgebungsdatei)

- Exportiere die Umgebungsdatei der Postman-Collection
- Kopiere die Datei in das Verzeichnis `resources/`.
- Benenne die Datei in `test_environment.postman_environment.json` um.

## Skript ausführen

- Navigiere zu `broadcast\run.sh` und führe das folgende Kommando aus:

    ```bash
    .\run.sh <udp-port>
    ```

> **Hinweis:** Wenn du Windows verwendest, benutze das Cygwin- oder Git Bash-Terminal.


## 3. Vollautomatisiertes Testen
Mit dieser Methode können alle Tests vollständig automatisch ausgeführt werden.

### Voraussetzungen


- **[Docker](https://www.docker.com/get-started):** Deine Server-App sollte in einem Docker-Container laufen.
- **[Python 3](https://www.python.org/downloads/):** Installiere Python 3, um die Testfälle auszuführen.

## Skript ausführen

- Führe das folgende Kommando aus:

    ```bash
    .\run.sh <udp-port>
    ```

> **Hinweis:** Ersetze <udp-port> durch den Port, auf dem der UDP-Broadcast gesendet werden soll.