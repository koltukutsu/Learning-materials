# import moviepy.editor as mpe
# import os

# PATH = "/home/semih/Documents/Work_Space/Learning-materials/Programming-Languages/Python/speech-recognition-api"
# FINAL_PATH = "/home/semih/Documents/Work_Space/Learning-materials/Programming-Languages/Python/speech-recognition-api"
# MP4_FILE = "videoplayback.mp4"
# MP3_FILE = "final.mp3"

# video = mpe.VideoFileClip(os.path.join(PATH, MP4_FILE))
# video.audio.write_audiofile(os.path.join(FINAL_PATH, MP3_FILE))


import os
from pydub import AudioSegment

SRC = "final.mp3"
DST = "tanitim.wav"

sound = AudioSegment.from_mp3(SRC)
sound.export(DST, format="wav")
