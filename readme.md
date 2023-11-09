# Inizializzare il progetto

[fix permissions fow windows](https://stackoverflow.com/questions/4037939/powershell-says-execution-of-scripts-is-disabled-on-this-system)

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

Fix for pytube: https://github.com/pytube/pytube/issues/1678#issuecomment-1609241125
Modificare il file .venv/Lib/site-packages/pytube/cypher.py a linea 264

````python

```python

**è necessario installare ffmpeg**

<https://pythonbasics.org/convert-mp3-to-wav/>

### Eseguire il codice

Modificare la variable "downloads" all'occorrenza

Windows

```bash
python main.py
````

Mac

```bash
python3 main.py
```

# Cartelle necessarie:

- download/audio
- download/videos
- download/wav
