
"""Sample code to use the IBM Watson Speech to Text API.
See more at https://blog.rmotr.com.
"""
import json
from watson_developer_cloud import SpeechToTextV1

IBM_USERNAME = "95ba9083-3632-4c04-bb53-f1fb9bf365b4"
IBM_PASSWORD = "jLkzXN1VpQnR"

stt = SpeechToTextV1(username=IBM_USERNAME, password=IBM_PASSWORD)
audio_file = open("audiotest.flac", "rb")


with open('transcript_result.json', 'w') as fp:
    result = stt.recognize(audio_file, content_type="audio/x-flac",
                           continuous=True, timestamps=False,
                           max_alternatives=1)
    json.dump(result, fp, indent=2)