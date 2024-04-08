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

    voice = "zh-yue"
    speed = 150
    amplitude = 150
    pitch = 90
    wordgap = 15
    lastdata = ""

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
        elif inputdata == "ImperialMarch":
            self.speech = ""
            bashCommand = "play /home/ubuntu/ros_ws/src/vocalize_ros2/resource/AudioFX/ImperialMarch.mp3"
            subprocess.run(bashCommand, shell=True)
        else:
            self.speech = inputdata

        self.lastdata = inputdata

        bashCommand = "echo " + self.speech + " | espeak-ng -v " + self.voice + " -p " + str(self.pitch) + " -a " + str(self.amplitude) + " -g " + str(self.wordgap) + " -s " + str(self.speed)
        print(bashCommand)
        subprocess.run(bashCommand, shell=True, check=True)

def main(args=None):
    rclpy.init(args=None)
    vocalize_node = VocalizeNode()
    print("Starting")
    rclpy.spin(vocalize_node)
    vocalize_node.destroy_node()
    rclpy.shutdown()
    print("Exiting")

if __name__ == "__main__":
    main()
