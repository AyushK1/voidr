import Queue
import time
import threading
from video_capture import run_video

class thisThread(threading.Thread):
    def __init__(self, threadID):
	threading.Thread.__init__(self)
	self.threadID = threadID
    def run(self):
	#A value of 1 runs the video thread
	if (threadID):
	    run_video()
	#A value of 0 runs the signal thread
	else:
	    pass
	    #Your code goes here and should replace the pass

vid_thread = thisThread(1)
sig_thread = thisThread(0)

q = Queue()

vid_thread.start()
sig_thread.start()

if (not q.empty()):
    pass
    #Insert code here to replace the pass
