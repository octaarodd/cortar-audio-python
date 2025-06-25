Cortar audio con Python

Este es un pequeño script hecho en Python que utiliza la librería `pydub` para procesar archivos de audio. El script corta los primeros 5 segundos de un archivo mp3 y guarda el resultado en un nuevo archivo.

¿Qué hace?

- Lee un archivo de audio (`tu_audio.mp3`)
- Elimina los primeros 5 segundos (5000 milisegundos)
- Guarda el audio modificado como `audio_cortado_v2.mp3`

¿Cómo usarlo?

1. Instalá las dependencias necesarias:

```bash
pip install pydub
```

2. Asegurate de tener instalado FFmpeg y que esté en tu PATH del sistema.

3. Colocá un archivo llamado tu_audio.mp3 en la misma carpeta del script.

4. Ejecutá el script:

```bash
python cortar_audio.py
```
5. El nuevo archivo audio_cortado.mp3 aparecerá en la misma carpeta.

Requisitos

Python 3.x
pydub
FFmpeg

Autor
Creado por Octavio Rodríguez como su primer proyecto de manipulación de audio con Python.
