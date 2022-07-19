import os
import pydub
# import librosa

# duration = librosa.get_duration(filename="/home/semih/Documents/teknofest_SH.wav")
# print(duration)
FILE = "tanitim.wav"
PATH = os.path.join(os.getcwd(), FILE)
FILE_NAME = FILE.rstrip(".wav")
OUTPUT_PATH = os.path.join(os.getcwd(), f"output{FILE_NAME}")
newAudio = pydub.AudioSegment.from_wav(PATH)
duration = newAudio.duration_seconds
print(duration)
# factor = 20
# division = int(duration / factor)

print(OUTPUT_PATH)
os.mkdir(OUTPUT_PATH)

for i in range(0, int(duration), 15):

    # in seconds
    # final time = 20

    t1 = i * 1000  # Works in milliseconds
    t2 = (i + 15) * 1000
    print(t1)
    print(t2)

    newAudio2 = newAudio[t1:t2]

    # Exports to a wav file in the current path.
    newAudio2.export(f'{OUTPUT_PATH}/{i}.wav', format="wav")

newAudio = newAudio[t2:]
# Exports to a wav file in the current path.
newAudio.export(f'{OUTPUT_PATH}/last.wav', format="wav")
