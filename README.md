# Virtual Keyboard using Computer Vision 🎹

A prototype virtual keyboard built using Python, OpenCV, and MediaPipe.
The system uses a camera (phone via DroidCam) to detect hand landmarks
and allows typing by tapping gestures.

## Features
- Real-time camera input
- Hand landmark detection
- Virtual keyboard rendering
- Tap-based key detection
- OS-level key input

## Tech Stack
- Python 3.11
- OpenCV
- MediaPipe
- Pynput


## 📱 Camera Setup (DroidCam)

This project supports using a **smartphone as a camera** via **DroidCam**.

### Steps:
1. Install **DroidCam** on your phone (Android / iOS)
2. Install **DroidCam Client** on your laptop
3. Connect phone and laptop using **USB or Wi-Fi**
4. Start DroidCam and note the camera index (usually `1`)
5. Update `main.py`:
   ```python
   cam = CameraStream(camera_index=1)
   
## How to Run
```bash
git clone https://github.com/your-username/virtual-keyboard.git
cd virtual-keyboard
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
