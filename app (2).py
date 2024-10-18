import torch
from TTS.api import TTS
import streamlit as st
import os

# Check if CUDA is available
device = "cuda" if torch.cuda.is_available() else "cpu"

# Function to generate audio from text
def generate_audio(text="A journey of a thousand miles begins with a single step."):
    tts = TTS(model_name='tts_models/en/ljspeech/fast_pitch').to(device)
    output_path = "outputs/output.wav"
    tts.tts_to_file(text=text, file_path=output_path)
    return output_path

# Streamlit app layout
st.title("Text to Speech Application")
text_input = st.text_input("Enter the text you want to convert to speech:", "A journey of a thousand miles begins with a single step.")

if st.button("Generate Audio"):
    output_file = generate_audio(text_input)

    # Check if file exists and play audio
    if os.path.exists(output_file):
        st.audio(output_file, format="audio/wav")
        st.success("Audio generated successfully!")
    else:
        st.error("Error generating audio.")
