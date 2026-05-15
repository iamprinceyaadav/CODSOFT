import cv2
import os

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

def detect_faces_image(image_path):
    # Image load karo
    img = cv2.imread(image_path)
    if img is None:
        print("Image nahi mili!")
        return
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Faces detect karo
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    
    print(f"Kitne faces mile: {len(faces)}")
    
    # Har face pe rectangle banao
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img, "Face", (x, y-10),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    # Result dikhao
    cv2.imshow("Face Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def detect_faces_webcam():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Webcam nahi mila!")
        return
    
    print("Webcam chal raha hai... 'q' dabaao band karne ke liye!")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, f"Face Detected", (x, y-10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
        # Kitne faces hain
        cv2.putText(frame, f"Faces: {len(faces)}", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        cv2.imshow("Face Detection - Webcam", frame)
        
        # Q dabaao band karne ke liye
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

def main():
    print("=" * 40)
    print("   Face Detection System!")
    print("=" * 40)
    print("\n1. Webcam se detect karo")
    print("2. Image se detect karo")
    
    choice = input("\nChoice karo (1/2): ")
    
    if choice == "1":
        detect_faces_webcam()
    elif choice == "2":
        image_path = input("Image ka path do: ")
        detect_faces_image(image_path)
    else:
        print("Galat choice!")

if __name__ == "__main__":
    main()