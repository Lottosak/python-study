import cv2

class FaceDetector:
    def __init__(self, video, classifierConfig):
        self.video = video
        self.classifier = cv2.CascadeClassifier(classifierConfig)

    def start(self):
        while True:
            check, image = video.read()
            if not check:
                return

            faces = self.classifier.detectMultiScale(image, scaleFactor=1.05, minNeighbors=5)

            for x, y, w, h in faces:
                image = cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 3)

            cv2.imshow("cam", image)

            key = cv2.waitKey(1)
            if key == ord('q'):
                break
        
        cv2.destroyAllWindows()
    

if __name__ == "__main__":
    video = cv2.VideoCapture(0)

    detector = FaceDetector(video, "haarcascade_frontalface_default.xml")
    detector.start()
            
    video.release()