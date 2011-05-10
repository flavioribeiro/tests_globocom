#!/usr/sbin/env python
#encoding: utf-8

from subprocess import Popen, PIPE

class VideoEngine(object):
    def __init__(self, video_path):
        self.stream = pyffmpeg.VideoStream()
        self.stream.open(video_path)

    def get_screenshot(self):
	'''ffmpeg -i sample2.mpeg -an -ss 00:00:03 -an -r 1 -vframes 1 -s 640x390 teste.jpg'''
        return dir(self.stream)

    def get_encoded_video_path(self):
        '''ffmpeg -i {0} -y -b 200000 -r 25 -s 320x240 -acodec aac -ab 128kb -vcodec mpeg4 -b 1200kb -mbd 2 -flags +4mv -cmp 2 -subcmp 2 -s 640x390 {1}'''

    def rotate_video(self):
        '''mencoder -oac copy -ovc lavc -vf rotate=1 original.mp4 -o 90_CW_rotated.mp4'''

a = VideoEngine("/home/flavio/devel/globaltests/challenge_3/flavyoutube/apps/backend/sample1.avi")
a.get_screenshot()
a = VideoEngine("/home/flavio/devel/globaltests/challenge_3/flavyoutube/apps/backend/sample2.mpeg")
a.get_screenshot()

