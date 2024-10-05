import cv2
import numpy as np
import os

class StopMotionStudio:
    def __init__(self):
        self.frames = []
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            raise IOError("Cannot open webcam")

    def capture_frame(self):
        ret, frame = self.cap.read()
        if ret:
            self.frames.append(frame)
            print("Frame captured")
        else:
            print("Failed to capture frame")

    def preview_animation(self):
        for frame in self.frames:
            cv2.imshow('Preview', frame)
            if cv2.waitKey(200) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()

    def export_video(self, output_file='animation.mp4'):
        if not self.frames:
            print("No frames to export")
            return

        height, width, _ = self.frames[0].shape
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_file, fourcc, 10, (width, height))
        
        for frame in self.frames:
            out.write(frame)
        
        out.release()
        print(f"Video exported as {output_file}")

    def run(self):
        while True:
            ret, frame = self.cap.read()
            cv2.imshow('Stop Motion Studio', frame)
            
            key = cv2.waitKey(1) & 0xFF
            if key == ord('c'):
                self.capture_frame()
            elif key == ord('p'):
                self.preview_animation()
            elif key == ord('e'):
                self.export_video()
            elif key == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    studio = StopMotionStudio()
    studio.run()
