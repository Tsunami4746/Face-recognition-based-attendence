# Facial-attendence

# 🧠 Face Recognition Attendance System

A Python-based real-time attendance system using face recognition through your webcam. It captures faces, encodes them into unique data, and automatically marks attendance with timestamps in a CSV file.

---

## 📌 Features

- ✅ Real-time face detection and recognition
- ✅ Automatic attendance logging (Name + Time)
- ✅ Face data capture per user
- ✅ CSV-based attendance log
- ✅ Lightweight and modular code structure

---

## 🗂️ Project Structure

face_attendance/
├── dataset/ # Captured face images per person
├── encodings.pickle # Stored face encodings for recognition
├── attendance.csv # Output CSV attendance log
├── capture_faces.py # Capture face images via webcam
├── encode_faces.py # Encode and save face data
├── recognize_faces.py # Recognize and log attendance in real-time


---

## 🔧 Requirements

Install required Python packages:

```bash
pip install opencv-python face-recognition numpy pandas cmake
```
🚀 Getting Started
1. Capture Faces
Run this to capture images of a person's face:
```bash
python capture_faces.py
```
Enter the user's name when prompted.

Face images will be saved to dataset/<Name>/.

2. Encode Captured Faces
Convert saved face images into encodings:
```bash
python encode_faces.py
```
Creates encodings.pickle containing known face data.

3. Start Attendance System
Run the real-time face recognition system:
```
python recognize_faces.py
```
Recognizes faces using webcam.

Logs attendance to attendance.csv.

Press q to exit the webcam window.

📄 Output
attendance.csv (sample)
```makefile
Name,Time
Alice,09:42:18
Bob,09:45:10
```
# 🚧 Future Improvements
🗓️ Daily logs with date stamps

💾 Database storage (SQLite, Firebase)

🖼️ GUI using Tkinter or PyQt

📤 Export attendance to Excel/PDF

👤 Author:
Tsunami 

📜 License
MIT License – Free for personal or commercial use.
