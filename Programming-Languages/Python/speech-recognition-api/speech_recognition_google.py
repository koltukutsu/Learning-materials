from google.cloud import speech
import os
import io
from glob import glob
## export GOOGLE_APPLICATION_CREDENTIALS="/home/semih/Downloads/glassy-landing-319407-6a659dafec34.json"
# Creates google client
client = speech.SpeechClient()
a = ["first", "second", "third", "fourth"]
for i, item in enumerate(glob("/home/semih/Documents/video/*")):
    # Full path of the audio file, Replace with your file name
    print(f"{i}..in order..{item}")
    file_name = os.path.join("/home/semih/Documents", item)

    #Loads the audio file into memory
    with io.open(file_name, "rb") as audio_file:
        content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        audio_channel_count=2,
        language_code="en-US",
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