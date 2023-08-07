#!/usr/bin/env python3
# Software License Agreement (BSD License)
# Vocalize String data on /vocalize to espeak-ng Text To Speech

#sudo apt install tts
#pip install tts
#pip install -r requirements.txt
#pip install sounddevice

from TTS.api import TTS
import sounddevice as sd
import rclpy
from std_msgs.msg import String
from rclpy.node import Node

class VocalizeNode(Node):
    def __init__(self):
        super().__init__('vocalize_node')
        self.subscription = self.create_subscription(
            String,
            '/chatgpt/response',
            self.response_callback,
            10
        )

        self.speaker = 6
        self.lastdata = ""
        self.gpu = False

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

        #Scrub Data
        inputdata = msg.data
        inputdata = inputdata.replace('"', '')
        inputdata = inputdata.replace("'", "")
        inputdata = inputdata.replace("\n", "")

        if inputdata == self.lastdata:
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
