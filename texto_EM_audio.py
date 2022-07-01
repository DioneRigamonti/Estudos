from gtts import gTTS
from playsound import playsound
import os

audio = 'audio.mp3'
language = 'pt-br'

sp = gTTS(text = 'Meu primeiro áudio gerado através de texto em Python .', lang=language)

# - - Salvando o audio - -
sp.save(audio)
# - - Tocando o audio - -
playsound(audio)
# - - Removendo o arquivo.
os.remove(audio)

