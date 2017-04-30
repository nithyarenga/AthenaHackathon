import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1
import speech2text_conf as conf
import os


def speech2text_conn(wav_foldername, wav_filename):
    speech_to_text = SpeechToTextV1(
        username=conf.text2speech_cred['username'],
        password=conf.text2speech_cred['password'],
        x_watson_learning_opt_out=False
    )
    speech_to_text.get_model('en-US_BroadbandModel')
    result = ''
    with open(os.path.join(wav_foldername, wav_filename), 'rb') as audio_file:
        result = json.dumps(speech_to_text.recognize(
            audio_file, content_type='audio/wav', timestamps=True, word_confidence=True), indent=2)
    return result