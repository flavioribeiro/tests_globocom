#!/usr/sbin/env python
#encoding: utf-8

from subprocess import Popen, PIPE, STDOUT
import tempfile
import os

VIDEOS_PATH = "/home/flavio/devel/globaltests/challenge_3/flavyoutube/media/videos/"

class VideoEngine(object):
    def __init__(self, video_path):
        self.video_path = video_path
        self.extension = self.video_path[self.video_path.rindex("."):]
        self.pure_name =  self.video_path[self.video_path.rindex("/"):self.video_path.rindex(".")]       
        self.new_video_path = VIDEOS_PATH + self.pure_name + ".mp4"

    def get_screenshot(self):
        screenshot = tempfile.NamedTemporaryFile()
        filename = screenshot.name + ".png"
        screenshot.close()
	command = "ffmpeg -i %s -an -ss 00:00:03 -an -r 1 -vframes 1 -s 290x168 %s" % (self.video_path, filename)
        p = Popen(command.split(), stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        p.communicate()
        print filename

    def get_encoded_video_path(self, rotate=False):
        if rotate:
            self._rotate_video()

        command = "ffmpeg -i %s -acodec copy -vcodec copy %s" % (self.video_path, self.new_video_path)
        p = Popen(command.split(), stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        p.communicate()
        print self.new_video_path

    def _rotate_video(self):
        command = "mencoder %s -vf rotate=1 -oac copy -ovc lavc  -o %s" % (self.video_path, "/tmp/" + self.pure_name + "-rotated" + self.extension)
        p = Popen(command.split(), stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        p.communicate()
        self.video_path = "/tmp/" + self.pure_name + "-rotated" + self.extension
       
if __name__ == "__main__":
    a = VideoEngine("/home/flavio/devel/globaltests/challenge_3/flavyoutube/apps/backend/sample1.avi")
    a.get_screenshot()
    a.get_encoded_video_path(rotate=True)
    a = VideoEngine("/home/flavio/devel/globaltests/challenge_3/flavyoutube/apps/backend/sample2.mpeg")
    a.get_screenshot()
    a.get_encoded_video_path(rotate=True)
    a = VideoEngine("/home/flavio/devel/globaltests/challenge_3/flavyoutube/apps/backend/sample3.mpg")
    a.get_screenshot()
    a.get_encoded_video_path(rotate=True)
    a = VideoEngine("/home/flavio/devel/globaltests/challenge_3/flavyoutube/apps/backend/sample4.avi")
    a.get_screenshot()
    a.get_encoded_video_path(rotate=True)
    a = VideoEngine("/home/flavio/devel/globaltests/challenge_3/flavyoutube/apps/backend/sample5.avi")
    a.get_screenshot()
    a.get_encoded_video_path(rotate=True)
    a = VideoEngine("/home/flavio/devel/globaltests/challenge_3/flavyoutube/apps/backend/sample6.mpeg")
    a.get_screenshot()
    a.get_encoded_video_path(rotate=True)



