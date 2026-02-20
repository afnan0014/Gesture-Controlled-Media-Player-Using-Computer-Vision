# 🎛️ Gesture-Controlled Media Player Using Computer Vision

A real-time computer vision system that enables **touchless media control** using hand gestures detected through a webcam.  
The system recognizes hand gestures and translates them into media control commands for VLC and other media players.

Built using **OpenCV**, **MediaPipe**, and **PyAutoGUI**, this project demonstrates practical Human–Computer Interaction (HCI) through AI-powered gesture recognition.

---

## 🚀 Features

✅ Real-time hand tracking using webcam  
✅ Gesture-based media control  
✅ Touchless interaction with VLC media player  
✅ Low-latency gesture recognition  
✅ Cooldown mechanism to prevent repeated triggers  
✅ Works with VLC, YouTube, and other media players

---

## 🧠 How It Works

1. Webcam captures live video frames.
2. MediaPipe detects hand landmarks (21 key points).
3. Finger states (up/down) are calculated.
4. Gestures are identified using landmark logic.
5. PyAutoGUI sends keyboard commands to control media playback.

   
---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| OpenCV | Video capture & image processing |
| MediaPipe | Hand landmark detection |
| PyAutoGUI | System keyboard automation |
| NumPy | Data processing |

---

## ✋ Gesture Controls

| Gesture | Finger Pattern | Action |
|--------|---------------|--------|
| Open Palm | `[1,1,1,1,1]` | Play / Pause |
| Index Finger | `[0,1,0,0,0]` | Volume Up |
| Pinky Finger | `[0,0,0,0,1]` | Volume Down |
| Index + Middle | `[0,1,1,0,0]` | Skip Forward |
| Index + Pinky | `[0,1,0,0,1]` | Skip Backward |
| Thumb | `[1,0,0,0,0]` | Change Subtitle |
| Thumb + Index | `[1,1,0,0,0]` | Change Audio Track |

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/gesture-media-control.git
cd gesture-media-control
```
### 2️⃣ Install dependencies

```bash
pip install opencv-python mediapipe pyautogui numpy
```

### 3️⃣ Download MediaPipe Model

hand_landmarker.task

### ▶️ Run the Project

```bash
python main.py
```

## 📂 Project Structure

gesture-media-control/
│
├── main.py
├── hand_landmarker.task
├── README.md
└── requirements.txt

