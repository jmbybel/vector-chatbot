Log of issues related to streaming / using temporary files / file-like objects with the various players so far (windows 11):

   * VLC - Works ok with playing saved files. plays a burst of static instead of audio if the active output device is on the "wrong" channel of a multi-channel output - like a SteelSeries headset. Doesn't seem to accept file-like objects
   * pydub - almost works, but required adding FFMpeg, then raised permission exceptions when attempting to play the BytesIO file-like as an mp3.
   * pyaudio - doesn't handle MP3s, which would force a change from google's gTTS, or adding some middle ground to get a file-like of a WAV
   * playsound - fails to open. errors similar to https://github.com/TaylorSMarks/playsound/issues/121 even though that's marked as fixed. downgrading to playsound 1.2.2 did not address it.
   * pygame - not tried yet




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
