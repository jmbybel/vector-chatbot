
from gtts import gTTS

import os
import time

#hardcode audio file save/load location to be windows directory C:/programming/data/sound/gtts
#TODO later move to a configurable spot
baseDirectory = "C:/programming/data/sound/gtts"
language = "en"

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

#utility function to create directories if they do not exist
def util_createPathIfMissing(path):
    if not os.path.exists(path):
        os.makedirs(path)


#generate a hello world audio file with gtts
def test_generateHelloWorldAudio():
    #if the file already exists, don't recreate hello world.
    if os.path.isfile(baseDirectory + "/helloWorld.mp3"):
        return baseDirectory + "/helloWorld.mp3"

    return generateAudioFile("Hello World", "helloWorld")


def main():
    filePath = test_generateHelloWorldAudio()

if __name__ == "__main__":
    main()