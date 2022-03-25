# gtts          ; 문자를 음성으로 변환해주는 라이브러리 필요. (pip install gtts)
# playsound     ; mp3를 재생해주는 라이브러리 필요. issue 사항으로 1.2.2 버전 사용 (pip install playsound==1.2.2)

from gtts import gTTS
from playsound import playsound

import os

path = os.path.dirname(os.path.realpath(__file__))
filename = "voice.mp3"

text_file = "voice.txt"
text_path = os.path.join(path, text_file);

with open(text_path, 'rt', encoding='UTF8') as f:
    read_file = f.read()

tts = gTTS(text=read_file, lang='ko')
tts.save(filename)

# mp3 재생
playsound(filename)