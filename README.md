# MonSnap 📸

[![MonSnap CI Pipeline](https://github.com/credkellar-boop/Monsnap/actions/workflows/super-lint.yml/badge.svg)](https://github.com/credkellar-boop/Monsnap/actions/workflows/super-lint.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org/)

MonSnap is an intelligent, high-performance edge computing video surveillance platform. Built using Python, OpenCV, and Google Cloud Services, MonSnap implements multi-threaded pipelines to capture real-time RTSP security camera feeds natively, cross-reference data using a centralized People Search engine, and execute contextual intelligence evaluations using Gemini AI and Google Maps.

---

## ✨ Advanced Features

* **Multi-Threaded Video Pipeline:** Eliminates hardware buffer latency by processing video ingestion on a dedicated background thread.
* **Gemini Multi-Modal Cognition:** Elevates basic edge computing to intelligent semantic security analysis by passing flagged frames directly to `gemini-2.5-flash`.
* **Google Maps Spatial Context:** Translates camera coordinate telemetry into human-readable physical addresses using reverse-geocoding engines.
* **Integrated People Search Directory:** Maps computer vision facial signature IDs instantly against enterprise profile matrices.
* **Automated CI/CD Pipeline:** Integrated GitHub Actions workflow to auto-lint and validate code health on every push.

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
│   ├── intel_engine.py      # Core Google Maps, Gemini, and People Search engine integration
│   └── stream_handler.py    # Threaded RTSPCameraStream connection manager
├── data/
│   ├── known_faces/         # Reference database for facial validation matching
│   └── snapshots/           # Target destination directory for captured faces
├── .gitignore               # Excludes virtual environments and temporary cache files
├── LICENSE                  # MIT Open-Source License
├── README.md                # Project documentation and deployment guide
├── main.py                  # Main orchestration loop and runtime logic
└── requirements.txt         # Project package dependencies
