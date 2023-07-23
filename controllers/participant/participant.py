# Copyright 1996-2023 Cyberbotics Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Minimalist controller example for the Robot Wrestling Tournament.
   Demonstrates how to play a simple motion file."""

from controller import Robot
from controller import Camera
from PIL import Image
import numpy as np

import sys

# We provide a set of utilities to help you with the development of your controller. You can find them in the utils folder.
# If you want to see a list of examples that use them, you can go to https://github.com/cyberbotics/wrestling#demo-robot-controllers
sys.path.append('..')
from utils.motion_library import MotionLibrary

robot = Robot()

# Assuming the name of the bottom camera is 'bottom_camera'
bottom_camera = robot.getCamera('CameraBottom')
bottom_camera.enable(10)  # Enable the camera with a sampling period of 10 milliseconds (you can adjust the value)



class Wrestler (Robot):
    def run(self):
        # to load all the motions from the motions folder, we use the MotionLibrary class:
        motion_library = MotionLibrary()
        # retrieves the WorldInfo.basicTimeTime (ms) from the world file
        time_step = int(self.getBasicTimeStep())
       while robot.step() != -1:
    # Access the image data from the bottom camera
    image_data = bottom_camera.getImage()

    # Process the image data here (e.g., save the image, do image processing, etc.)

    # Optional: Break the loop when a certain condition is met
    # if some_condition:
    #     break

        while self.step(time_step) != -1:  # mandatory function to make the simulation run
            motion_library.play('TaiChi')


# create the Robot instance and run main loop
wrestler = Wrestler()
wrestler.run()
