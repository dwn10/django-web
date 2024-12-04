# 1) https://pypi.org/project/streamlit/

# 2) Terminal: cd PYTHON/Audio_a_Texto > pip install streamlit pyaudio pyperclip whisper
#                                   > streamlit run app.py

# 3) Welcome to Streamlit! / You can now view your Streamlit app in your browser.
        # Local URL: http://localhost:8501
        # Network URL: http://100.126.10.200:8501

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

import streamlit as st

# Shared Tailwind CSS classes
TW_BG = "bg-background"
TW_TEXT = "text-primary-foreground"
TW_CARD = "bg-card"
TW_INPUT = "bg-input"
TW_BTN = "bg-primary"
TW_BTN_HOVER = "hover:bg-primary/80"
TW_SECONDARY_BTN = "bg-secondary"
TW_SECONDARY_TEXT = "text-secondary-foreground"

def audio_transcription_app():
    st.markdown('<h1 class="text-3xl font-bold mb-4">Audio Transcription App</h1>', unsafe_allow_html=True)
    
    st.markdown('<div class="w-full max-w-md p-4 rounded-lg shadow-lg">', unsafe_allow_html=True)
    
    st.markdown('<label for="audioInput" class="block text-sm font-medium mb-2">Select Audio File:</label>', unsafe_allow_html=True)
    audio_input = st.file_uploader("Upload Audio File", type=["mp3", "wav", "ogg"])
    
    if audio_input:
        transcribe_btn = st.button("Transcribe", key="transcribe_btn")
        transcription_output = st.text_area("Transcription Output", height=200, placeholder="Transcription will appear here", key="transcription_output", disabled=True)
        copy_btn = st.button("Copy to Clipboard", key="copy_btn")
        
        if transcribe_btn:
            # Transcription logic here
            transcription_output.value = "Transcribed text will appear here"
        
        if copy_btn:
            st.text(transcription_output.value)
    
    st.markdown('</div>', unsafe_allow_html=True)

audio_transcription_app()
