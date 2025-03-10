import os
import json

directory = os.listdir("./Songs/")
audioFiles = []

audioExtensions = ["mp3", "ogg", "flac"]
for f in directory:
    if f.split(".")[1] in audioExtensions:
        audioFiles.append({"Filename":"./Songs/" + f, "Title":f.split(".")[0]})

audioJsonFile = open("AudioFiles.js", "w")
audioJsonFile.write("var files = ")
json.dump(audioFiles, audioJsonFile)

audioJsonFile.write("; ")
audioJsonFile.close()




