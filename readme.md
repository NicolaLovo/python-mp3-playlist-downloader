# Inizializzazione del progetto

> Nota: da fare solo la prima volta che si apre il progetto

## Prerequisiti

Scaricare e aggiungere alle variabili d'ambiente [ffmpeg](https://www.videohelp.com/software/ffmpeg)

Scaricare e installare **Python 3.12** (testato su **3.12.9**)

> Verificare che python sia installato scrivendo sul terminale il comando `python --version`

### Per Python > 3.12

Installa le librerie mancanti per audioop:

```bash
pip install audioop-lts
```

## Creare l'ambiente

```bash
python -m venv .venv
```

Oppure, se quello sopra non funziona

```bash
py -3 -m venv .venv
```

## Attivare l'ambiente

```bash
.venv\scripts\activate
```

## Installare le librerie

```bash
pip install -r requirements.txt
```

# Avviare il programma

Opzionale: abilitare i permessi [windows](https://stackoverflow.com/questions/4037939/powershell-says-execution-of-scripts-is-disabled-on-this-system)

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

## Attivare l'ambiente

```bash
.venv\scripts\activate
```

## Avviare il programma

```bash
python main.py
```

## Cartelle necessarie:

- download/audio
- download/videos
- download/wav

# Creare l'eseguibile

```bash
pyinstaller main.py --onefile
```

## Mac

aprire la cartella del programma nel terminale

```bash
python3 -m venv .venv
source .venv/bin/activate
```

```bash
python3 main.py
```
