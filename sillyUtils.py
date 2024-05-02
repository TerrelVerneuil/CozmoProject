import cozmo
import asyncio
import os
from PIL import Image as im 

notes = [cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.Quarter),
         cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.Quarter),
         cozmo.song.SongNote(cozmo.song.NoteTypes.F2, cozmo.song.NoteDurations.Quarter),
         cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Quarter),
         cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Quarter),
         cozmo.song.SongNote(cozmo.song.NoteTypes.F2, cozmo.song.NoteDurations.Quarter),
         cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.Quarter),
         cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Quarter),
         cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter),
         cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter),
         cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Quarter),
         cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.Quarter),
         cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.Quarter),
         cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.Quarter),
         cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Quarter),
         cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Half),]

# Play the song lyrics
def sign_song(robot: cozmo.robot.Robot):
    robot.play_song(song_notes=notes, loop_count=1, in_parallel=False, num_retries=0).wait_for_completed()
    
#cosmo displays a picture of his "home" on his face display
#requires directory change
def face_display_home(robot: cozmo.robot.Robot):
    parent_dir = r"C:\Users\Dressler\Pictures"
    path = os.path.join(parent_dir, "cozmo_resized")
    source_image_path = os.path.join(path, "image0.jpeg")
    source_image = im.open(source_image_path)
    displayImage = source_image.resize(cozmo.oled_face.dimensions(), im.NEAREST)
    image_screen_data = cozmo.oled_face.convert_image_to_screen_data(displayImage)
    robot.display_oled_face_image(image_screen_data, 1000.0).wait_for_completed(10)