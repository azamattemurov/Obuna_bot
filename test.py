import os

audio_file = "music/O'ylab ko'r - 1.mp3"

if not os.path.isfile(audio_file):
    print(f"Fayl mavjud emas: {audio_file}")
else:
    print(f"Fayl mavjud: {audio_file}")
