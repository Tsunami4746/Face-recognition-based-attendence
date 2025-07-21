import cv2
import os

name = input("Enter the name of the person: ").strip()
path = f"dataset/{name}"

os.makedirs(path, exist_ok=True)

cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Capture Face - Press Q to Quit", frame)
    
    if count % 5 == 0:
       img_path = os.path.join(path, f"{count}.jpg")
       cv2.imwrite(img_path, frame)


    count += 1

    if cv2.waitKey(1) & 0xFF == ord('q') or count > 50:
        break

cap.release()
cv2.destroyAllWindows()