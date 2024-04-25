import cozmo
from cozmo.util import degrees
import cv2
import os

# File path configuration
parent_dir = "/Users/little/CozmoProject/Cozmo-Project"
path = os.path.join(parent_dir, "images")

# Only needs to be run once
try:
    os.mkdir(path)
except FileExistsError:
    print("Directory already exists")

def take_pictures(robot: cozmo.robot.Robot):
  # Initial setup, generate repeatable head angle and lift height
  robot.say_text("Taking pictures").wait_for_completed()
  move_arms = robot.set_lift_height(0)
  move_arms.wait_for_completed()
  set_head = robot.set_head_angle((cozmo.robot.MAX_HEAD_ANGLE) / 3, in_parallel = True)
  set_head.wait_for_completed()
  # Enabling Cozmo Camera
  robot.camera.image_stream_enabled = True
  deg_step = 5
  
  # Saves picture of what Cozmo sees every 10 degrees.
  for d in range(0, 360, deg_step):
    fileName = "image" + str(d) + ".jpeg"
 
    robot.turn_in_place(degrees(deg_step)).wait_for_completed()
    
    latest_image = robot.world.latest_image
    # annotation seems to be important, we have had issues saving images if we don't annotate
    annotated = latest_image.annotate_image()

    if latest_image is not None:
      print("image = %s" % latest_image)
      converted = annotated.convert()
      file_path = os.path.join(path, fileName)
      converted.save(file_path, "JPEG", resolution=10)

cozmo.run_program(take_pictures)