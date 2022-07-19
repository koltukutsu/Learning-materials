from google.cloud import speech
import os
import io
from glob import glob

# export GOOGLE_APPLICATION_CR
# EDENTIALS="/home/semih/Documents/speechtext-324715-2559ab3aad1f.json"

# Creates google client

client = speech.SpeechClient()
# LANGUAGE_CODE = "en-US"
LANGUAGE_CODE = "tr-TR"
SPLITTED_WAV_PATH = "outputtanitim"
PATH = os.path.join(os.getcwd(), SPLITTED_WAV_PATH)
PATH_OF_FINAL_WAVS = PATH + "/*.wav"

# a = ["first", "second", "third", "fourth"]
print("started")
# print(os.getcwd())
# print(PATH)
# print(PATH_OF_FINAL_WAVS)
print(glob(PATH_OF_FINAL_WAVS))
for i, item in enumerate(glob(PATH_OF_FINAL_WAVS)):
    # Full path of the audio file, Replace with your file name
    print(f"{i}..in order..{item}")
    file_name = os.path.join(PATH, item)

    # Loads the audio file into memory
    with io.open(file_name, "rb") as audio_file:
        content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        audio_channel_count=2,
        language_code=LANGUAGE_CODE,
    )

    # Sends the request to google to transcribe the audio
    response = client.recognize(request={"config": config, "audio": audio})

    # Reads the response
    for result in response.results:
        sonuc = result.alternatives[0].transcript
        print("Transcript: {}".format(sonuc))
        item = item.rstrip(".wav")
        with open(f"{item}.txt", "w") as ma:
            ma.write(sonuc)
print("ended")
