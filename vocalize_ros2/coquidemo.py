#!/usr/bin/env python3
# Software License Agreement (BSD License)
# Vocalize String data on /vocalize to espeak-ng Text To Speech

#Ubuntu 20
#sudo apt install tts
#pip install tts
#pip install -r requirements.txt
#pip install sounddevice
#sudo apt-get install libportaudio2
#rclpy missing? Source /opt/ros/humble/setup.bash

import torch
from TTS.api import TTS
import sounddevice as sd

if __name__ == '__main__':
    maxspeaker = 108
    from TTS.api import TTS

    # List available 🐸TTS models
    print(TTS().list_models())

    # Get device
    device = "cuda" if torch.cuda.is_available() else "cpu"

    #Init TTS
    model_name = "tts_models/en/vctk/vits"
    if model_name:
        tts = TTS(model_name = model_name).to(device)

    # Run TTS with Speakers ID
    for i in range(0, maxspeaker+1):
        print(tts.speakers[i])
        wav = tts.tts("Hello, nice to meet you. I am speaker " + str(i) + " named " + tts.speakers[i] + ". It was a dark and stormy night. You hear a stirring in Granny's apple pie bakery. It sounds like little kobolds are trying to rob the place. I'm here to pledge my allegiance to Krondor and to Lord Serpent X.", speaker=tts.speakers[i])
        sd.play(wav, 22050)
        sd.wait()


