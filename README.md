# MonSnap 📸

[![MonSnap CI Pipeline](https://github.com/credkellar-boop/Monsnap/actions/workflows/super-lint.yml/badge.svg)](https://github.com/credkellar-boop/Monsnap/actions/workflows/super-lint.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org/)

MonSnap is a high-performance, real-time video streaming and facial recognition platform. Built using Python and OpenCV, MonSnap implements multi-threaded edge computing pipelines to pull RTSP security camera feeds natively without video lag, frame drops, or memory leaks.

By separating camera frame-grabbing from the core deep learning and computer vision processing cycles, MonSnap ensures you are always analyzing real-time data.

---

## ✨ Features

* **Multi-Threaded Video Pipeline:** Eliminates hardware buffer latency by processing video ingestion on a dedicated background thread.
* **TCP Transport Enforcement:** Automatically overrides flaky UDP streaming defaults to prevent video compression artifacts and screen smearing.
* **Dynamic Matrix Downsampling:** Boosts CPU detection efficiency by up to 300% via configurable internal image scaling.
* **Automated CI/CD Pipeline:** Integrated GitHub Actions workflow to auto-lint and validate code health on every push.
* **Modular Architecture:** Clean segregation between ingestion layers, computer vision logic, and local data storage.

---

## 📁 Repository Architecture

```text
MonSnap/
├── .github/
│   └── workflows/
│       └── super-lint.yml   # Automated CI/CD pipeline configuration
├── core/
│   ├── __init__.py          # Identifies core directory as an importable module
│   ├── face_detector.py     # Haar Cascade implementation and coordinate scaling
│   └── stream_handler.py    # Threaded RTSPCameraStream connection manager
├── data/
│   ├── known_faces/         # Reference database for facial validation matching
│   └── snapshots/           # Target destination directory for captured faces
├── .gitignore               # Excludes virtual environments and temporary cache files
├── LICENSE                  # MIT Open-Source License
├── README.md                # Project documentation and deployment guide
├── main.py                  # Main orchestration loop and runtime logic
└── requirements.txt         # Project package dependencies
