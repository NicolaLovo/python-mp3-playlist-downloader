# Inizializzazione del progetto

> Nota: da fare solo la prima volta che si apre il progetto


## Prerequisiti

Scaricare e installare python
> Verificare che python sia installato scrivendo sul terminale il comando `python`

Scaricare e aggiungere alle variabili d'ambiente [ffmpeg](https://www.videohelp.com/software/ffmpeg)

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



# Roba per sviluppatori


Fix for pytube: https://github.com/pytube/pytube/issues/1678#issuecomment-1609241125
Modificare il file .venv/Lib/site-packages/pytube/cypher.py a linea 264
```python
function_patterns = [
    r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
    r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',
    r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])\([a-z]\)',
]
```