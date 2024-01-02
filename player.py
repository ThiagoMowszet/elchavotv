import os
import random
import time
from subprocess import Popen

# Especifica la nueva ruta donde se encuentran tus videos
custom_path = "/run/media/thiago/New Volume/El Chavo Del Ocho/1972/"
directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), custom_path)

videos = []


def getVideos():
    global videos
    videos = []
    for file in os.listdir(directory):
        # Cambiar por el .{} necesario.
        if file.lower().endswith('.avi'):
            videos.append(os.path.join(directory, file))
    print("Videos encontrados:", videos)


def playVideos():
    global videos
    if len(videos) == 0:
        getVideos()
        time.sleep(5)
        return
    random.shuffle(videos)
    for video in videos:
        print(f"Reproduciendo video: {video}")
        playProcess = Popen(['mpv', video])
        playProcess.wait()


while True:
    playVideos()
