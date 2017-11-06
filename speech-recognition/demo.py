"""
Code modified from:
https://cloud.google.com/speech/docs/reference/libraries
and 
https://gist.github.com/mabdrabo/8678538
"""
import pyaudio
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
 
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 3
 
audio = pyaudio.PyAudio()
 
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print("recording...")
frames = []
 
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print("done")
 
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()


#merge into one binary string
all = b""
for frame in frames:
    all += frame

# Instantiates a Google Speech client
client = speech.SpeechClient()

audio = types.RecognitionAudio(content=all)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=RATE,
    language_code='en-US')

# Detects speech in the audio file
response = client.recognize(config, audio)

for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))