
from gtts import gTTS
from audioPlayer import play_mp3_vlc, record_audio

import os
import time

#hardcode audio file save/load location to be windows directory C:/programming/data/sound/gtts
#TODO later move to a configurable spot
baseDirectory = "C:/programming/data/sound/gtts"
language = "en"

#generate a hello world audio file with gtts
def generateHelloWorldAudio():
    #if the file already exists, don't recreate hello world.
    if os.path.isfile(baseDirectory + "/helloWorld.mp3"):
        return baseDirectory + "/helloWorld.mp3"

    return generateAudioFile("Hello World", "helloWorld")

#generate an audio file with gtts from a given line of text
#return the full path of the audio file
#optionally save the file with a given name, otherwise it saves as the current system time in millis
def generateAudioFile(audioText, optionalFilename = None):
    tts = gTTS(text=audioText, lang=language)
    fullAudioFilePath = baseDirectory + "/" + str(int(time.time())) + ".mp3"
    if optionalFilename is not None:
        tts.save(baseDirectory + "/" + optionalFilename + ".mp3")
        fullAudioFilePath = baseDirectory + "/" + optionalFilename + ".mp3"
    util_createPathIfMissing(baseDirectory)
    tts.save(fullAudioFilePath)

    print("DEBUG", audioText)

    return fullAudioFilePath

def playAudioFile(audioFile):
    play_mp3_vlc(audioFile)

#utility function to create directories if they do not exist
def util_createPathIfMissing(path):
    if not os.path.exists(path):
        os.makedirs(path)


def main():
    filePath = generateHelloWorldAudio()
    playAudioFile(filePath)

if __name__ == "__main__":
    main()