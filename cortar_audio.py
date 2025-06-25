from pydub import AudioSegment

# Cargar el archivo de audio
audio = AudioSegment.from_file("tu_audio.mp3")

# Cortar los primeros 5 segundos [5000 milisegundos]
audio_cortado = audio[5000:]

# Exportar el nuevo audio
audio_cortado.export("audio_cortado_v2.mp3", format = "mp3")

print("Audio Cortado correctamente. Guardado como 'audio_cortado.mp3'")