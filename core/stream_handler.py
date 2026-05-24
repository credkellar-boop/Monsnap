import os
import queue
import threading
import time
import cv2


class RTSPCameraStream:
    """Handles camera connection in a separate thread to eliminate network stream lag."""

    def __init__(self, rtsp_url):
        # Force TCP transport instead of UDP for stream stability
        os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;tcp"

        self.cap = cv2.VideoCapture(rtsp_url, cv2.CAP_FFMPEG)
        self.q = queue.Queue(maxsize=3)
        self.stopped = False

        if not self.cap.isOpened():
            print(f"❌ Error: Unable to open RTSP stream at {rtsp_url}")
            exit(-1)

        self.thread = threading.Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        while not self.stopped:
            ret, frame = self.cap.read()
            if not ret:
                time.sleep(0.1)
                continue

            if self.q.full():
                try:
                    self.q.get_nowait()
                except queue.Empty:
                    pass
            self.q.put(frame)

    def read(self):
        return self.q.get()

    def release(self):
        self.stopped = True
        self.thread.join()
        self.cap.release()
