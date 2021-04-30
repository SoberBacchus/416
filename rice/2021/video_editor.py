from moviepy.editor import *

import os

video = VideoFileClip( "C:\\Users\\chris\\rice\\macrosCollege\\vid.mp4").subclip(6*60, 9*60)

video.write_videofile("vid2.mp4",fps=25) # Many options...
