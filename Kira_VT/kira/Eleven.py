import pydub
import pydub.playback
import io
from elevenlabslib import *
import os

#Carga la key de Elevenlabs
def load_El_key():
    El_key_path = os.path.abspath("Kira_VT/kira/keys/El_key.txt")
    with open(El_key_path, "r") as f:
        return f.read().strip()

#define las variables de api y voz
API_KEY = load_El_key()
VOICE_NAME = "Elli"

#Crea la funcion de text to speach
def play(bytesData):
    sound = pydub.AudioSegment.from_file_using_temporary_files(io.BytesIO(bytesData))
    pydub.playback.play(sound)
    return

#define las variables de usuario y generacion de voz
user = ElevenLabsUser(API_KEY) 
voice = user.get_voices_by_name(VOICE_NAME)[0] 

