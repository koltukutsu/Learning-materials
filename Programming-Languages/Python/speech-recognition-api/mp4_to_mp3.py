# import moviepy.editor as mpe
# import os

# PATH = "/home/semih/Downloads"
# FINAL_PATH = "/home/semih/Documents"
# MP4_FILE = "Teknofest 2021 (Steve Hoffman) Keynote.mp4"
# MP3_FILE = "teknofest_SH.mp3"

# video = mpe.VideoFileClip(os.path.join(PATH, MP4_FILE))
# video.audio.write_audiofile(os.path.join(FINAL_PATH, MP3_FILE))
import os
from pydub import AudioSegment

SRC = "/home/semih/Documents/teknofest_SH.mp3"
DST = "/home/semih/Documents/teknofest_SH.wav"

sound = AudioSegment.from_mp3(SRC)
sound.export(DST, format="wav") 
