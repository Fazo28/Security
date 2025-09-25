# 🛡️ Python Security Camera Tool

A simple motion-detection security camera built with Python and OpenCV.  
The tool uses your webcam (or an IP camera) to detect movement and save snapshots when motion occurs.  

---

## 🚀 Features
- Motion detection using frame difference
- Saves snapshots automatically in `output/`
- Live camera feed with motion highlights
- Cross-platform (Windows, Linux, macOS)

---

## 📦 Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/Fazo28/security.git
   cd security
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage
Run the tool:
```bash
python camera.py
```

- A window will open showing your camera feed  
- Green boxes appear when motion is detected  
- Snapshots are saved in the `output/` folder  
- Press **q** to quit  

---

## ⚡ Example Output
Snapshots look like this:

```
output/
 ├── motion_20250925_153000_0.jpg
 ├── motion_20250925_153005_1.jpg
```

---

## 🛠️ Future Upgrades
- Email / Telegram alerts  
- Video recording instead of snapshots  
- Run on Raspberry Pi for DIY home security  

---

## 📜 License
MIT License
