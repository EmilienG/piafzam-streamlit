import streamlit as st
import requests
import pandas as pd
from datetime import date, time
import numpy as np


spell = st.secrets['spell']
key = st.secrets.some_magic_api.key


st.title("PIAFZAM 🕊️")
st.caption("Quel espece d'oiseau est en train de chanter 🎵?")

# 1. Contrôleurs (upload) — PNG / JPG, pas d'audio

audio_value = st.audio_input("Record high quality audio", sample_rate=44100)

if audio_value:
    st.audio(audio_value)

#Transforme le dossier en WAV ou MP3
file_type = audio_value.type if hasattr(audio_value, "type") else "audio/wav"
file_extension = file_type.split("/")[-1]

files = {
    "file": (
        f"recording.{file_extension}",
        audio_value.getvalue(),
        file_type,
    )
}

url = key

# Bouton pour déclencher la requête
if st.button("Analyser l'audio"):
    with st.spinner("Analyse en cours..."):
        # Utilisation de POST et files= pour l'envoi de fichier
        response = requests.post(url, files=files)

        if response.status_code == 200:
            prediction = response.json()
            st.write(prediction)
        else:
            st.error(f"Erreur {response.status_code} : {response.text}")
