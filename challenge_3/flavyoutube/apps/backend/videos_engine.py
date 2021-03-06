#!/usr/sbin/env python
#encoding: utf-8

from subprocess import Popen, PIPE, STDOUT
import tempfile
import os

VIDEOS_PATH = "/home/flavio/devel/globaltests/challenge_3/flavyoutube/media/videos/"

class VideoEngine(object):
    def __init__(self, video_path, rotate=False):
        self.video_path = video_path
        self.extension = self.video_path[self.video_path.rindex("."):]
        self.pure_name =  self.video_path[self.video_path.rindex("/"):self.video_path.rindex(".")]       
        self.new_video_path = VIDEOS_PATH + self.pure_name + ".ogv"
        print '*** criou video engine', self.pure_name, self.new_video_path, self.extension

        if rotate==True:
            self._rotate_video()

    def get_screenshot(self):
        print '*** pegando o screenshot'
        screenshot = tempfile.NamedTemporaryFile()
        filename = screenshot.name + ".png"
        screenshot.close()
        try:
            command = "ffmpeg -i %s -an -ss 00:00:03 -an -r 1 -vframes 1 -s 290x168 %s" % (self.video_path, filename)
            p = Popen(command.split(), stdout=PIPE, stdin=PIPE, stderr=STDOUT)
            p.communicate()
            screenshot = open(filename)
        except:
            command = "ffmpeg -i %s -an -ss 00:00:01 -an -r 1 -vframes 1 -s 290x168 %s" % (self.video_path, filename)
            p = Popen(command.split(), stdout=PIPE, stdin=PIPE, stderr=STDOUT)
            p.communicate()
            screenshot = open(filename)

        return screenshot

    def get_encoded_video_path(self):
        print '*** gerando o ogg'
        command = "ffmpeg2theora %s -o %s" % (self.video_path, self.new_video_path)
#        command = "ffmpeg -i %s -acodec copy -vcodec copy %s" % (self.video_path, self.new_video_path)
#        command = "HandBrakeCLI -Z Universal -i %s -o %s --rate 29.97" % (self.video_path, self.new_video_path)
        print command
        p = Popen(command.split(), stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        p.communicate()
        return self.new_video_path

    def _rotate_video(self):
        print '*** rotacionando o video'
        command = "mencoder %s -vf rotate=1 -oac copy -ovc lavc  -o %s" % (self.video_path, "/tmp/" + self.pure_name + "-rotated" + self.extension)
        p = Popen(command.split(), stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        p.communicate()
        self.video_path = "/tmp/" + self.pure_name + "-rotated" + self.extension
       
if __name__ == "__main__":
    a = VideoEngine("/home/flavio/samples/sample1.avi", rotate=True)
    a.get_screenshot()
    a.get_encoded_video_path()
    a = VideoEngine("/home/flavio/samples/sample2.mpeg", rotate=True)
    a.get_screenshot()
    a.get_encoded_video_path()
    a = VideoEngine("/home/flavio/samples/sample3.mpg", rotate=True)
    a.get_screenshot()
    a.get_encoded_video_path()
    a = VideoEngine("/home/flavio/samples/sample4.avi", rotate=True)
    a.get_screenshot()
    a.get_encoded_video_path()






