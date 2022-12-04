from keras.models import load_model
import cv2
import numpy as np
from random import choice

REV_CLASS_MAP = {
    0: "left",
    1: "right",
    2: "straight",
    3: "none"
}


def mapper(val):
    return REV_CLASS_MAP[val]



model = load_model("linedetect-model.h5")

cap = cv2.VideoCapture(0)

prev_move = None

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # rectangle for user to play
    cv2.rectangle(frame, (70, 70), (300, 300), (255, 255, 255), 2)
    # rectangle for computer to play

    # extract the region of image within the user rectangle
    roi = frame[70:300, 70:300]
    img = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (227, 227))

    # predict the move made
    pred = model.predict(np.array([img]))
    move_code = np.argmax(pred[0])
    user_move_name = mapper(move_code)

    # predict the winner (human vs computer)
    # display the information
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Line is: " + user_move_name,
                (50, 50), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)


    cv2.imshow("Rock Paper Scissors", frame)

    k = cv2.waitKey(2)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
