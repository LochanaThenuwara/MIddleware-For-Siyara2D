import threading
import time
import TCPSocket
import WebsocketServer
import RealTimedb
import Cache

import SocketServer
import json

exitFlag = 0

class WebSocketThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        WebsocketServer.funcWS()
        #execfile('WebsocketServer.py')
        # print "Starting " + self.name
        # print_time(self.name, self.counter, 5)
        # print "Exiting " + self.name

class TCPsocketThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        # print_time(self.name, self.counter, 5)
        print "Exiting " + self.name
        TCPSocket.funcTCP()

# class DbThread(threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#
#     def run(self):
#         RealTimedb.dbConnection()

class ChangeFeedThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print "Starting " + self.name
            # print_time(self.name, self.counter, 5)
        print "Exiting " + self.name
        Cache.changeFeed()

# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#             threadName.exit()
#         time.sleep(delay)
#         print "%s: %s" % (threadName, time.ctime(time.time()))
#         counter -= 1

# Create new threads
thread1 = WebSocketThread(1, "Thread-1", 1)
thread2 = TCPsocketThread(2, "Thread-2", 2)
# thread3 = DbThread(2, "Thread-3", 3)
thread4 = ChangeFeedThread(2, "Thread-4", 3)

# Start new Threads
thread1.start()
# thread3.start()
thread2.start()
thread4.start()


print "Exiting Main Thread"