#!/usr/bin/env python3
# Software License Agreement (BSD License)
# Vocalize String data on /vocalize to ElevenLabs Text To Speech

from elevenlabs.client import ElevenLabs
from elevenlabs import play

import sounddevice as sd
import rclpy
from std_msgs.msg import String
from rclpy.node import Node

class VocalizeNode(Node):
    def __init__(self):
        super().__init__('vocalize_node')

        self.subscription_response = self.create_subscription(
            String,
            '/gpt/response',
            self.response_callback,
            10
        )

        self.subscription_vocalize = self.create_subscription(
            String,
            '/vocalize',
            self.response_callback,
            10
        )

        self.client = ElevenLabs(
          # Defaults to ELEVEN_API_KEY
#          api_key=""
        )

#        self.voice = "Carter the Mountain King"
        self.voice = "Ava - Calm and slow"
        self.model = "eleven_multilingual_v2"
        self.lastdata = ""

    def response_callback(self, msg):

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

        audio = self.client.generate(text=inputdata, voice=self.voice, model=self.model)
        play(audio)
#        sd.play(audio)
#        sd.wait()

if __name__ == '__main__':
    rclpy.init(args=None)
    vocalize_node = VocalizeNode()
    rclpy.spin(vocalize_node)
    vocalize_node.destroy_node()
    rclpy.shutdown()
