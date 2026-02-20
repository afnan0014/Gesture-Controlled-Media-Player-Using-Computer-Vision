import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import pyautogui
import time

# Load model
base_options = python.BaseOptions(
    model_asset_path="hand_landmarker.task"
)

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.VIDEO,
    num_hands=1
)

detector = vision.HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)

frame_id = 0

def fingers_up(hand_landmarks, frame_shape):
    h, w, _ = frame_shape

    # fingertip indexes
    tips = [4, 8, 12, 16, 20]

    fingers = []

    # Thumb (special case - x direction)
    if hand_landmarks[4].x < hand_landmarks[3].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers (y direction)
    for tip in tips[1:]:
        if hand_landmarks[tip].y < hand_landmarks[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers

last_action_time = 0
cooldown = 1.0  # seconds

def perform_action(fingers):
    global last_action_time

    current_time = time.time()

    if current_time - last_action_time < cooldown:
        return

    # OPEN PALM → Play/Pause
    if fingers == [1,1,1,1,1]:
        pyautogui.press("space")
        print("Play/Pause")

    # INDEX UP → Volume Up (UP ARROW)
    elif fingers == [0,1,0,0,0]:
        pyautogui.press("up")
        print("Volume Up")

    # PINKY UP → Volume Down (DOWN ARROW)
    elif fingers == [0,0,0,0,1]:
        pyautogui.press("down")
        print("Volume Down")

    # INDEX + MIDDLE → Skip Forward
    elif fingers == [0,1,1,0,0]:
        pyautogui.press("right")
        print("Skip Forward")

    # INDEX + PINKY → Skip Back
    elif fingers == [0,1,0,0,1]:
        pyautogui.press("left")
        print("Skip Back")

    # THUMB UP ONLY → Change Subtitle (C)
    elif fingers == [1,0,0,0,0]:
        pyautogui.press("v")
        print("Subtitle Changed")

    # THUMB + INDEX → Change Audio Track (V)
    elif fingers == [1,1,0,0,0]:
        pyautogui.press("b")
        print("Audio Track Changed")

    last_action_time = current_time
    
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    results = detector.detect_for_video(mp_image, frame_id)
    frame_id += 1

    # Draw landmarks
    if results.hand_landmarks:
      for hand in results.hand_landmarks:

        fingers = fingers_up(hand, frame.shape)
        perform_action(fingers)

        print(fingers)

        for lm in hand:
            h, w, _ = frame.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(frame, (cx, cy), 5, (0,255,0), -1)

    cv2.imshow("Hand Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()