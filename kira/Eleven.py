import pydub
import pydub.playback
import io
from elevenlabslib import *


API_KEY = ""
VOICE_NAME = "Elli"

def play(bytesData):
    sound = pydub.AudioSegment.from_file_using_temporary_files(io.BytesIO(bytesData))
    pydub.playback.play(sound)
    return

user = ElevenLabsUser(API_KEY) 
voice = user.get_voices_by_name(VOICE_NAME)[0] 

