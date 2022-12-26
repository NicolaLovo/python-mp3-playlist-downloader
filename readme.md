# Inizializzare il progetto

```bash
py -3 -m venv .venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.venv\scripts\activate
```

### Mac

aprire la cartella del programma nel terminale

```bash
python3 -m venv .venv
source .venv/bin/activate
```

# Installare le librerie

```bash
pip install pytube moviepy pydub
```

**è necessario installare ffmpeg**

<https://pythonbasics.org/convert-mp3-to-wav/>

### Eseguire il codice

Modificare la variable "downloads" all'occorrenza

Windows

```bash
python main.py
```

Mac

```bash
python3 main.py
```

# Cartelle necessarie:

- download/audio
- download/videos
- download/wav
