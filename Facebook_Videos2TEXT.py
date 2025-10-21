"""
Facebook_Videos2TEXT
"""

#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import moviepy.editor as mp
import speech_recognition as sr
import os

def convertir_video_a_audio(video_path):
    """
    Esta función extrae el audio de un video y lo guarda como archivo WAV.
    """
    clip = mp.VideoFileClip(video_path)
    audio_path = f"{video_path}.wav"
    clip.audio.write_audiofile(audio_path, codec='pcm_s16le')  # codec para formato WAV
    return audio_path

def transcribir_audio_a_texto(audio_path):
    """
    Esta función utiliza la biblioteca speech_recognition para transcribir el audio a texto.
    """
    r = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = r.record(source)
    try:
        text = r.recognize_google(audio_data, language='es-ES')  # Asumiendo que el audio está en español
        return text
    except sr.UnknownValueError:
        return "Google Speech Recognition no pudo entender el audio"
    except sr.RequestError as e:
        return f"¿No se pudo solicitar resultados desde el servicio de Google Speech Recognition; {e}"

def procesar_video(video_path):
    """
    Esta función orquesta la conversión de video a audio y luego la transcripción a texto.
    """
    print(f"Procesando video: {video_path}")
    audio_path = convertir_video_a_audio(video_path)
    texto = transcribir_audio_a_texto(audio_path)
    print(f"Transcripción completada. Texto extraído: {texto[:500]}")  # Imprime los primeros 500 caracteres

    # Opcional: eliminar el archivo de audio para ahorrar espacio
    os.remove(audio_path)

# Asumiendo que tienes el video de Facebook descargado como "video_de_facebook.mp4"
video_path = "video_de_facebook.mp4"
procesar_video(video_path)



if __name__ == "__main__":
    pass
