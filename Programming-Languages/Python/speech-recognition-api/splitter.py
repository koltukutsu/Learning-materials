import pydub
# import librosa

# duration = librosa.get_duration(filename="/home/semih/Documents/teknofest_SH.wav")
# print(duration)
newAudio = pydub.AudioSegment.from_wav("/home/semih/Documents/teknofest_SH.wav")
duration = newAudio.duration_seconds
print(duration)
# factor = 20
# division = int(duration / factor)

for i in range(0, int(duration), 15):

# in seconds
# final time = 20

    t1 = i  * 1000 #Works in milliseconds
    t2 = (i + 15) * 1000
    print(t1)
    print(t2)

    newAudio2 = newAudio[t1:t2]
    newAudio2.export(f'/home/semih/Documents/video/{i}.wav', format="wav") #Exports to a wav file in the current path.

newAudio = newAudio[t2:]
newAudio.export('/home/semih/Documents/video/last.wav', format="wav") #Exports to a wav file in the current path.
