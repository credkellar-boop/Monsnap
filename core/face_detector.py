import cv2


class FaceDetector:
    """Handles face detection modeling and coordinate scaling."""

    def __init__(self, scale_percent=50):
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )
        self.scale_percent = scale_percent

    def detect(self, frame):
        # Downsample frame for processing speed boost
        width = int(frame.shape[1] * self.scale_percent / 100)
        height = int(frame.shape[0] * self.scale_percent / 100)
        small_frame = cv2.resize(
            frame, (width, height), interpolation=cv2.INTER_AREA
        )

        gray = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = self.face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )

        # Scale coordinates back up to original frame size
        scaled_faces = []
        for x, y, w, h in faces:
            orig_x = int(x * (100 / self.scale_percent))
            orig_y = int(y * (100 / self.scale_percent))
            orig_w = int(w * (100 / self.scale_percent))
            orig_h = int(h * (100 / self.scale_percent))
            scaled_faces.append((orig_x, orig_y, orig_w, orig_h))

        return scaled_faces
