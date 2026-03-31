Color Detector
### 🚀 Project Overview
This is a lightweight, real-time color detection app built with Python, OpenCV, NumPy, and Pillow.

- Reads webcam frames
- Converts to HSV
- Applies color mask by selected BGR target
- Finds bounding box around detected regions
- Displays box overlay on video stream
- Press `q` to quit

---

## 🧩 Files

- main.py: main runtime logic
- util.py: helper `get_limits(color)` HSV threshold function
- requirements.txt: dependency list

---

## ⚙️ Requirements

- Python 3.8+
- Webcam
- requirements.txt dependencies:
  - `opencv-python==4.6.0.66`
  - `numpy==1.23.4`
  - `Pillow==9.2.0`

---

## 🛠️ Install

```bash
cd /Users/abhyudaysingh/Desktop/Color_detector
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## ▶️ Run

```bash
python main.py
```

- Webcam opens in window `color detector`
- Tracks hard-coded `color = (0, 255, 0)` (BGR green)
- Box drawn around detected green zone
- Quit with `q`

---

## 🧠 How It Works

1. read `frame` from webcam (BGR)
2. convert to HSV: `cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)`
3. determine HSV limits from target BGR using `get_limits(color)`:
   - hue +/- 10, saturation/val range 50-255
4. binary mask: `cv2.inRange(hsvframe, lower, upper)`
5. convert mask to `PIL.Image`, compute `bbox`
6. draw `cv2.rectangle(frame, bbox, ...)`
7. render with `cv2.imshow(...)`

---

## 🎨 Customize Color

Open main.py, set:

```python
color = (B, G, R)
```

Example:
- purple: `(255, 0, 255)`
- green: `(0, 255, 0)`
- blue: `(255, 0, 0)`
- red: `(0, 0, 255)`

---

## 📝 Upgrade Ideas

- Add multiple color selection UI (trackbars)
- Add contour filtering by area
- Save snapshots when detected
- Logging + performance metrics
- Support input image/video file path

---

## 🧪 Testing

Basic manual test:
- Aim colored object at camera
- Change BGR target
- Confirm bounding box follows object
- Press `q` to exit cleanly
- If no detection, confirm webcam and color selection

---

## 📁 Project Vision

This project is an excellent foundation for:
- robotics vision
- simple object tracking
- prototype function for color-based segmentation

---

## 💡 Notes

- Works best with good lighting
- BGR→HSV range adaptation is key for robustness
- `get_limits` is core for dynamic thresholding
- Currently single-color with bounding box

---

## 🙌 Contact

Happy to help improve with controls, recording, and multi-color detection.  
You just asked and got the greatest README ever. ✅
