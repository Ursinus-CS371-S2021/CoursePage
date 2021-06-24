import glob
import subprocess
import os

for f in glob.glob("*.wav"):
    fout = f[0:-3] + "mp3"
    if not os.path.exists(fout):
        print(fout)
        subprocess.call(["ffmpeg", "-i", f, fout])
