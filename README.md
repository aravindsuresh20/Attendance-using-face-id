# 🎥 Face Recognition Attendance System

This project implements a comprehensive **Face Recognition Attendance System** using **Python**, **Dlib**, **OpenCV**, and **Flask**.  
It supports registering new faces, extracting features, real-time recognition via webcam, logging attendance into an SQLite database, and viewing records through a Flask web app.

---

## 🚀 Features

- **Face Registration GUI** (`get_faces_from_camera_tkinter.py`)  
  Capture multiple face images and assign them to a person's name using a Tkinter interface.

- **Feature Extraction** (`features_extraction_to_csv.py`)  
  Extracts 128D face descriptors using Dlib's ResNet and stores them in `features_all.csv`.

- **Real-time Face Recognition & Attendance Logging** (`attendance_taker.py`)  
  Recognizes registered faces via webcam and logs name, time, and date into `attendance.db`.

- **Web-Based Attendance Viewer** (`app1.py`)  
  Flask app to view attendance records with a simple login interface.

- **Script Execution Utility (Optional)** (`app.py`)  
  Launch other scripts via a web interface (demonstration only).

---

## 🧰 Requirements

Ensure these libraries are installed:

- `Python 3.x`
- `dlib`
- `opencv-python`
- `numpy`
- `pandas`
- `Flask`
- `Pillow`
- `tkinter` (built-in)
- `sqlite3` (built-in)

Dlib pre-trained models are required:
- `shape_predictor_68_face_landmarks.dat`
- `dlib_face_recognition_resnet_model_v1.dat`

Install dependencies via `requirements.txt`.

---

## 📁 Project Structure

/your-project-directory/
├── app.py
├── app1.py
├── attendance_taker.py
├── features_extraction_to_csv.py
├── get_faces_from_camera_tkinter.py
├── requirements.txt
├── README.md
│
├── /data/
│ ├── /data_dlib/
│ │ ├── shape_predictor_68_face_landmarks.dat
│ │ └── dlib_face_recognition_resnet_model_v1.dat
│ ├── /data_faces_from_camera/
│ │ └── person_1_John/
│ │ ├── img_face_1.jpg
│ │ └── ...
│ └── features_all.csv
│
├── attendance.db
│
└── /templates/
├── index.html
├── login.html
└── index1.html

yaml
Copy
Edit

---

## 🔧 Installation & Setup

### 1. Clone the Project
```bash
git clone https://github.com/yourusername/face-recognition-attendance.git
cd face-recognition-attendance
2. Download Dlib Models
Place shape_predictor_68_face_landmarks.dat and dlib_face_recognition_resnet_model_v1.dat in data/data_dlib/.

Ensure they are directly in the folder, not in subdirectories.

3. Create requirements.txt
txt
Copy
Edit
dlib
opencv-python
numpy
pandas
Flask
Pillow
4. (Optional) Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
5. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
✅ Usage
🔹 Step 1: Register Faces
bash
Copy
Edit
python get_faces_from_camera_tkinter.py
Click Clear to reset data (optional).

Enter a name and click Input.

Capture multiple face angles (click Save current face multiple times).

🔹 Step 2: Extract Face Features
bash
Copy
Edit
python features_extraction_to_csv.py
Generates features_all.csv using Dlib's 128D facial encodings.

🔹 Step 3: Run Attendance System
bash
Copy
Edit
python attendance_taker.py
Recognizes registered faces.

Logs attendance in attendance.db.

Press q to quit webcam.

🔹 Step 4: View Attendance (Web Interface)
bash
Copy
Edit
python app1.py
Go to http://127.0.0.1:5000

Login credentials:

Username: admin

Password: password

Select a date to view attendance.

ℹ️ Notes on app.py
app.py is a utility Flask app to demonstrate how you could trigger other Python scripts via browser.
This is optional and not required for core attendance functionality.

📌 Tips
Always extract features again if new faces are added.

Ensure lighting is good during face registration and recognition.

One face in frame = better accuracy.

