This will be a project to create a chatbot with a LLM, interacted with via text-to-speech for the prompt responses

for the initial version will use Google TTS, local Llama2 via ollama

attempting to use VLC for the audio in initial work. will probably switch later


externally need to start a local Ollama llama2 instance
    * from their quickstart guide, after install just:
    * ollama run llama2 

To stream the text-to-speech rather than save to a file, then read it, ffmpeg may eventually be needed...

    * https://ffmpeg.org/download.html


has a requirements.txt so can install requirements from pip easily.

    *  pip install -r requirements.txt

possible pip installs for future items?:
    
    * pydub (instead of python-vlc)
    
    *possibly pyttsx3