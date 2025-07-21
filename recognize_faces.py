import cv2 
import face_recognition
import pickle
import os
import pandas as pd
from datetime import datetime


with open("encodings.pickle", "rb") as f:
    known_encodings = pickle.load(f)

known_name = list(known_encodings.keys())
known_faces = list(known_encodings.values())


attendance_file = "attendence.csv"

try:
    df = pd.read_csv(attendance_file)
except:
    df = pd.DataFrame(columns=["Name", "Time"])

seen_today = set(df["Name"].values)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, boxes)

    for encoding, box in zip(encodings, boxes):
        matches = face_recognition.compare_faces(known_faces, encoding, tolerance=0.6)
        name = "Unknown"

        if True in matches:
            matched_idx = matches.index(True)
            name = known_name[matched_idx]

            if name not in seen_today:
                seen_today.add(name)
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                new_row = pd.DataFrame([{"Name": name, "Time": now}])
                df = pd.concat([df, new_row], ignore_index=True)
                df.to_csv(attendance_file, index=False)
        

        top, right, bottom, left = box
        cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,255,0), 2)

    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()