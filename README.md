# Monsnap
​A real-time video streaming and facial recognition platform. Built with Python and OpenCV, Monsnap handles high-performance, threaded RTSP/hardware camera feeds, automated face detection, and intelligent snapshot captures.
MonSnap/
├── .gitignore               # Keeps temporary Python files and video logs out of Git
├── README.md                # Project overview, installation steps, and hardware setup
├── requirements.txt         # List of dependencies (opencv-python, etc.)
├── main.py                  # Main orchestration loop (the script we built)
├── core/
│   ├── __init__.py
│   ├── stream_handler.py    # Holds the RTSPCameraStream threading class
│   └── face_detector.py     # Holds detection models (Haar Cascade, FaceNet, etc.)
└── data/
    ├── known_faces/         # Folder to store reference photos for future face recognition
    └── snapshots/           # Target folder for saving images when a face is detected
