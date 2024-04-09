#!/usr/bin/env python3
# Software License Agreement (BSD License)
# Vocalize String data on /vocalize to espeak-ng Text To Speech

#sudo apt install espeak-ng
#sudo apt-cache search mbrola
#sudo apt install mbrola mbrola-us1 mbrola-us2 mbrola-us3
#sudo apt install sox
#sudo apt-get install libsox-fmt-mp3

import rclpy
import subprocess
from std_msgs.msg import String
from rclpy.node import Node
from rclpy.parameter import Parameter

class VocalizeNode(Node):
    def __init__(self):
        super().__init__('vocalize_node')
        self.subscription = self.create_subscription(
            String,
            '/vocalize',
            self.response_callback,
            10
        )
        self.subscription = self.create_subscription(
            String,
            '/gpt/response',
            self.response_callback,
            10
        )

        self.declare_parameters(
            namespace='',
            parameters=[
                ('voice', 'zh-yue'),
                ('speed', 150),
                ('amplitude', 150),
                ('pitch', 90),
                ('wordgap', 15)
            ]
        )

        self.lastdata = ""
        self.voice = ""
        self.speed = 0
        self.amplitude = 0
        self.pitch = 0
        self.wordgap = 0

    def get_parameters(self):
        self.voice = self.get_parameter('voice').value
        self.speed = self.get_parameter('speed').value
        self.amplitude = self.get_parameter('amplitude').value
        self.pitch = self.get_parameter('pitch').value
        self.wordgap = self.get_parameter('wordgap').value

    def response_callback(self, msg):
        self.get_parameters()

        #Scrub Data
        inputdata = msg.data
        inputdata = inputdata.replace('"', '')
        inputdata = inputdata.replace("'", "")
        inputdata = inputdata.replace("\n", "")

        if inputdata == self.lastdata:
            self.speech = ""
        else:
            self.speech = inputdata

        self.lastdata = inputdata

        if self.speech != "":
            self.get_logger().info('Vocalize: ' + str(self.speech))
            bashCommand = "echo " + self.speech + " | espeak-ng -v " + self.voice + " -p " + str(self.pitch) + " -a " + str(self.amplitude) + " -g " + str(self.wordgap) + " -s " + str(self.speed)
            print(bashCommand)
            subprocess.run(bashCommand, shell=True, check=True)

def main(args=None):
    rclpy.init(args=None)
    vocalize_node = VocalizeNode()
    print("Starting Vocalize Node")
    rclpy.spin(vocalize_node)
    vocalize_node.destroy_node()
    rclpy.shutdown()
    print("Exiting")

if __name__ == "__main__":
    main()
