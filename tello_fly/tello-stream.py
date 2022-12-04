#!/usr/bin/python3


import threading
import socket
import cv2


""" Welcome note """
print("\nTello Video Stream Program\n")


class Tello:
    def __init__(self):
        self._running = True
        self.video = cv2.VideoCapture("udp://0.0.0.0:11111",cv2.CAP_FFMPEG)
        if not self.video.isOpened():
            self.video.open('udp://0.0.0.0:11111')

    def terminate(self):
        self._running = False
        self.video.release()
        cv2.destroyAllWindows()

    def recv(self):
        """ Handler for Tello states message """
        while self._running:

                ret, frame = self.video.read()
                if ret:
                    # Resize frame


                    # Display the resulting frame
                    cv2.imshow('Tello', frame)
                # Wait for display image frame
                # cv2.waitKey(1) & 0xFF == ord('q'):
                if cv2.waitKey (1)&0xFF == ord ('q'):
                    break



""" Start new thread for receive Tello response message """
t = Tello()
recvThread = threading.Thread(target=t.recv)
recvThread.start()

while True:
    try:
        # Get input from CLI
        msg = input()

        # Check for "end"
        if msg == "bye":
            t.terminate()
            recvThread.join()
            print("\nGood Bye\n")
            break
    except KeyboardInterrupt:
        t.terminate()
        recvThread.join()
        break
