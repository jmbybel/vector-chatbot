This will be a project to create a chatbot with a LLM, interacted with via text-to-speech for the prompt responses

for the initial version will use Google TTS, local Llama2 via ollama

attempting to use VLC for the audio in initial work. will probably switch later


externally need to start a local Ollama llama2 instance
    * from their quickstart guide, after install just:
    * ollama run llama2 

pip installs needed so far:

    * langchain
    
    * langchain-community
    
    * python-vlc
    
    * gTTS
    
    * speechrecognition
    
    * setuptools
    
        ** due to errors from distutils
    *possibly pyttsx3

    * pyaudio, for saving files
