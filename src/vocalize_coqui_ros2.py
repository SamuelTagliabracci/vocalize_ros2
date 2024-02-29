#!/usr/bin/env python3
# Software License Agreement (BSD License)
# Vocalize String data on /vocalize to espeak-ng Text To Speech

#sudo apt install tts
#pip install tts
#pip install -r requirements.txt
#pip install sounddevice
#sudo apt-get install libportaudio2
#rclpy missing? Source /opt/ros/humble/setup.bash

from TTS.api import TTS
import sounddevice as sd
import rclpy
from std_msgs.msg import String
from rclpy.node import Node

class VocalizeNode(Node):
    def __init__(self):
        super().__init__('vocalize_node')

        self.subscription1 = self.create_subscription(
            String,
            '/chatgpt/response',
            self.response_callback,
            10
        )

        self.subscription2 = self.create_subscription(
            String,
            '/objects/people',
            self.response_callback,
            10
        )

        self.subscription3 = self.create_subscription(
            String,
            '/vocalize',
            self.response_callback,
            10
        )

        # self.speaker = 80 #Sexy Girl Voice
        self.speaker = 61 #Deep Lord Commander
#        self.speaker = 81 #Dashing Knight
#        self.speaker = 72 #Dashing Adventurer
#        self.speaker = 59 #Dark Rogue Guy
        self.lastdata = ""
        self.gpu = True

        #Init TTS
        self.model_name = "tts_models/en/vctk/vits"
        if self.model_name:
            self.tts = TTS(model_name = self.model_name, gpu=self.gpu)
        else:
            self.model_path = "models/SerpentX/model_file.pth"
            self.config_path = "models/SerpentX/config.json"
            self.tts = TTS(model_path = self.model_path, config_path = self.config_path, gpu = self.gpu)

    def response_callback(self, msg):
    #    node = rclpy.get_node('vocalize_node')
    #    node.get_logger().info('Vocalize: %s', msg.data)

        if msg.data[:2].isdigit() and msg.data[2] == ':':
            self.speaker = int(msg.data[:2])
            msg.data = msg.data[2:]

        #Scrub Data
        inputdata = msg.data
        inputdata = inputdata.replace('"', '')
        inputdata = inputdata.replace("'", "")
        inputdata = inputdata.replace("\n", "")

        if inputdata == self.lastdata or not inputdata:
            self.speech = ""
            return(0)
        else:
            self.speech = inputdata

        self.lastdata = inputdata


        # Run TTS with Speakers ID
        if self.speaker:
            wav = self.tts.tts(inputdata, speaker=self.tts.speakers[self.speaker])
        else:
            # Run TTS without speaker
            wav = self.tts.tts(inputdata)

        #, language=self.tts.languages[0])

        # Text to speech to a file
        #tts.tts_to_file(text=inputdata, file_path="output.wav")

        sd.play(wav, 22050)
        sd.wait()

if __name__ == '__main__':
    rclpy.init(args=None)
    vocalize_node = VocalizeNode()
    rclpy.spin(vocalize_node)
    vocalize_node.destroy_node()
    rclpy.shutdown()
