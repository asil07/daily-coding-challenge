import cv2
import mediapipe as mp

# Initialize Mediapipe Pose class
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Initialize drawing class
mp_drawing = mp.solutions.drawing_utils

# Capture video feed (you can use a webcam or a sports video file)
cap = cv2.VideoCapture(0)  # Use 0 for webcam, or provide a video file path

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert the frame to RGB since Mediapipe processes RGB images
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame with Mediapipe Pose
    result = pose.process(rgb_frame)
    
    # Draw pose landmarks on the frame if detected
    if result.pose_landmarks:
        mp_drawing.draw_landmarks(frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Display the frame with pose landmarks
    cv2.imshow('Pose Estimation', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
