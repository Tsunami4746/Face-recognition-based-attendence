import face_recognition
import os
import cv2
import pickle

data = {}
dataset_path = "dataset/"

for user in os.listdir(dataset_path):
    user_path = os.path.join(dataset_path, user)
    for img_name in os.listdir(user_path):
        img_path = os.path.join(user_path, img_name)
        image = cv2.imread(img_path)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        boxes = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, boxes)

        if encodings:
           data[user] = data.get(user, []) + [encodings[0]]

for key in data:
    data[key] = sum(data[key]) / len(data[key])  # Average encoding

with open("encodings.pickle", "wb") as f:
    pickle.dump(data, f)

print("Encodings saved.")