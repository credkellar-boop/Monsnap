import cv2
from core.face_detector import FaceDetector
from core.stream_handler import RTSPCameraStream


def main():
    # --- CONFIGURATION ---
    # Replace with your camera's live stream feed URL or use 0 for local webcam
    RTSP_URL = "rtsp://admin:password@192.168.1.100:554/stream1"

    print("🔌 Starting MonSnap Stream...")
    cam = RTSPCameraStream(RTSP_URL)
    detector = FaceDetector(scale_percent=50)

    print("🚀 System Live. Press 'q' to exit.")

    while True:
        frame = cam.read()

        # Run detection
        faces = detector.detect(frame)

        # Draw overlays
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(
                frame,
                "Face Detected",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2,
            )

        # Display window
        cv2.imshow("MonSnap Platform", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    print("Shutting down MonSnap safely...")
    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
